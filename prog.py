import pandas as pd
import numpy as np

# Load your existing dataset
existing_df = pd.read_csv('C:/Users/dev/OneDrive/Documents/Python-Project/larger_dataset1.csv')

# Define the factor by which you want to increase the dataset size
augmentation_factor = 20  # You can adjust this as needed

# Calculate the number of rows to sample from the existing dataset
num_samples = len(existing_df) * augmentation_factor

# Randomly sample rows from the existing dataset
augmented_df = existing_df.sample(n=num_samples, replace=True)

# Reset the index of the new DataFrame
augmented_df.reset_index(drop=True, inplace=True)

# Save the augmented dataset to a new CSV file
augmented_df.to_csv('C:/Users/dev/OneDrive/Documents/Python-Project/larger_dataset2.csv', index=False)

print("Dataset generation completed.")
