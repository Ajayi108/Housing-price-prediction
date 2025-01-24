import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# Load data
@st.cache_data
def load_data():
    data = pd.read_csv("American_Housing_Data_Augmented.csv")
    return data

data = load_data()

# Separate numerical and categorical data
numerical_data = data.select_dtypes(include=["float", "int"])
categorical_data = data.select_dtypes(include=["object", "category"])

# Handle missing values
numerical_data = numerical_data.fillna(numerical_data.mean())
categorical_data = categorical_data.fillna("Missing")

# Encode categorical variables
label_encoders = {}
encoded_categorical = pd.DataFrame()

for col in categorical_data.columns:
    le = LabelEncoder()
    encoded_categorical[col] = le.fit_transform(categorical_data[col])
    label_encoders[col] = le

# Combine numerical and encoded categorical data
full_data = pd.concat([numerical_data, encoded_categorical], axis=1)

# Generate the correlation matrix
correlation_matrix = full_data.corr()

# Correlation heatmap
st.title("Correlation Heatmap of fake data")
st.write("Visualizing the correlations between features including categorical variables.")

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
st.pyplot(plt)

# Correlation with target variable
target_variable = "Price"
if target_variable in full_data.columns:
    correlations = correlation_matrix[target_variable].sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    correlations.plot(kind="bar", color="skyblue")
    plt.title(f"Correlation with {target_variable}")
    plt.ylabel("Correlation Coefficient")
    plt.xlabel("Features")
    st.pyplot(plt)
else:
    st.write(f"The target variable '{target_variable}' is not in the dataset.")
