from flask import Blueprint, render_template, send_from_directory, current_app


about = Blueprint('about', __name__)


@about.route("/about")
def about_page():
    
    return render_template('about.html', title='About')