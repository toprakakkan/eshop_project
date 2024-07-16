from flask import Blueprint, request, session, flash, redirect, url_for, render_template, jsonify
import mysql.connector
from project.config import Config

cart = Blueprint('cart', __name__)

db_config = {
    'user': Config.DB_USER,
    'password': Config.DB_PASS,
    'host': Config.DB_HOST,
    'database': Config.DB_NAME
}

@cart.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    product_id = str(data.get('product_id'))
    quantity = int(data.get('quantity', 1))
    
    if 'cart' not in session:
        session['cart'] = {}
    
    if product_id in session['cart']:
        session['cart'][product_id] += quantity
    else:
        session['cart'][product_id] = quantity

    session.modified = True
    return jsonify(success=True)

@cart.route('/cart_items')
def cart_items():
    cart_items = []
    total_price = 0
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    
    for product_id, quantity in session.get('cart', {}).items():
        cursor.execute("""
            SELECT p.product_id, p.product_name, p.product_price, pp.product_picture_url
            FROM product p
            LEFT JOIN product_picture pp ON p.product_id = pp.product_id
            WHERE p.product_id = %s
        """, (product_id,))
        product = cursor.fetchone()
        if product:
            product['quantity'] = quantity
            product['total_price'] = product['product_price'] * quantity
            cart_items.append(product)
            total_price += product['total_price']

    cursor.close()
    conn.close()

    return jsonify(cart_items=cart_items, total_price=total_price)

@cart.route('/update_cart_quantity', methods=['POST'])
def update_cart_quantity():
    data = request.get_json()
    product_id = data.get('product_id')
    change = int(data.get('change'))

    if 'cart' not in session:
        session['cart'] = {}

    if product_id in session['cart']:
        session['cart'][product_id] += change
        if session['cart'][product_id] <= 0:
            del session['cart'][product_id]
    else:
        session['cart'][product_id] = max(1, change)

    session.modified = True
    return jsonify(success=True)


@cart.route('/features')
def cart_features():
    cart_items = []
    total_price = 0
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    
    for product_id, quantity in session.get('cart', {}).items():
        cursor.execute("""
            SELECT p.product_id, p.product_name, p.product_price, pp.product_picture_url
            FROM product p
            LEFT JOIN product_picture pp ON p.product_id = pp.product_id
            WHERE p.product_id = %s
        """, (product_id,))
        product = cursor.fetchone()
        if product:
            product['quantity'] = quantity
            product['total_price'] = product['product_price'] * quantity
            cart_items.append(product)
            total_price += product['total_price']

    cursor.close()
    conn.close()

    return render_template('features.html', cart_items=cart_items, total_price=total_price, is_features=True)

