import streamlit as st

# Path to your text file
file_path = "FAke_Data_Training_output_results.txt"

# Read the contents of the text file
try:
    with open(file_path, "r") as file:
        content = file.read()
except FileNotFoundError:
    content = "File not found. Please check the file path. Or run Train_models.py"

st.title("Model Trainning performance")
st.subheader("The followning models are use and these are their perfomance:")

# You can use st.text or st.code based on preference
st.text(content)  # Display as plain text
# st.code(content, language="plaintext")  # Display with formatting