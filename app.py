import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

# Load environment variables (LangSmith tracing works automatically)
load_dotenv()

app = Flask(__name__)

# Initialize Groq Model
groq_api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(
    model_name="openai/gpt-oss-120b",
    groq_api_key=groq_api_key,
    temperature=0.7
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful, accurate, and polite AI assistant. Answer in {language}."),
    MessagesPlaceholder(variable_name="messages")
])

chain = prompt | llm

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    raw_history = data.get("messages", [])
    language = data.get("language", "English")

    # Reconstruct LangChain message objects
    formatted_messages = []
    for msg in raw_history:
        if msg["role"] == "user":
            formatted_messages.append(HumanMessage(content=msg["content"]))
        elif msg["role"] == "assistant":
            formatted_messages.append(AIMessage(content=msg["content"]))

    try:
        response = chain.invoke({"messages": formatted_messages, "language": language})
        return jsonify({"success": True, "reply": response.content})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)