import streamlit as st
from streamlit_chat import message
import requests

# Streamlit app configuration
st.title("Rasa Chatbot")
st.write("Chat with the bot and get predictions.")

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Rasa server endpoint
rasa_endpoint = "http://localhost:5005/webhooks/rest/webhook"

# User input
input_text = st.text_input("You:", key="input")

if input_text:
    # Append user message to the session state
    st.session_state["messages"].append({"message": input_text, "is_user": True})
    
    # Send message to Rasa and get the response
    try:
        response = requests.post(
            rasa_endpoint,
            json={"sender": "user", "message": input_text}
        )
        if response.status_code == 200:
            for bot_response in response.json():
                st.session_state["messages"].append(
                    {"message": bot_response.get("text", ""), "is_user": False}
                )
        else:
            st.session_state["messages"].append(
                {"message": "Error: Unable to connect to Rasa server.", "is_user": False}
            )
    except Exception as e:
        st.session_state["messages"].append(
            {"message": f"Error: {str(e)}", "is_user": False}
        )

# Display chat messages
for idx, msg in enumerate(st.session_state["messages"]):
    message(msg["message"], is_user=msg["is_user"], key=f"message-{idx}")
