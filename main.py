from dotenv import load_dotenv
import os
import google.generativeai as genai
import streamlit as st

# Load API Key
load_dotenv(override=True)
API_KEY = os.getenv('API_KEY')

# Configure Gemini Model
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to generate a chatbot response
def generate_response(prompt):
    res = model.generate_content(prompt)
    return res.text

# Streamlit App UI
st.title("TRx ✨")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages (User and Assistant)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
user_input = st.chat_input("Ask me anything...")

if user_input:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate bot response
    response = generate_response(user_input)

    # Store assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Display assistant's response
    with st.chat_message("assistant"):
        st.markdown(response)
