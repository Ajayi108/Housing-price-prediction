import streamlit as st
import requests

st.title("Rasa Chatbot")

# Chat interface
st.sidebar.header("Chat with our bot!")
user_input = st.sidebar.text_input("You:", placeholder="Type your message here...")

# Rasa REST API endpoint
RASA_SERVER_URL = "http://localhost:5005/webhooks/rest/webhook"

if user_input:
    # Send message to Rasa
    response = requests.post(
        RASA_SERVER_URL,
        json={"sender": "user", "message": user_input},
    )
    
    # Display bot response
    if response.status_code == 200:
        messages = response.json()
        for message in messages:
            st.write(f"Bot: {message.get('text', '')}")
    else:
        st.error("Failed to connect to the chatbot server. Please ensure the Rasa server is running.")
