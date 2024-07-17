from flask import Blueprint, render_template, send_from_directory, current_app, request
import mysql.connector
from project.config import Config
from project.product.routes import get_categories


shop = Blueprint('shop', __name__)

db_config = {
    'user': Config.DB_USER,
    'password': Config.DB_PASS,
    'host': Config.DB_HOST,
    'database': Config.DB_NAME
}

@shop.route('/shop', methods=['GET'])
def display_shop():
    category_id = request.args.get('category_id', default=None, type=int)
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    
    if category_id:
        cursor.execute("""
            SELECT product_id, product_name, product_description, product_price
            FROM product 
            WHERE category_id = %s
        """, (category_id,))
    else:
        cursor.execute("""
            SELECT product_id, product_name, product_description, product_price, product_coverPictureUrl
            FROM product
        """)
    
    products = cursor.fetchall()
    
    cursor.execute("""
        SELECT product_id, product_picture_url, product_picture_url2, product_picture_url3 
        FROM Product_Picture
    """)
    pictures = cursor.fetchall()
    
    picture_dict = {pic['product_id']: [pic['product_picture_url'], pic['product_picture_url2'], pic['product_picture_url3']] for pic in pictures}
    
    for product in products:
        product['pictures'] = picture_dict.get(product['product_id'], ['', '', ''])
    
    cursor.close()
    conn.close()
    
    categories = get_categories()

    
    return render_template('shop.html', products=products, categories=categories, selected_category=category_id)