# Product Requirement Document Generator

A lightweight Streamlit-based application that uses the Qwen 3 1.7B model via [Ollama](https://ollama.com) to generate high-quality Product Requirement Documents (PRDs) from user prompts.

---

## ✨ Features

- 💬 Chat interface powered by Streamlit
- 🤖 Real-time response streaming from Qwen 3.1.7B using Ollama
- 🧠 Internal reasoning shown in a collapsible section (`<think>...</think>`)
- 📋 Copy-to-clipboard support for generated PRDs
- 🧱 Clear markdown output of PRDs for further processing
- 🔁 Chat history maintained using `st.session_state`

---

## 📁 File Structure
```
├── env/
│   └── agent.py        # Main app file
└── README.md           # Project description and instructions

```

---

## ⚙️ Setup Instructions

### 1. Requirements

- Python 3.8+
- [Ollama](https://ollama.com) installed and running locally
- Required Python packages:
  - `streamlit`
  - `requests`

### 2. Install Dependencies

```bash
pip install streamlit requests

# Start the Ollama model server (Qwen 3.1.7B)
ollama run qwen3:1.7b

# Run the Streamlit app
streamlit run env/agent.py

```

## 🧠 How It Works

- User enters a product idea in the chat box.
- The app sends a streaming request to the Qwen 3.1.7B model served by Ollama.
- Response includes `<think>...</think>` blocks for internal reasoning.
- Internal thoughts are extracted and shown in an expandable box.
- The remaining content is treated as the Product Requirement Document and displayed.
- A “📋 Copy to Clipboard” button allows users to quickly copy the output PRD.

## 📌 Notes

- Clipboard copy is implemented via `components.html()` using JavaScript.
- Regular expressions are used to separate `<think>` content from the actual PRD.
- Streamed content is appended chunk-by-chunk for responsive UI.


Connect me on [LinkedIn](www.linkedin.com/in/snehal-python) for collaborations 
