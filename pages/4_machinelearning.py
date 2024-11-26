import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Function to train models and return performance
def train_models(data):
    features = ['Beds', 'Baths', 'Living Space', 'Median Household Income']
    target = 'Price'
    
    # Drop rows with missing values
    data_cleaned = data.dropna(subset=features + [target])
    
    X = data_cleaned[features]
    y = data_cleaned[target]
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Train Linear Regression
    linear_model = LinearRegression()
    linear_model.fit(X_train, y_train)
    y_pred_linear = linear_model.predict(X_test)
    mse_linear = mean_squared_error(y_test, y_pred_linear)
    r2_linear = r2_score(y_test, y_pred_linear)
    
    # Train Decision Tree
    tree_model = DecisionTreeRegressor(random_state=42)
    tree_model.fit(X_train, y_train)
    y_pred_tree = tree_model.predict(X_test)
    mse_tree = mean_squared_error(y_test, y_pred_tree)
    r2_tree = r2_score(y_test, y_pred_tree)
    
    return {
        "Linear Regression": {"MSE": mse_linear, "R2": r2_linear},
        "Decision Tree": {"MSE": mse_tree, "R2": r2_tree}
    }

# Streamlit Application
st.title("Housing Price Prediction Model Comparison")


# Load data
data = pd.read_csv('American_Housing_Data.csv')
file_path = "American_Housing_Data.csv"
data = pd.read_csv(file_path)
st.write("Data Preview:")
st.dataframe(data.head())
    
# Model Training and Evaluation
st.write("Training Models...")
performance = train_models(data)
    
# Display Results
st.write("Model Performance:")
for model, metrics in performance.items():
    st.subheader(model)
    st.write(f"Mean Squared Error: {metrics['MSE']}")
    st.write(f"R² Score: {metrics['R2']}")
