# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score  # Corrected import
import joblib

# Load the dataset (ensure CSV is in the same directory as this script)
data = pd.read_csv('American_Housing_Data_Augmented.csv')

# Drop columns with low correlation
columns_to_drop = ['Latitude', 'Longitude', 'Zip Code', 'Zip Code Population', 'Address', 'County', 'State']
data = data.drop(columns=columns_to_drop, errors='ignore')

# Data preprocessing
data = data.dropna()  # Handle missing values

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
lr_rmse = mean_squared_error(y_test, lr_pipeline.predict(X_test), squared=False)  # Corrected calculation
rf_rmse = mean_squared_error(y_test, rf_pipeline.predict(X_test), squared=False)  # Corrected calculation

# Collect results in a string
output = []
output.append("Linear Regression Performance:")
output.append(f"RMSE: {lr_rmse}")
output.append(f"R²: {r2_score(y_test, lr_pipeline.predict(X_test))}")

output.append("\nRandom Forest Performance:")
output.append(f"RMSE: {rf_rmse}")
output.append(f"R²: {r2_score(y_test, rf_pipeline.predict(X_test))}")

# Print results to console
for line in output:
    print(line)


print("The models for the fake data training is not saved since it is not used for prediction")

# Write the results to a file
with open('FAke_Data_Training_output_results.txt', 'w') as f:
    f.write('\n'.join(output))
    f.write('\n The models for the fake data training is not saved since it is not used for prediction "\n')
