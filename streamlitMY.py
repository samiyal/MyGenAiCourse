import streamlit as st
from google import genai

st.markdown(
    """
    <h1 style='text-align: center;'> Python AI Assistant</h1>
    <p style='text-align: center; font-size:18px;'>
        Ask any Python programming question.
    </p>
    """,
    unsafe_allow_html=True,
)

# Get API key from secrets (SECURE)
try:
    robo = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])
    mychat = robo.chats.create(model="gemini-flash-lite-latest")
except Exception as e:
    st.error(f"Failed to initialize AI: {e}")
    st.stop()

# Placeholder for the response
response_placeholder = st.empty()

# Fixed: Added a label (can be hidden)
question = st.text_input(
    "Your Question", 
    placeholder="Enter your Python question here...",
    label_visibility="collapsed"  # Hides the label visually
)

col1, col2, col3 = st.columns([4, 1, 4])

with col2:
    send = st.button("Send")

if send:
    if question.strip():  # Check if question is not empty
        with st.spinner("Thinking..."):
            try:
                response = mychat.send_message(question)
                response_placeholder.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question.")
