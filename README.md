# 🧳 Travel Agent Chatbot

A friendly AI-powered travel agent chatbot built using **LangGraph**, **Groq**, and **Streamlit**. Ask about tourist attractions in any U.S. city, and it will respond with insightful, city-specific travel recommendations.

---

## 🌍 Features

- 💬 Conversational chat interface using Streamlit
- 🧠 Built with `LangGraph`'s `create_react_agent`
- ⚡ Powered by `Groq` (LLaMA 3.1 - 8B Instant)
- 🛠️ Custom tool used to extract the city name from user queries
- 🎯 Personalized travel responses using LLM knowledge (not from static tool output)

---
## Technologies Used:

| Tool                | Purpose                          |
| ------------------- | -------------------------------- |
| **Streamlit**       | Web interface & chat layout      |
| **LangGraph**       | Agent orchestration              |
| **Groq API**        | Model inference (LLaMA 3.1 - 8B) |
| **LangChain Tools** | Tool wrapping and invocation     |
| **Python-dotenv**   | Local API key management         |



## How to Run:

### 1. Clone the Repository


git clone https://github.com/yourusername/travel-agent-chatbot.git

cd travel-agent-chatbot

### 2. Install Dependencies

pip install -r requirements.txt

### 3. Set Up Environment Variables
Create a .env file in the root directory and add your Groq API key:

GROQ_API_KEY=your_groq_api_key_here

### 4. Run the App

python file_name.py


## 🧠 How It Works:

*A custom LangGraph agent is created using create_react_agent.

*A tool named tourist_guide is used only to extract the city name from user input.

*The model then uses its own trained knowledge to generate an accurate, warm, travel-oriented response.

*Responses are streamed and shown using st.chat_message() in a Streamlit chatbot UI.

