import pandas as pd
G1=pd.read_csv("/Users/shyam/Downloads/review/Grocery_and_Gourmet_Food_5.csv")
columns_to_drop = ['verified', 'reviewTime', 'unixReviewTime','image']  
G1.drop(columns=columns_to_drop, inplace=True)
G2=pd.read_csv("/Users/shyam/Downloads/review/Grocery_and_Gourmet_Food.csv")
columns_to_drop = ['unixReviewTime']  
G2.drop(columns=columns_to_drop, inplace=True)
merged_df = pd.merge(G1, G2, on=['asin','reviewerID'], how='outer')
merged_df.to_csv('merged.csv', index=False)