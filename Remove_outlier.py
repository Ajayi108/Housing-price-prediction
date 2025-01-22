import pandas as pd 
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'American_Housing_Data_20231209.csv'  # Update if the dataset is in a different location
data = pd.read_csv(file_path)

# Function to remove outliers using IQR and visualize with box plot
def remove_outliers_with_boxplot(df, column):
    # Create a box plot to visualize the column
    plt.figure(figsize=(8, 6))
    plt.boxplot(df[column], vert=False)
    plt.title(f"Box Plot of {column}")
    plt.xlabel(column)
    plt.show()
    
    # Calculate IQR
    Q1 = df[column].quantile(0.25)  # First quartile
    Q3 = df[column].quantile(0.75)  # Third quartile
    IQR = Q3 - Q1  # Interquartile range
    lower_bound = Q1 - 1.5 * IQR  # Lower boundary
    upper_bound = Q3 + 1.5 * IQR  # Upper boundary
    
    # Print the boundaries
    print(f"{column}: Lower Bound = {lower_bound}, Upper Bound = {upper_bound}")
    
    # Filter out outliers
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

# List of numeric columns to process
numeric_columns = ['Price', 'Beds', 'Baths', 'Living Space', 'Zip Code Population', 
                   'Zip Code Density', 'Median Household Income', 'Latitude', 'Longitude']

# Iteratively remove outliers and plot box plots
data_no_outliers = data.copy()  # Create a copy of the data
for column in numeric_columns:
    print(f"Processing column: {column}")
    data_no_outliers = remove_outliers_with_boxplot(data_no_outliers, column)

# Save the cleaned dataset
cleaned_file_path = 'American_Housing_Data_No_Outliers_BoxPlot.csv'
data_no_outliers.to_csv(cleaned_file_path, index=False)

print(f"Outliers removed using box plot method. Cleaned data saved to: {cleaned_file_path}")