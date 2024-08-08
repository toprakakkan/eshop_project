import os
import mysql.connector


class Config:
    SECRET_KEY= os.environ.get('SECRET_KEY')
    DB_USER = os.environ.get('DB_USER')
    DB_PASS = os.environ.get('DB_PASS')
    DB_HOST = os.environ.get('DB_HOST')
    DB_NAME = os.environ.get('DB_NAME')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    # JWT_TOKEN_LOCATION = ['cookies', 'query_string']
   

def db_connection():

   db_config = {
        'user': Config.DB_USER,
        'password': Config.DB_PASS,
        'host': Config.DB_HOST,
        'database': Config.DB_NAME
    }

   conn = mysql.connector.connect(**db_config)
   cursor = conn.cursor(dictionary=True)
   return conn, cursor