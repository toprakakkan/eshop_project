from flask_login import UserMixin
from project.config import db_connection
import bcrypt


class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @staticmethod
    def get(user_id):
        conn, cursor = db_connection()
        cursor.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
        user_data = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if user_data:
            return User(user_data['user_id'], user_data['user_username'], user_data['user_password'])
        return None

    @staticmethod
    def find_by_username(username):
        conn, cursor = db_connection()
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
    