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


# Replace 'SalePrice' with your target variable's name
target_variable = "Price"
correlations = numerical_data.corr()[target_variable].sort_values(ascending=False)

plt.figure(figsize=(10, 6))
correlations.plot(kind="bar", color="skyblue")
plt.title(f"Correlation with {target_variable}")
plt.ylabel("Correlation Coefficient")
plt.xlabel("Features")
st.pyplot(plt)
