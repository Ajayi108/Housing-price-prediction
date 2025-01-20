import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Feature Relationships")
st.write("Explore relationships between two features.")

# Load data
@st.cache
def load_data():
    data = pd.read_csv("American_Housing_Data.csv")
    return data

data = load_data()
x_col = st.selectbox("Select X-axis", data.columns)
y_col = st.selectbox("Select Y-axis", data.columns)
plt.figure(figsize=(8, 5))
sns.scatterplot(x=data[x_col], y=data[y_col])
st.pyplot(plt)
