import os
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("TRUNCATE TABLE products")
def convert_to_data(user_recomendations):
  result=user_recomendations
  df = pd.DataFrame(result)
  df = df.drop(df[df['name'] == 'name'].index)
  for index, row in df.iterrows():
    sql="INSERT INTO products (name, price,image) VALUES (%s, %s,%s)"
    val = (row['name'], row['price'],row['image'])
    mycursor.execute(sql, val)
    print(mycursor.rowcount, "record inserted.")
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")




