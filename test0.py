
from flask import Flask, request,send_from_directory
from flask.templating import render_template
import test7 as t
#import test1 as t1
#import os
#import mysql.connector
import pandas as pd
from IPython.display import HTML

app = Flask(__name__,template_folder='template',static_folder='static')

@app.route('/images/<path:filename>')
def serve_image(filename):
    # Serve images from the 'images' folder in the 'static' directory
    return send_from_directory('static/images', filename)

def get_recommendations(product_name):
    res = t.rec_lin(product_name)
    return res

@app.route('/')
def view_form():
    return render_template('input.html')


@app.route('/recommendations',methods=['GET'])
def recommendations():
    # Get product name from query parameters
    ds=pd.read_csv("products (1).csv", names=['id', 'name', 'brand', 'price', 'quantity', 'image', 'rating'])
    product_name = request.args['product_name']
    indices = pd.Series(ds.index, index=ds["name"])
    idx = indices[product_name]
    image_idx = ds['image'].iloc[idx]
    price="Rs"+str(ds['price'].iloc[idx])
    #product_name = "Adidas Originals Green T-shirt"
    #product_name = input('Enter product name: ')
    print(product_name)
    if product_name is None:
        print("Product Name is Required")

        # Get recommendations for the user
    user_recommendations = get_recommendations(product_name)
    df=pd.DataFrame(user_recommendations)
    df = df.drop(df[df['name'] == 'name'].index)
    print(user_recommendations)
    #t1.convert_to_data(user_recommendations)
    name_list=df['name'].tolist()
    image_list=df['image'].tolist()
    for index, row in df.iterrows():
        row['price']= "Rs"+str(row['price'])
    price_list=df['price'].to_list()
    #zip_list=zip(name_list,image_list,price_list)


    return render_template('login.html',name_list=name_list,image_list=image_list,price_list=price_list,length=len(name_list),product_name=product_name,image_idx=image_idx,price=price)


if __name__ == '__main__':
    app.run(debug=True)