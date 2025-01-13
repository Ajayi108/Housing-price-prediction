# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error, r2_score
import joblib

# Load the dataset (ensure CSV is in the same directory as this script)
data = pd.read_csv('American_Housing_Data.csv')

# Drop columns with low correlation
columns_to_drop = ['Latitude', 'Longitude', 'Zip Code', 'Zip Code Population', 'Address', 'County', 'State']
data = data.drop(columns=columns_to_drop, errors='ignore')

# Data preprocessing
data = data.dropna()  # Handle missing values (customize as needed)

# Define features and target variable
target = 'Price'  # Target column
features = [col for col in data.columns if col != target]

X = data[features]
y = data[target]

# Identify categorical and numerical features
categorical_features = ['City']  # Only 'City' remains as a categorical feature
numerical_features = [col for col in features if col not in categorical_features]

# Define a column transformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ]
)

# Linear Regression Pipeline
lr_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', LinearRegression())
])

# Random Forest Pipeline
rf_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', RandomForestRegressor(random_state=42))
])

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression Model
lr_pipeline.fit(X_train, y_train)

# Train Random Forest Model
rf_pipeline.fit(X_train, y_train)

# Evaluate Models
lr_rmse = root_mean_squared_error(y_test, lr_pipeline.predict(X_test))
rf_rmse = root_mean_squared_error(y_test, rf_pipeline.predict(X_test))

print("Linear Regression Performance:")
print(f"RMSE: {lr_rmse}")
print(f"R²: {r2_score(y_test, lr_pipeline.predict(X_test))}")

print("\nRandom Forest Performance:")
print(f"RMSE: {rf_rmse}")
print(f"R²: {r2_score(y_test, rf_pipeline.predict(X_test))}")

# Save the models
joblib.dump(lr_pipeline, 'linear_regression_model.pkl')
joblib.dump(rf_pipeline, 'random_forest_model.pkl')

print("Models saved as 'linear_regression_model.pkl' and 'random_forest_model.pkl'")
