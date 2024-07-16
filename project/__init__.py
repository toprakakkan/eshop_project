import os
from flask import Flask
from project.config import Config
from flask_login import LoginManager
from flask_jwt_extended import JWTManager



login_manager = LoginManager()
login_manager.login_view = 'users.login'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    login_manager.init_app(app)
    jwt = JWTManager(app)
    
    
    
    
    from project.main.routes import main
    from project.product.routes import product
    from project.users.routes import users
    from project.cart.routes import cart
    from project.checkout.routes import checkout
    from project.about.routes import about
    from project.shop.routes import shop
    from project.blog.routes import blog

    
    app.register_blueprint(main)
    app.register_blueprint(product)
    app.register_blueprint(users)
    app.register_blueprint(cart)
    app.register_blueprint(checkout)
    app.register_blueprint(about)
    app.register_blueprint(shop)
    app.register_blueprint(blog)
    
    
   
    
   
    return app
    
    