import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load the preprocessed dataset
data = pd.read_csv('Transformed_American_Housing_Data.csv')

# Separate features and target variable
X = data.drop(columns=['Price'])
y = data['Price']

# Shuffle and split the data into training, validation, and test sets
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Initialize the models
linear_model = LinearRegression()
random_forest_model = RandomForestRegressor(random_state=42)

# Train the models
linear_model.fit(X_train, y_train)
random_forest_model.fit(X_train, y_train)

# Evaluate on the validation set
linear_val_predictions = linear_model.predict(X_val)
rf_val_predictions = random_forest_model.predict(X_val)

linear_val_mse = mean_squared_error(y_val, linear_val_predictions)
rf_val_mse = mean_squared_error(y_val, rf_val_predictions)

#print 
print(f"Validation MSE for Linear Regression: {linear_val_mse}")
print(f"Validation MSE for Random Forest: {rf_val_mse}")

# Test set evaluation
linear_test_predictions = linear_model.predict(X_test)
rf_test_predictions = random_forest_model.predict(X_test)

linear_test_mse = mean_squared_error(y_test, linear_test_predictions)
rf_test_mse = mean_squared_error(y_test, rf_test_predictions)

print(f"Test MSE for Linear Regression: {linear_test_mse}")
print(f"Test MSE for Random Forest: {rf_test_mse}")

# Save test predictions for comparison
test_results = pd.DataFrame({
    'Actual': y_test,
    'Linear Regression Predictions': linear_test_predictions,
    'Random Forest Predictions': rf_test_predictions
})

test_results.to_csv('Test_Results_Comparison.csv', index=False)
print("Test predictions saved to 'Test_Results_Comparison.csv'")
