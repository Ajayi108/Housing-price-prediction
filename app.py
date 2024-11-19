import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model


st.title("American hausing Data Analysis")

#Load the dataset
data = pd.read_csv('American_Housing_Data.csv')
file_path = "American_Housing_Data.csv"
data = pd.read_csv(file_path)

# Display the dataset
st.subheader("Dataset Overview")
st.write(data.head())

# Basic statistics
st.subheader("Basic Statistics")
st.write(data.describe())