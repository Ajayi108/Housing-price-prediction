import streamlit as st
import pandas as pd

st.title("Summary Statistics")
st.write("Descriptive statistics of the dataset.")

# Load data
@st.cache_data
def load_data():
    data = pd.read_csv("American_Housing_Data.csv")
    return data

data = load_data()
st.write(data.describe())


