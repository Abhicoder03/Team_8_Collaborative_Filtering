import pandas as pd

# Load the CSV file
df = pd.read_csv('Grocery_and_Gourmet_Food_5.csv')


# Assuming there's an 'image' column, filter rows where 'image' is not null
filtered_df = df[df['image'].notnull()]

# Drop duplicates based on the 'asin' column, keeping the first occurrence
unique_asin_df = filtered_df.drop_duplicates(subset=['asin'], keep='first')

# Select only the 'asin' and 'image' columns
asin_image_df = unique_asin_df[['asin', 'image']]

# Save to a new CSV file
asin_image_df.to_csv('unique_asin_image.csv', index=False)