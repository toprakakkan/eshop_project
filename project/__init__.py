from flask import Flask, jsonify
from project.config import Config
from flask_login import LoginManager
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, JWTManager
from flask_login import current_user


login_manager = LoginManager()
login_manager.login_view = 'users.login'
jwt = JWTManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    login_manager.init_app(app)
    jwt.init_app(app)
    
    
    from project.main.routes import main
    from project.product.routes import product
    from project.users.routes import users
    from project.cart.routes import cart
    from project.checkout.routes import checkout
    from project.about.routes import about
    from project.shop.routes import shop
    from project.blog.routes import blog
    from project.errors.handlers import errors
    from project.contact.routes import contact
    from project.tickets.routes import tickets
    from project.auth.routes import auth
    from project.models.routes import models
    
    
    app.register_blueprint(main)
    app.register_blueprint(product)
    app.register_blueprint(users)
    app.register_blueprint(cart)
    app.register_blueprint(checkout)
    app.register_blueprint(about)
    app.register_blueprint(shop)
    app.register_blueprint(blog)
    app.register_blueprint(errors)
    app.register_blueprint(contact)
    app.register_blueprint(tickets)
    app.register_blueprint(auth)
    app.register_blueprint(models)
   
    @app.context_processor
    def inject_is_blogger():
        def is_blogger():
            return current_user.is_authenticated and current_user.id in (1, 6)
        def is_admin():
            return current_user.is_authenticated and current_user.id == 1
        return dict(is_blogger=is_blogger, is_admin=is_admin)
    
   
    return app
    
    