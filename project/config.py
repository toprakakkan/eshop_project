import os

class Config:
    SECRET_KEY= os.environ.get('SECRET_KEY')
    DB_USER = os.environ.get('DB_USER')
    DB_PASS = os.environ.get('DB_PASS')
    DB_HOST = os.environ.get('DB_HOST')
    DB_NAME = os.environ.get('DB_NAME')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')