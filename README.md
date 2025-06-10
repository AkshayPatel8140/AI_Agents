# 🤖 AI Agents

Welcome to Akshay Patel's AI Agent Suite!  
This repository contains three AI-powered chatbot systems:

1. Local Ollama Chatbot Server (`phi3`)
2. Ollama Chatbot Web Frontend (React UI)
3. Gemini-Powered Personal AI Agent (Streamlit app)
4. Ollama With RAG AI Agent for Pizza Store (Ollama `llama3.2`)
5. LangChain Research AI Agent

---
---

# 1. Getting Started with the Ollama Chatbot Server

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
---
# 2. Starting the Ollama Chatbot Web
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
---
# 3. Gemini-Powered Personal AI Agent (Streamlit)
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

---
---
# 4. Ollama With RAG AI Agent for Pizza Store review (Ollama `llama3.2`)
### Overview

This project is an AI-powered agent designed to answer user questions about a pizza restaurant by leveraging real customer reviews. It uses Retrieval-Augmented Generation (RAG) to provide accurate and context-aware responses based on previously collected reviews.

---
### How It Works

1. **Data Ingestion & Embedding**  
   - The project loads a CSV file containing realistic pizza store reviews.
   - Each review is converted into an embedding using the Ollama LLM model.
   - These embeddings are stored in a Chroma vector database for efficient retrieval.

2. **Retrieval-Augmented Generation (RAG)**  
   - When a user asks a question, the system retrieves the most relevant reviews from the database using vector similarity search.
   - The retrieved reviews and the user's question are combined into a prompt.

3. **Intelligent Response Generation**  
   - The prompt is sent to the Ollama LLM, which generates a detailed and contextually relevant answer based on the reviews.

---
### Features

- **Contextual Answers:** Responses are grounded in real customer feedback.
- **Efficient Search:** Uses vector embeddings for fast and relevant review retrieval.
- **Interactive CLI:** Users can ask questions in a command-line interface.

---
### Technologies Used

- [LangChain](https://www.langchain.com/) (Ollama LLM, Chroma vector store)
- Python
- Pandas

---
### Usage

1. Open the terminal in the `ollama_With_RAG_AI_Agent` folder.

2. Run the command to install the `requirements.txt`
    ```bash
    pip install -r requirements.txt
    ```
3. Run the `main.py` file
    ```bash
    python run main.py
    ```

---
### Example

```
Ask your question (q to quit): What do people say about the crust?
[AI]: Most reviews mention that the crust is crispy and flavorful...
```

---
This project demonstrates how to combine LLMs and vector databases to build intelligent, review-based Q&A agents for businesses.

---
---
# 5. LangChain Research AI Agent

### Overview

This project is an AI-powered research assistant that helps users generate structured research summaries on any topic. It leverages advanced language models (Anthropic Claude 3.5 Sonnet) and integrates external tools (web search, Wikipedia, file saving) to provide comprehensive, well-sourced answers in a consistent format.

---
### Features

- **Structured Research Output:** Returns research results in a standardized format (topic, summary, sources, tools used).
- **Tool Integration:** Uses web search, Wikipedia, and file-saving tools to enhance research capabilities.
- **LLM-Powered Reasoning:** Utilizes Anthropic Claude 3.5 Sonnet for high-quality, context-aware responses.
- **Extensible:** Easily add or modify tools for custom research workflows.
- **Interactive CLI:** Users can input research queries directly in the terminal.

---
### How It Works

1. **User Query:**  
   The user is prompted to enter a research question.

2. **Agent Reasoning:**  
   The agent uses the language model and available tools to gather information, summarize findings, and cite sources.

3. **Structured Output:**  
   The response is formatted using a Pydantic schema, ensuring consistency and easy downstream processing.

4. **Error Handling:**  
   If the output cannot be parsed, the raw response is displayed for debugging.

---
### Project Structure

- `main.py` — Main entry point; handles agent setup, user interaction, and output parsing.
- `tools.py` — Custom tool definitions (web search, Wikipedia, save to file).
- `.env` — Store your API keys and environment variables here.

---
### Requirements

- Python 3.9+
- [LangChain](https://www.langchain.com/)
- [Anthropic API access](https://docs.anthropic.com/claude/docs/quickstart)
- [Pydantic](https://docs.pydantic.dev/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

Install dependencies:
```bash
pip install -r requirements.txt
```

---
### Environment Setup

Create a `.env` file in the project root with your API keys:
```
ANTHROPIC_API_KEY=your_anthropic_api_key
OPENAI_API_KEY=your_openai_api_key  # if using OpenAI tools
```

---
### Example Usage

```bash
python main.py
```

**Sample Interaction:**
```
What can i help you research? The impact of AI on healthcare
ResearchResponse(
    topic='The impact of AI on healthcare',
    summary='AI is transforming healthcare by improving diagnostics, personalizing treatment, and streamlining administrative tasks...',
    sources=['https://en.wikipedia.org/wiki/Artificial_intelligence_in_healthcare', ...],
    tools_used=['web_search', 'wikipedia']
)
```

---
### Customization

- Add or modify tools in `tools.py` to extend the agent's capabilities.
- Adjust the Pydantic schema in `main.py` for different output formats.

---

This project demonstrates how to combine LLMs, tool use, and structured output for advanced research automation.