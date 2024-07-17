from flask_login import UserMixin
import mysql.connector
from project.config import Config
import bcrypt
from flask import request, jsonify
from flask_wtf.csrf import CSRFProtect
from project.__init__ import create_app


db_config = {
    'user': Config.DB_USER,
    'password': Config.DB_PASS,
    'host': Config.DB_HOST or 'localhost',
    'database': Config.DB_NAME
}

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @staticmethod
    def get(user_id):
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
        user_data = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if user_data:
            return User(user_data['user_id'], user_data['user_username'], user_data['user_password'])
        return None

    @staticmethod
    def find_by_username(username):
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user WHERE user_username = %s", (username,))
        user_data = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if user_data:
            return User(user_data['user_id'], user_data['user_username'], user_data['user_password'])
        return None

    @staticmethod
    def hash_password(password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    @staticmethod
    def check_password(hashed_password, password):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
    