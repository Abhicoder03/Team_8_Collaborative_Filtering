from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split
import pandas as pd
import ast 
from flask import Flask, render_template, request, jsonify
# Load images and ASIN IDs
images_df = pd.read_csv('/Users/shyam/Downloads/review/unique_asin_image.csv').head(100)
# Assuming your DataFrame is named merged_df and it's already filtered to include only 'reviewerID', 'asin', 'rating' columns
merged_df=pd.read_csv("/Users/shyam/Downloads/review/merged.csv")
# Define a Reader object. The rating_scale parameter is tuple of the minimum and maximum rating.
merged_df=merged_df.head(200000)
reader = Reader(rating_scale=(1, 5))

# Load the dataset from from flask import Flask, request, render_template
from surprise import Dataset, Reader, KNNBasic, SVD
import pandas as pd

app = Flask(__name__, template_folder='/Users/shyam/Downloads/review/templates')




# Assuming merged_df is your DataFrame and it's loaded here
# For demonstration, replace this with loading your actual DataFrame


data = Dataset.load_from_df(merged_df[['reviewerID', 'asin', 'rating']], reader)
trainset = data.build_full_trainset()

# KNN Model
knn_model = KNNBasic(sim_options={'name': 'cosine', 'user_based': False})
knn_model.fit(trainset)

# SVD Model
svd_model = SVD()
svd_model.fit(trainset)


# Apply the parsing function to the 'image' column


# Convert the DataFrame to a dictionary for easy lookup
def parse_image_url(url_list_str):
    try:
        # Safely evaluate the string to a list
        urls = ast.literal_eval(url_list_str)
        # Return the first URL in the list, or None if the list is empty
        return urls[0] if urls else None
    except (ValueError, SyntaxError):
        # Return None or a default URL if there's an error in parsing
        return None

# Apply the parsing function to the 'image' column
images_df['image'] = images_df['image'].apply(parse_image_url)

# Convert the DataFrame to a dictionary for easy lookup
asin_to_image_url = pd.Series(images_df.image.values, index=images_df.asin).to_dict()
@app.route('/')
def index():
    # Convert the DataFrame to a list of dictionaries for easier handling in the template
    images_list = images_df.to_dict(orient='records')
    return render_template('index.html', images_list=images_list)



asin_to_image_url = pd.Series(images_df.image.values, index=images_df.asin).to_dict()

@app.route('/recommend', methods=['POST'])
def recommend():
    user_id = request.form.get('user_id')
    product_id = request.form.get('product_id')
    k = int(request.form.get('k', 10))
    
    # KNN Recommendations (Similar Products)
    inner_id = knn_model.trainset.to_inner_iid(product_id)
    neighbors = knn_model.get_neighbors(inner_id, k=k)
    similar_products_asin = [knn_model.trainset.to_raw_iid(inner_id) for inner_id in neighbors]
    
    # Map ASINs to image URLs for similar products
    similar_products = [{'asin': asin, 'image': asin_to_image_url.get(asin, 'default_image_url')} for asin in similar_products_asin]
    
    # SVD Recommendations (Products for User)
    all_products = trainset.all_items()
    all_products_asin = [trainset.to_raw_iid(x) for x in all_products]
    predictions = [svd_model.predict(user_id, iid) for iid in all_products_asin]
    predictions.sort(key=lambda x: x.est, reverse=True)
    recommended_products_asin = [pred.iid for pred in predictions[:k]]
    
    # Map ASINs to image URLs for recommended products
    recommended_products = [{'asin': asin, 'image': asin_to_image_url.get(asin, 'default_image_url')} for asin in recommended_products_asin]
    
    return render_template('recommendations.html', similar_products=similar_products, recommended_products=recommended_products)
if __name__ == '__main__':
    app.run(debug=True)