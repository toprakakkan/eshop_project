from flask import Blueprint, render_template, request
from project.models.shop_models import ShopModel
from project.models.product_models import ProductModel


shop = Blueprint('shop', __name__)

@shop.route('/shop', methods=['GET'])
def display_shop():
    category_id = request.args.get('category_id', default=None, type=int)
    
    products = ShopModel.get_products(category_id)  
    pictures = ShopModel.get_product_pictures()
    
    picture_dict = {pic['product_id']: [pic['product_picture_url'], pic['product_picture_url2'], pic['product_picture_url3']] for pic in pictures}
    
    for product in products:
        product['pictures'] = picture_dict.get(product['product_id'], ['', '', ''])
    
    categories = ProductModel.get_categories()

    
    return render_template('shop.html', products=products, categories=categories, selected_category=category_id)