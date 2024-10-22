from flask import render_template, request, Blueprint, redirect, url_for, flash, jsonify
from flask_login import login_required
from project.users.decorators import admin_required
from project.product.forms import AddProducts
from project.models.product_models import ProductModel  # Import the ProductModel class

product = Blueprint('product', __name__)

@product.route('/addproduct', methods=['POST', 'GET'])
@login_required
@admin_required
def add_product():
    categories = ProductModel.get_categories()
    category_choices = [(category['category_id'], category['category_name']) for category in categories]
    
    form = AddProducts(request.form)
    form.category_id.choices = category_choices
    
    if request.method == 'POST' and form.validate():
        image_urls = [form.image_url.data, form.image_url2.data, form.image_url3.data]
        ProductModel.add_product(
            form.category_id.data,
            form.name.data,
            form.price.data,
            form.description.data,
            image_urls
        )
        
        flash('Product added successfully!', 'success')
        return redirect(url_for('product.add_product'))
    else:
        if request.method == 'POST':
            flash('Failed to add product. Please correct the errors and try again.', 'danger')

    return render_template('addproduct.html', title='Add Product Page', form=form)

@product.route('/product/<int:product_id>', methods=['GET'])
def product_detail(product_id):
    product = ProductModel.get_product_detail(product_id)
    
    if product:
        return jsonify(product)
    else:
        return jsonify({'error': 'Product not found'}), 404
