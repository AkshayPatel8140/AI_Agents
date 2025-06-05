import streamlit as st
import google.generativeai as genai

# === Configure Gemini API ===
genai.configure(api_key="your_gemini_api_key_here")
# === Gemini Model Setup ===
model = genai.GenerativeModel("gemini-2.0-flash")

# === 2. Define Your Personal Profile (Knowledge Base) ===
AKSHAY_PROFILE = """
Akshay Patel is a Full Stack Engineer with over 4.5 years of experience in software development. 
He specializes in React Native, TypeScript, Node.js, AWS, PostgreSQL, and Python. 
He has worked at eInfochips, Moon Technolabs, and Virtual Heights, and is currently pursuing an MS in Computer Science at San Francisco Bay University.

Akshay has built several notable projects including:
- AI Academic Advisor: An AI-powered educational assistant.
- TaskHive: A productivity and task management tool with project hierarchies.
- SEEKRZ: A job-matching and career planning platform.
- A POS system for the USA market.

He is passionate about AI, automation, and hackathons. He won the AI Supply Chain Hackathon and frequently works on real-time AI agents and full-stack projects.

Contact: akshay@example.com
GitHub: https://github.com/akshaypatel
LinkedIn: https://linkedin.com/in/akshaypatel
"""

# === Initialize session state for message history ===
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat()
    # Inject your personal profile as the first message
    st.session_state.chat_session.send_message(
        "You are an AI assistant that knows everything about Akshay Patel. "
        "Use the following profile to answer questions:\n\n" + AKSHAY_PROFILE
    )
if "messages" not in st.session_state:
    st.session_state.messages = []

if "messages" not in st.session_state:
    st.session_state.messages = []

# === Streamlit UI ===
st.set_page_config(page_title="Akshay Patel – AI Chat Agent", layout="centered")
st.title("🤖 Ask About Akshay Patel")

# Display chat history
for role, message in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(message)

# User input
prompt = st.chat_input("Ask me anything about Akshay Patel...")

if prompt:
    # Display user message
    st.session_state.messages.append(("user", prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get Gemini response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat_session.send_message(prompt)
            st.markdown(response.text)

    # Save assistant response
    st.session_state.messages.append(("assistant", response.text))
