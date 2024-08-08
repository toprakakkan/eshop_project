from flask import Blueprint, request, session, render_template, jsonify
from project.models.cart_models import CartModel  
cart = Blueprint('cart', __name__)

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
    
    for product_id, quantity in session.get('cart', {}).items():
        product = CartModel.get_product_details(product_id)
        if product:
            product['quantity'] = quantity
            product['total_price'] = product['product_price'] * quantity
            cart_items.append(product)
            total_price += product['total_price']

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
    
    for product_id, quantity in session.get('cart', {}).items():
        product = CartModel.get_product_details(product_id)
        if product:
            product['quantity'] = quantity
            product['total_price'] = product['product_price'] * quantity
            cart_items.append(product)
            total_price += product['total_price']

    return render_template('features.html', cart_items=cart_items, total_price=total_price, is_features=True)
