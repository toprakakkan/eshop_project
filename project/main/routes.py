from flask import Blueprint, render_template, send_from_directory, current_app
from project.models.main_models import MainModel


main = Blueprint('main', __name__)



@main.route("/")
@main.route("/home")
def home():
    products = MainModel.get_home_products()
    return render_template('home.html', title='Home', products=products)
    
@main.route('/static/<path:filename>')
def custom_static(filename):
    return send_from_directory(current_app.root_path + '/static/', filename)

