import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import sigmoid_kernel



df = pd.read_csv("products (1).csv",names=['id','name','brand','price','quantity','image','rating'])
print(df)
#print(df.shape)
#print(df.info())
#print(df.duplicated())
df.dropna(inplace = True)
#print(df.info())




new = df['brand'].str.split("|", n=3, expand=True)
tfidf=TfidfVectorizer(stop_words='english')
df[""] = df['brand'].fillna("")
tfidf_matrix = tfidf.fit_transform(df['brand'])
#print(tfidf_matrix.shape)
#print(tfidf.get_feature_names_out()[0:20])

    # Create the matrix
linear = linear_kernel(tfidf_matrix, tfidf_matrix)
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
sig_score = sigmoid_kernel(tfidf_matrix, tfidf_matrix)

#print(linear.shape)
#print(cosine_sim.shape)
#print(sig_score.shape)

#print(linear[1])
#print(cosine_sim[1])
#print(sig_score[1])

indices = pd.Series(df.index, index=df["name"])
#print(indices[:20])

#Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'

#Replace NaN with an empty string

#Construct the required TF-IDF matrix by fitting and transforming the data


#Output the shape of tfidf_matrix

def rec_lin(product_name, linear=linear):
    # Get the index of the product that matches the product name
    idx = indices[product_name]
    # Get the pairwise similarity scores
    # Enumerate adds a counter to the iterable and lets it be converted into a list of tuples
    sim_scores = list(enumerate(linear[idx]))

    # Sort the products based on the similarity scores
    # Reverse gives us the similarity scores in descending order
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar products
    sim_scores = sim_scores[1:11]

    # Get the product indices
    product_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar products
    # iloc allows us to retrieve rows from a data frame
    return df[["name","price","image"]].iloc[product_indices]

#recommend=input("Enter the name of the product you want recommendation on: ")
#recommend=recommend.strip()
#print("The recommended product of the above product by category: ")
#result = rec_lin(recommend)
#print(result)


