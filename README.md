 🤖 GenAI Multilingual Chatbot

> A high-performance, context-aware conversational AI application powered by **Groq**, **LangChain**, and **LangSmith Observability**.

---

📌 Overview

This project is a modern Generative AI chatbot designed for high-speed inference and seamless multilingual conversations. Built using **LangChain LCEL (LangChain Expression Language)** and **Groq's LPU acceleration**, the assistant remembers chat history, supports custom system prompts, and seamlessly switches between multiple languages (English, Hindi, Telugu, Spanish, French).

The application includes end-to-end telemetry and monitoring through **LangSmith**, tracking latency, token consumption, and execution pipelines in real time.

---

✨ Key Features

* ⚡ **Ultra-Fast Responses:** Powered by Groq LPU engine running state-of-the-art open-weights models (`openai/gpt-oss-120b`).
* 💬 **Context-Aware Memory:** Retains multi-turn conversation history within active sessions.
* 🌐 **Multilingual Support:** Dynamic language adaptation across English, Hindi, Telugu, Spanish, French, and more.
* 📊 **Full Observability:** Automatic tracing and prompt evaluation via LangSmith integration.
* 🎨 **Dual Frontend Options:** Includes both a ready-to-use **Streamlit UI** and a custom **Flask + Tailwind CSS** interface.

---

🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Language Engine** | Python 3.10+ |
| **LLM Provider** | Groq API (`openai/gpt-oss-120b`) |
| **Orchestration** | LangChain Core (`ChatGroq`, `ChatPromptTemplate`, LCEL) |
| **Monitoring** | LangSmith SDK |
| **Frontend Options** | Streamlit / Flask + Tailwind CSS |

---

## 📂 Project Structure

```text
genai-chatbot/
│
├── .env                      # API keys & environment configuration (Do NOT commit)
├── .gitignore                # Git ignore rules
├── requirements.txt          # Python dependencies
├── app.py                    #Flask server
└── templates/
    └── index.html            # Tailwind CSS UI
