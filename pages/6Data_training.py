import streamlit as st
import pandas as pd

# Path to your text file
file_path = "output_results.txt"

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

# Load data
data = pd.read_csv('American_Housing_Data.csv')
file_path = "American_Housing_Data.csv"
data = pd.read_csv(file_path)
st.write("Data Preview:")
st.dataframe(data.head())