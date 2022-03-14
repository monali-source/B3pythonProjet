from flask import Flask
from flask_restful import Resource, Api, reqparse
from matplotlib.pyplot import get
import pandas as pd
import mysql.connector
import ast

from soupsieve import select
app = Flask(__name__)
api = Api(app)
import pymysql
import requests

# Open database connection
db = pymysql.connect(host="localhost",user="root",password="",database="python" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to CREATE a record into the database.
sql = """CREATE TABLE book (titre  CHAR(20) NOT NULL,prix FLOAT )"""

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO book (titre, prix)
 VALUES ('hello', 20)"""

sql = """SELECT * FROM book.book"""

try:
   # Execute the SQL command
   cursor.execute(sql)

   result = cursor.fetchall()
   for i in result:
    print(i)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
   db.close()






class Users(Resource):

   def get(self):
      data = pd.read_csv('result.csv')
      data = data.to_dict()
      return {'get': str(id)}

   def put(self, id):
      self.data.insert(id)
      return{'put' : str(id)}

   def delete(self, id):
     self.data.drop(id)

     return{}

   def poste(self, id):
      return{}
   

    
api.add_resource(Users, '/<id>') 


if __name__ == '__main__':
    app.run(debug=True)