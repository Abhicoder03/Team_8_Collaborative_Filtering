
# Team_8_Collaborative_Filtering

## Data :-

![ezgif-6-5348e44210](https://github.com/Abhicoder03/Team_8_Collaborative_Filtering/assets/76257252/0ffdb973-a2ac-484f-97b5-e9c4ca2d9f92)
![ezgif-6-f44545cfe4](https://github.com/Abhicoder03/Team_8_Collaborative_Filtering/assets/76257252/c64ea14e-8081-4b4d-9cdc-b088fb07d522)
![ezgif-6-67abbf4038](https://github.com/Abhicoder03/Team_8_Collaborative_Filtering/assets/76257252/36d48ecc-1ea3-4d61-ad9d-0b3ab7f23f4a)
![ezgif-6-d4ba1eee64](https://github.com/Abhicoder03/Team_8_Collaborative_Filtering/assets/76257252/198580a8-07c0-4bf7-aaed-cec65dd54447)


 - The dataset used in this Assignment is the Grocery and Gourmet Food from Amazon Product Reviews,which contains product and user interactions. 
 - The dataset consists of two files, one JSON file with product information and the other with user interaction information.

## Data Fields :-
 - **reviewerID** - ID of the reviewer, e.g. A2SUAM1J3GNN3B
 - **asin** - ID of the product, e.g. 0000013714
 - **reviewerName** - name of the reviewer
 - **vote** - helpful votes of the review
 - **style** - a disctionary of the product metadata, e.g., "Format" is "Hardcover"
 - **reviewTex**t - text of the review
 - **overall** - rating of the product
 - **summary** - summary of the review
 - **unixReviewTime** - time of the review (unix time)
 - **reviewTime** - time of the review (raw)
 - **image** - images that users post after they have received the product
 - ![image](https://github.com/Abhicoder03/Team_8_Collaborative_Filtering/assets/76257252/6bf36256-f191-47bd-9161-816c6e88acc6)




## General Steps:

**Preprocess data**: preprocess the data and filter out irrelevant data, generate user-item rating matrix based on the data

**Choose a collaborative filtering algorithm**: There are two main types of collaborative filtering algorithms: user-based and item-based.

**Train the model**: Use the chosen algorithm to train the model. This will involve identifying similarities between users or items based on the available data.

**Generate recommendations**: Once the model has been trained, it can be used to generate recommendations for users. This could involve using the model to identify similar users or items to the ones that a user has already interacted with, and then recommending items that those similar users or items have also interacted with.

**Evaluate the model**: To determine the accuracy of the model, use metrics such as precision, recall, and F1 score to evaluate its performance. This will help identify areas for improvement and ensure that the model is generating accurate recommendations.


## Files Overview:
 - **EDA & Data Preprocessing.ipynb** : Insights from data and visualization Toy-Data Generation [Quick Recipes]
 - **Matrix Factorization.ipynb** : Collaborative filtering based Recommendation system with Matrix Factorization (Model based - SVD)
 - **MultiRound_Baseline.ipynb** : Multi-Round Recommendation system based on Baseline estimation approach
 - **Latent_Factor_Models.ipynb** : Recommedation system based on Latent Factor Model
 - **Item_Item_Memory_Based.ipynb** : Item Item collborative Recommendation system without Matrix Factorization(Memory Based)
 - **Item_Item_Memory_Based-MRR(BASIC).ipynb** : Item Item collborative Multiround Recommendation system (Memory Based)
 - **Item_Item_Memory_Based-MRR(DYNAMIC).ipynb** : Item Item collborative Multiround Recommendation system (Memory Based)
 - **User_User_Memory_based_Recommendation_System.ipynb** : User User collborative Recommendation system (Memory Based)

Contributors :-

- Vishaka Nair
- Srushti Bhagchandani
- Shyam Saktawat
- Ayush Kumar Sahu
- Abhishek Choudhary

<p align="center">Made with :heart:</p>
 
