import streamlit as st
from streamlit_chat import message
import requests
import pandas as pd

#======================================================================
# Load the city list dynamically from the dataset
@st.cache_data
def load_cities():
    # Path to the dataset
    file_path = "American_Housing_Data.csv"
    data = pd.read_csv(file_path)
    cities = sorted(data['City'].dropna().unique())
    return cities

# Load cities into a variable
available_cities = load_cities()

# Streamlit app configuration
st.title("Rasa Chatbot")
st.write("please Check the Dialogue flow page and then Chat with the bot to get predictions.")
st.write("I am a chatbot that can make predictions of housing prices for the following cities in the USA:")

# Display the list of cities in a collapsible section
with st.expander("View Available Cities"):
    st.write(", ".join(available_cities))

#=000000000000000000000000000000000000000000000000000000000000000000000000000000000

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Rasa server endpoint
rasa_endpoint = "http://localhost:5005/webhooks/rest/webhook"

# Display chat messages

# User input
input_text = st.chat_input("You:", key="input")

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
for idx, msg in enumerate(st.session_state["messages"]):
    message(msg["message"], is_user=msg["is_user"], key=f"message-{idx}")


