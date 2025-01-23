import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Distribution Plots")
st.write("Select a column to visualize its distribution.")

# Load data
@st.cache_data
def load_data():
    data = pd.read_csv("American_Housing_Data.csv")
    return data

data = load_data()
column = st.selectbox("Select a column", data.select_dtypes(include=["float", "int"]).columns)
plt.figure(figsize=(8, 5))
sns.histplot(data[column], kde=True, bins=30)
st.pyplot(plt)
