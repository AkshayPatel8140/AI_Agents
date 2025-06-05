import streamlit as st
import google.generativeai as genai

# === 1. Configure Gemini API Key ===
genai.configure(api_key="your_gemini_api_key_here")

# === 2. Streamlit App Setup ===
st.set_page_config(page_title="Akshay Patel – AI Chat Agent", layout="centered")
st.title("🤖 Ask About Akshay Patel")

# === 3. Upload or Edit Profile Section ===
st.sidebar.header("📝 Upload or Edit Akshay's Profile")

uploaded_file = st.sidebar.file_uploader(
    "Upload a profile file (.txt or .md)", type=["txt", "md"]
)

if uploaded_file:
    AKSHAY_PROFILE = uploaded_file.read().decode("utf-8")
else:
    AKSHAY_PROFILE = st.sidebar.text_area(
        "Or paste Akshay's profile here:",
        height=300,
        value="""
Akshay Patel is a Full Stack Engineer with 4.5+ years of experience. He works with React Native, TypeScript, Node.js, AWS, and PostgreSQL. Currently pursuing MS CS at SFBU. Built TaskHive, AI Academic Advisor, SEEKRZ, and POS system. Won AI Supply Chain Hackathon.
Contact: akshay@example.com
GitHub: https://github.com/akshaypatel
LinkedIn: https://linkedin.com/in/akshaypatel
""",
    )

# === 4. (Re)Start Chat Session on Profile Change ===
if st.sidebar.button("🔄 Load this profile into AI agent"):
    model = genai.GenerativeModel("gemini-2.0-flash")
    chat = model.start_chat()
    chat.send_message(
        "You are an AI agent that knows everything about Akshay Patel. Use the following profile to answer questions:\n\n"
        + AKSHAY_PROFILE
    )
    st.session_state.chat_session = chat
    st.session_state.messages = []
    st.sidebar.success("✅ Profile loaded into the AI agent!")

# === 5. Ensure Chat Session is Initialized ===
if "chat_session" not in st.session_state:
    model = genai.GenerativeModel("gemini-2.0-flash")
    st.session_state.chat_session = model.start_chat()
    st.session_state.chat_session.send_message(
        "You are an AI agent that knows everything about Akshay Patel. Use the following profile to answer questions:\n\n"
        + AKSHAY_PROFILE
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

# === 6. Show Chat History ===
for role, message in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(message)

# === 7. Input Section ===
prompt = st.chat_input("Ask anything about Akshay Patel...")

if prompt:
    st.session_state.messages.append(("user", prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat_session.send_message(prompt)
            st.markdown(response.text)

    st.session_state.messages.append(("assistant", response.text))
