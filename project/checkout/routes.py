from flask import Blueprint, request, session, flash, redirect, url_for, render_template, jsonify
import mysql.connector
from project.config import Config
from project.checkout.forms import CheckoutForm
from flask_jwt_extended import jwt_required

checkout = Blueprint('checkout', __name__)

db_config = {
    'user': Config.DB_USER,
    'password': Config.DB_PASS,
    'host': Config.DB_HOST,
    'database': Config.DB_NAME
}

@checkout.route('/checkout', methods=['GET', 'POST'])
def go_checkout():
    form = CheckoutForm()
    cart_items = []
    total_price = 0
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    for product_id, quantity in session.get('cart', {}).items():
        cursor.execute("SELECT * FROM product WHERE product_id = %s", (product_id,))
        product = cursor.fetchone()
        if product:
            product['quantity'] = quantity
            product['total_price'] = product['product_price'] * quantity
            cart_items.append(product)
            total_price += product['total_price']

    cursor.close()
    conn.close()

    if form.validate_on_submit():
        flash('Your order has been placed successfully!', 'success')
        session.pop('cart', None)
        return redirect(url_for('product.display_shop'))

    return render_template('checkout.html', is_checkout=True, form=form, cart_items=cart_items, total_price=total_price)


@checkout.route('/process_checkout', methods=['POST'])
def process_checkout():
    form = CheckoutForm()
    if form.validate_on_submit():
        flash('Your order has been placed successfully!', 'success')
        session.pop('cart', None)
        return redirect(url_for('home'))

   