from flask import Flask, render_template, redirect, url_for, request, flash, Blueprint, jsonify, make_response
from flask_login import login_user, logout_user, login_required, current_user
from models import User
from project.config import Config
from project import login_manager
from project.users.forms import LoginForm, RegisterForm
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import mysql.connector

users = Blueprint('users', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

db_config = {
    'user': Config.DB_USER,
    'password': Config.DB_PASS,
    'host': Config.DB_HOST,
    'database': Config.DB_NAME
}

@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.find_by_username(username)
        if user and User.check_password(user.password, password):
            login_user(user)
            access_token = create_access_token(identity={'username': username})
            response = make_response(redirect(url_for('main.home')))
            response.set_cookie('access_token', access_token, httponly=True, samesite='Strict')
            flash('Logged in successfully.', 'success')
            return response 
        flash('Invalid username or password.', 'danger')
    return render_template('login.html', form=form)



@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        hashed_password = User.hash_password(password)
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO user (user_username, user_password) VALUES (%s, %s)", (username, hashed_password))
            conn.commit()
            cursor.close()
            conn.close()
            flash('Registration successful.', 'success')
            return redirect(url_for('users.login'))
        except mysql.connector.Error as err:
            print(f"Database Error: {err}")
            flash('Failed to register user. Please try again.', 'danger')
    return render_template('register.html', form=form)

@users.route('/logout')
@login_required
def logout():
    logout_user()
    response = make_response(redirect(url_for('users.login')))
    response.set_cookie('access_token', '', expires=0)
    flash('You have been logged out.', 'success')
    return response

@users.route('/protected', methods=['GET'])
@jwt_required()
def protected():
     current_user = get_jwt_identity()
     return jsonify(logged_in_as=current_user), 200
