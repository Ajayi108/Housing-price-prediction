import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def preprocess_housing_data(input_file, output_file):
    # Load the dataset
    housing_data = pd.read_csv(input_file)
    
    
    #Drop irrelevant columns ('Address')
    housing_data = housing_data.drop(columns=['Address'])
    
    #Encode categorical data
    categorical_cols = ['City', 'State', 'County']
    encoder = OneHotEncoder(sparse_output=False, drop='first')  # Fixed argument
    encoded_data = pd.DataFrame(encoder.fit_transform(housing_data[categorical_cols]),
                                columns=encoder.get_feature_names_out(categorical_cols))
    
    # Drop original categorical columns and add encoded ones
    housing_data = housing_data.drop(columns=categorical_cols).reset_index(drop=True)
    housing_data = pd.concat([housing_data, encoded_data], axis=1)
    
    #Normalize numerical features
    numerical_cols = ['Price', 'Beds', 'Baths', 'Living Space', 'Zip Code Population',
                      'Zip Code Density', 'Median Household Income', 'Latitude', 'Longitude']
    scaler = StandardScaler()
    housing_data[numerical_cols] = scaler.fit_transform(housing_data[numerical_cols])
    
    # Save the processed data
    housing_data.to_csv(output_file, index=False)
    print(f"Data preprocessed and saved to {output_file}")

if __name__ == "__main__":
    input_file = 'American_Housing_Data.csv'
    output_file = 'Transformed_American_Housing_Data.csv'
    preprocess_housing_data(input_file, output_file)
