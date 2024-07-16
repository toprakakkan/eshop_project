from .forms import AddProducts
from flask import render_template, request, Blueprint, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
import mysql.connector
from project.config import Config
from project.users.decorators import admin_required


product = Blueprint('product', __name__)

db_config = {
    'user': Config.DB_USER,
    'password': Config.DB_PASS,
    'host': Config.DB_HOST,
    'database': Config.DB_NAME
}

def get_categories():
    conn = mysql.connector.connect(**db_config)
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT category_id, category_name FROM category ORDER BY category_name ASC")
    categories = cursor.fetchall()
    cursor.close()
    conn.close()
    return categories

@product.route('/addproduct', methods=['POST', 'GET'])
@login_required
@admin_required
def add_product():
    categories = get_categories()
    category_choices = [(category['category_id'], category['category_name']) for category in categories]
    
    form = AddProducts(request.form)
    form.category_id.choices = category_choices
    
    if request.method == 'POST' and form.validate():
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            sql = """
            INSERT INTO Product (category_id, product_name, product_price, product_description) 
            VALUES (%s, %s, %s, %s)
            """
            values_product = (
                form.category_id.data,
                form.name.data,
                form.price.data,
                form.description.data
            )

            cursor.execute(sql, values_product)
            product_id = cursor.lastrowid

            sql_image = """
            INSERT INTO Product_Picture (product_id, product_picture_url)
            VALUES (%s, %s)
            """
            values_image = (
                product_id,
                form.image_url.data
            )

            cursor.execute(sql_image, values_image)
            
            conn.commit()

            cursor.close()
            conn.close()

            flash('Product added successfully!', 'success')
            return redirect(url_for('product.add_product'))
        except mysql.connector.Error as err:
            print(f"Database Error: {err}")
            flash('Failed to add product. Please try again.', 'danger')
        except Exception as e:
            print(f"Unexpected Error: {e}")
            flash('An unexpected error occurred. Please try again.', 'danger')
    else:
        print("Form validation failed or method is GET")
        print("Form errors:", form.errors)

    return render_template('addproduct.html', title='Add Product Page', form=form)


@product.route('/product/<int:product_id>', methods=['GET'])
def product_detail(product_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT p.product_id, p.product_name, p.product_description, p.product_price, pp.product_picture_url 
        FROM Product p
        LEFT JOIN Product_Picture pp ON p.product_id = pp.product_id
        WHERE p.product_id = %s
    """, (product_id,))
    product = cursor.fetchone()

    cursor.close()
    conn.close()

    return jsonify(product)
