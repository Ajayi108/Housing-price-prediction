import seaborn as sns
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
@st.cache_data
def load_data():
    data = pd.read_csv("American_Housing_Data.csv")
    return data

data = load_data()
numerical_data = data.select_dtypes(include=["float", "int"]).fillna(0)

st.title("Correlation Pairplot")
st.write("Pairwise scatterplots and histograms of numerical features.")

# Pairplot for numerical features
sns.pairplot(numerical_data)
st.pyplot(plt)
