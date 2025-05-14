import requests
import json
import re
import streamlit as st
import html
import streamlit.components.v1 as components
st.set_page_config(
    page_title="PRD Generator ",
    page_icon="📄"
)
st.title("📄 PRD Generator : Powered by Qwen 3 ")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "system",
        "content": (
            "Act as an experienced Product Requirement Document Generator. "
            "You have been powered by Qwen 3. You know how to write detailed Product Requirement Documents. "
            "Your output will be used by other AI agents to build end-to-end production-ready applications and websites."
        )
    }]

for message in st.session_state.messages:
    if message['role'] != 'system':
        with st.chat_message(message['role']):
            st.markdown(message['content'])

if prompt := st.chat_input("Write your requirements !!"):
    st.session_state.messages.append({'role':'user','content':prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Use `st.markdown` to display the complete response
    with st.chat_message('assistant'):
        ollama_url : str = "http://localhost:11434/api/chat"

        payload : dict = {
            "model" : "qwen3:1.7b",
            "messages":[{
                "role": m['role'],
                "content":m['content']

            }
            for m in st.session_state.messages],
            "temperature" : 0.85

        }

        response = requests.post(ollama_url,json=payload, stream=True)
        complete_response = ""
        placeholder = st.empty()

        for chunk in response.iter_lines():
            if chunk:
                content = json.loads(chunk.decode('utf-8'))['message']['content']
                complete_response += content
        think_match = re.search(r"<think>(.*?)</think>", complete_response, re.DOTALL)
        thinking = think_match.group(1).strip() if think_match else None
        prd_body = re.sub(r"<think>.*?</think>", "", complete_response, flags=re.DOTALL).strip()

        if thinking:
            with st.expander("🤔 Internal Reasoning (Click to view)", expanded=False):
                st.markdown(thinking)

        placeholder.markdown("### 📄 Product Requirement Document")

        placeholder.code(prd_body, language='markdown')

        safe_response = html.escape(complete_response).replace("\n", "\\n").replace("`", "\\`")

        components.html(f"""
        <button onclick="navigator.clipboard.writeText(`{safe_response}`)" 
                style="margin-top: 10px; background-color: #4CAF50; color: white; border: none; padding: 8px 12px; border-radius: 4px; cursor: pointer;">
            📋 Copy to Clipboard
        </button>
        """,height=60)


    st.session_state.messages.append({'role':'assistant', 'content': complete_response})

st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #888; padding: 10px;">
        Made with ❤️ using Qwen3:1.7B | Ollama
    </div>
    """, 
    unsafe_allow_html=True
)