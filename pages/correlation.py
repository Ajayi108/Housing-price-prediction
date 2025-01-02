import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
@st.cache_data
def load_data():
    data = pd.read_csv("American_Housing_Data.csv")
    return data

data = load_data()

# Filter numerical columns
numerical_data = data.select_dtypes(include=["float", "int"])

# Handle missing values (e.g., fill with mean or drop rows with NaN)
numerical_data = numerical_data.fillna(numerical_data.mean())

st.title("Correlation Heatmap")
st.write("Visualizing the correlations between numerical features.")

# Generate the correlation matrix and plot
plt.figure(figsize=(10, 6))
correlation_matrix = numerical_data.corr()
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
st.pyplot(plt)
