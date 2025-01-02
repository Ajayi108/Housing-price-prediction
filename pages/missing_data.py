import streamlit as st
import pandas as pd

st.title("Missing Data Overview")
st.write("Visualizing missing data in the dataset.")

# Load data
@st.cache
def load_data():
    data = pd.read_csv("American_Housing_Data.csv")
    return data

data = load_data()
missing = data.isnull().sum()
missing = missing[missing > 0]
if not missing.empty:
    st.bar_chart(missing)
else:
    st.write("No missing data found.")
