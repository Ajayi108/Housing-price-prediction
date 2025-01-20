import streamlit as st
import requests
from streamlit_chat import message  # Install with: pip install streamlit-chat

# Initialize session state for chat messages
if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "user_message" not in st.session_state:
    st.session_state["user_message"] = ""  # Separate from the widget key

# Rasa REST API endpoint
RASA_SERVER_URL = "http://localhost:5005/webhooks/rest/webhook"

st.title("House Price Prediction Chatbot")

# Function to send a message to Rasa and get a response
def send_message(user_message):
    response = requests.post(
        RASA_SERVER_URL,
        json={"sender": "user", "message": user_message},
    )
    if response.status_code == 200:
        return response.json()
    else:
        return [{"text": "Sorry, I couldn't connect to the chatbot server."}]

# Display chat messages
for i, msg in enumerate(st.session_state["messages"]):
    if msg["is_user"]:
        message(msg["message"], is_user=True, avatar_style="adventurer", key=f"user_{i}")  # User messages on the right
    else:
        message(msg["message"], is_user=False, avatar_style="bottts", key=f"bot_{i}")  # Bot messages on the left

# Add space at the bottom to keep the input box at the bottom
st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

# Chat input at the bottom
user_input = st.text_input(
    "Your Message:", 
    placeholder="Type your message here...", 
    value=st.session_state["user_message"],  # Use the separate session state variable
    key="chat_input"
)

# When the user presses the Send button
if st.button("Send"):
    if user_input:
        # Add user message to chat history
        st.session_state["messages"].append({"is_user": True, "message": user_input})
        
        # Get bot response
        bot_response = send_message(user_input)
        
        # Add bot message to chat history
        for msg in bot_response:
            st.session_state["messages"].append({"is_user": False, "message": msg.get("text", "")})
        
        # Clear the session state variable
        st.session_state["user_message"] = ""
