from flask import Blueprint, session, flash, redirect, url_for, render_template
from project.checkout.forms import CheckoutForm
from project.models.checkout_model import CheckoutModel  


checkout = Blueprint('checkout', __name__)

@checkout.route('/checkout', methods=['GET', 'POST'])
def go_checkout():
    form = CheckoutForm()
    cart = session.get('cart', {})
    cart_items, total_price = CheckoutModel.get_cart_items(cart)

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
