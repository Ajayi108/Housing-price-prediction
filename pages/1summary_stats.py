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
st.write("Summary of real data")
st.write(data.describe())

@st.cache_data
def load_fake_data():
    fake_data = pd.read_csv("American_Housing_Data_Augmented.csv")
    return fake_data

fake_data = load_fake_data()
st.write("Fake Data Summary Statistics:")
st.write(fake_data.describe())