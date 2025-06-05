# 🤖 AI Agents

Welcome to Akshay Patel's AI Agent Suite!  
This repository contains three AI-powered chatbot systems:

1. Local Ollama Chatbot Server (`phi3`)
2. Ollama Chatbot Web Frontend (React UI)
3. Gemini-Powered Personal AI Agent (Streamlit app)

---

## 1. Getting Started with the Ollama Chatbot Server

Run a local LLM server powered by Ollama.

### Steps:

1. Install Ollama (only once):  
   👉 [https://ollama.com/download](https://ollama.com/download)

2. Run the model:
   ```bash
   ollama run phi3
   ```

3. Open the terminal in the `ollama_chatbot_server` folder.

4. Start the Python app:
    ```bash
    python app.py
    ```

---
## 2. Starting the Ollama Chatbot Web
Launch a React-based UI that connects to the Ollama server.

### Steps:

1. Open the terminal in the `ollama_chatbot_web` folder.

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the frontend:
    ```bash
    npm start
    ```

4. A new web page will open with a button in the center.

5. Click the `OPEN CHAT` button to enter the chatbot interface.

---
## 3. Gemini-Powered Personal AI Agent (Streamlit)
This project includes two Streamlit-based applications that use Google Gemini via the google-generativeai library to answer questions about Akshay Patel using a personalized knowledge base.

### 1. `personal_ai_agent.py`  
A minimal, hardcoded version of the agent with Akshay’s profile embedded in the code.
- Static profile
- Basic chatbot UI
### 2. `personal_ai_agent_dynamic.py`  
An advanced version where you can upload a `.txt` or `.md` file or edit the profile directly in the app sidebar.

- Upload profile file (`.txt`, `.md`)
- Edit and reload profile live
- Automatically resets Gemini's context
- Full chat memory



### Steps:
1. Install the required Python packages:
    ```bash
    pip install streamlit google-generativeai
    ```

2. Get your Gemini API key: 
    👉 [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

3. Paste your key into the script: 
    ```bash
    genai.configure(api_key="your_gemini_api_key_here")
    ```

4. Run the python file:
    ```bash
    streamlit run personal_ai_agent.py
    ```
    or
    ```bash
    streamlit run personal_ai_agent_dynamic.py
    ```
