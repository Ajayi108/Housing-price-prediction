import pandas as pd
import numpy as np

# Load the original dataset
data = pd.read_csv('American_Housing_Data.csv')  # Adjust path if needed

# Set random seed for reproducibility
np.random.seed(42)

# Columns to retain
columns_to_keep = ['Price', 'Beds', 'Baths', 'Living Space', 'City', 'Median Household Income', 'Zip Code Density']

# Filter original dataset to keep only the necessary columns
data = data[columns_to_keep]

# Get unique cities from the dataset
unique_cities = data['City'].unique()

# Calculate the number of fake rows (50% of the original data size)
num_fake_rows = len(data) // 2

# Generate fake data
fake_data = {
    "Price": np.random.uniform(100000, 2000000, num_fake_rows),
    "Beds": np.random.randint(1, 7, num_fake_rows),
    "Baths": np.random.randint(1, 5, num_fake_rows),
    "Living Space": np.random.randint(500, 5000, num_fake_rows),
    "City": np.random.choice(unique_cities, num_fake_rows),
    "Median Household Income": np.random.uniform(30000, 150000, num_fake_rows),
    "Zip Code Density": np.random.uniform(500, 5000, num_fake_rows),
}

# Create a DataFrame for the fake data
fake_data_df = pd.DataFrame(fake_data)

# Append the fake data to the original dataset
augmented_data = pd.concat([data, fake_data_df], ignore_index=True)

# Save the augmented dataset to a new CSV file
augmented_data.to_csv('American_Housing_Data_Augmented.csv', index=False)

print("Fake data added, unnecessary columns dropped, and saved as 'American_Housing_Data_Augmented.csv'")
