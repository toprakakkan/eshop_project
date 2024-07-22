from flask import Blueprint, render_template, send_from_directory, current_app
from project.config import Config
import mysql.connector


main = Blueprint('main', __name__)

db_config = {
    'user': Config.DB_USER,
    'password': Config.DB_PASS,
    'host': Config.DB_HOST,
    'database': Config.DB_NAME
}

@main.route("/")
@main.route("/home")
def home():
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT p.product_name, pp.product_picture_url
        FROM product p
        LEFT JOIN product_picture pp ON p.product_id = pp.product_id
        WHERE p.product_coverPictureUrl IN (1, 2, 3)
    """)
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template('home.html', title='Home', products=products)
    
@main.route('/static/<path:filename>')
def custom_static(filename):
    return send_from_directory(current_app.root_path + '/static/', filename)

