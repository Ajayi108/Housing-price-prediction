import streamlit as st

st.title("Hello, Streamlit!")
st.write("Welcome to your first Streamlit app.")


import pandas as pd
import numpy as np
from sklearn import linear_model



st.title("Streamlit Interactive App Example")

# Text input
#name = st.text_input("Enter your name:")
#st.write(f"Hello, {name}!")

# Slider input
#age = st.slider("Select your age:", 0, 100)
#st.write(f"You are {age} years old.")


#=====================================================
# Load data
data = pd.read_csv('fake_sales_data.csv')

# Display the data
st.write("Data Preview:", data)


# Display summary statistics
st.write("Data Summary:")
st.write(data.describe())

# Plot data
st.subheader("Simple Line Plot of First Column")
st.line_chart(data[data.columns[0]]
              
              )
#00000000000000000000000000000
X = data.iloc[:,7:8]
X= X.values


Y = data.iloc[:,2]
Y= Y.values

reg = linear_model.LinearRegression()
reg.fit(X , Y)
print(reg.coef_)
