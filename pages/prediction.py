import streamlit as st
import pandas as pd
import joblib

# Load the trained models
lr_model = joblib.load('linear_regression_model.pkl')
rf_model = joblib.load('random_forest_model.pkl')

# Load the dataset from the root directory
data = pd.read_csv('American_Housing_Data.csv')

# Drop columns with low correlation
columns_to_drop = ['Latitude', 'Longitude', 'Zip Code', 'Zip Code Population', 'Address', 'County', 'State']
data = data.drop(columns=columns_to_drop, errors='ignore')

# Define features
target = 'Price'  # Target column
features = [col for col in data.columns if col != target]

categorical_features = ['City']
numerical_features = [col for col in features if col not in categorical_features]

# Get unique cities from the dataset
unique_cities = data['City'].unique()

# Streamlit app
st.title("Housing Price Prediction App")
st.write("Predict housing prices using Linear Regression and Random Forest models.")

# Show a preview of the dataset
if st.checkbox("Show Dataset Preview"):
    st.write("Dataset Preview:")
    st.write(data.head())

# Input features form
st.sidebar.header("Input Features")

# Dynamically create input fields for remaining features
user_inputs = {}
st.sidebar.write("Enter the feature values below:")

# Dropdown for City selection
user_inputs['City'] = st.sidebar.selectbox("Select City", options=unique_cities)

# Input fields for numerical features
for feature in numerical_features:
    user_inputs[feature] = st.sidebar.number_input(f"Enter {feature}", value=0.0)

# Create DataFrame for user input
input_data = pd.DataFrame([user_inputs])

# Predict button
if st.sidebar.button("Predict"):
    # Predict using both models
    lr_prediction = lr_model.predict(input_data)
    rf_prediction = rf_model.predict(input_data)

    # Display predictions
    st.write("Predictions for the entered data:")
    st.write(f"Linear Regression Prediction: ${lr_prediction[0]:,.2f}")
    st.write(f"Random Forest Prediction: ${rf_prediction[0]:,.2f}")
