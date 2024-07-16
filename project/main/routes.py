from flask import Blueprint, render_template, send_from_directory, current_app, request


main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    
    return render_template('home.html', title='Home')
    
@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route('/static/<path:filename>')
def custom_static(filename):
    return send_from_directory(current_app.root_path + '/static/', filename)
