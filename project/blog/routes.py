from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import current_user, login_required
from project.blog.forms import PostForm, AddComment
from project.config import Config
import mysql.connector
from project.users.decorators import admin_required
from datetime import datetime


blog = Blueprint('blog', __name__)

db_config = {
    'user': Config.DB_USER,
    'password': Config.DB_PASS,
    'host': Config.DB_HOST,
    'database': Config.DB_NAME
}

@blog.route("/blog")
def blog_home():
    page = request.args.get('page', 1, type=int)
    per_page = 5  
    offset = (page - 1) * per_page

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(*) AS total FROM blog")
    total_posts = cursor.fetchone()['total']

    cursor.execute("""
        SELECT b.blog_id, b.blog_fotoUrl, b.blog_content, b.blog_title, b.blog_date, b.blog_readCount, u.user_username AS author
        FROM blog b 
        JOIN user u ON b.user_id = u.user_id
        WHERE blog_deleteTime IS NULL
        ORDER BY b.blog_date DESC
        LIMIT %s OFFSET %s
    """, (per_page, offset))
    posts = cursor.fetchall()

    cursor.execute("SELECT blog_category_id, blog_category_name FROM blog_category")
    categories = cursor.fetchall()

    cursor.close()
    conn.close()

    for post in posts:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT bc.blog_category_name
            FROM blog_category_combiner bcc
            JOIN blog_category bc ON bcc.blog_category_id = bc.blog_category_id
            WHERE bcc.blog_id = %s
        """, (post['blog_id'],))
        post['categories'] = [category['blog_category_name'] for category in cursor.fetchall()]

    total_pages = (total_posts + per_page - 1) // per_page

    return render_template('blog.html', posts=posts, categories=categories, page=page, total_pages=total_pages)



@blog.route("/blog/new", methods=['GET', 'POST'])
@login_required
@admin_required
def new_post():
    form = PostForm()

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT blog_category_id, blog_category_name FROM blog_category")
        categories = cursor.fetchall()
        cursor.close()
        conn.close()

        form.categories.choices = [(category['blog_category_id'], category['blog_category_name']) for category in categories]

        if request.method == 'POST' and form.validate():
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            sql_post = """
            INSERT INTO blog (blog_fotoUrl, blog_content, blog_title, user_id, blog_date) 
            VALUES (%s, %s, %s, %s, %s)
            """
            values_post = (
                form.picture.data,
                form.content.data,
                form.title.data,
                current_user.id,
                current_date
            )

            cursor.execute(sql_post, values_post)
            post_id = cursor.lastrowid

            sql_category_combiner = "INSERT INTO blog_category_combiner (blog_id, blog_category_id) VALUES (%s, %s)"
            for category_id in form.categories.data:
                cursor.execute(sql_category_combiner, (post_id, category_id))

            conn.commit()
            cursor.close()
            conn.close()

            flash('Post created successfully!', 'success')
            return redirect(url_for('blog.new_post'))

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        flash('Failed to create post. Please try again.', 'danger')
    except Exception as e:
        print(f"Unexpected Error: {e}")
        flash('An unexpected error occurred. Please try again.', 'danger')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

    return render_template('addpost.html', title='Add Product Page', form=form)

@blog.route("/blog/<int:blog_id>", methods=['GET', 'POST'])
def post(blog_id):
    form = AddComment()
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("""
        UPDATE blog
        SET blog_readCount = blog_readCount + 1
        WHERE blog_id = %s
    """, (blog_id,))
    conn.commit()

    cursor.execute("""
        SELECT b.blog_id, b.blog_fotoUrl, b.blog_content, b.blog_title, b.blog_date, b.blog_readCount, u.user_username AS author
        FROM blog b
        JOIN user u ON b.user_id = u.user_id
        WHERE b.blog_id = %s
    """, (blog_id,))
    post = cursor.fetchone()

    if not post:
        cursor.close()
        conn.close()
        abort(404)

    cursor.execute("""
        SELECT bc.blog_category_name
        FROM blog_category_combiner bcc
        JOIN blog_category bc ON bcc.blog_category_id = bc.blog_category_id
        WHERE bcc.blog_id = %s
    """, (blog_id,))
    post['categories'] = [category['blog_category_name'] for category in cursor.fetchall()]

    cursor.execute("""
        SELECT blogcom_id, blogcom_content, blogcom_date, blogcom_name AS author
        FROM blog_comments
        WHERE blog_id = %s
        ORDER BY blogcom_date DESC
    """, (blog_id,))
    comments = cursor.fetchall()

    if form.validate_on_submit():
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            
            current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            sql_comment = """
            INSERT INTO blog_comments (blog_id, blogcom_content, blogcom_name, blogcom_email, blogcom_date) 
            VALUES (%s, %s, %s, %s, %s)
            """
            values_comment = (
                blog_id,
                form.content.data,
                form.name.data,
                form.email.data,
                current_date
            )

            cursor.execute(sql_comment, values_comment)
            conn.commit()
            cursor.close()
            conn.close()

            flash('Your comment has been added.', 'success')
            return redirect(url_for('blog.post', blog_id=blog_id))

        except mysql.connector.Error as err:
            print(f"Database Error: {err}")
            flash('Failed to add comment. Please try again.', 'danger')
        except Exception as e:
            print(f"Unexpected Error: {e}")
            flash('An unexpected error occurred. Please try again.', 'danger')
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
                
    
    return render_template('post.html', post=post, comments=comments, form=form)


@blog.route("/blog/<int:blog_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(blog_id):
    form = PostForm()
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute("SELECT blog_category_id, blog_category_name FROM blog_category")
        categories = cursor.fetchall()
        form.categories.choices = [(category['blog_category_id'], category['blog_category_name']) for category in categories]

        cursor.execute("SELECT * FROM blog WHERE blog_id = %s", (blog_id,))
        post = cursor.fetchone()

        if not post:
            abort(404)

        if post['user_id'] != current_user.id:
            abort(403)

        if request.method == 'POST' and form.validate():
            current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            sql_update_post = """
            UPDATE blog 
            SET blog_fotoUrl = %s, blog_content = %s, blog_title = %s, blog_updateTime = %s
            WHERE blog_id = %s
            """
            values_update_post = (
                form.picture.data,
                form.content.data,
                form.title.data,
                current_date,
                blog_id
            )

            cursor.execute(sql_update_post, values_update_post)
            
            cursor.execute("DELETE FROM blog_category_combiner WHERE blog_id = %s", (blog_id,))
            sql_category_combiner = "INSERT INTO blog_category_combiner (blog_id, blog_category_id) VALUES (%s, %s)"
            for category_id in form.categories.data:
                cursor.execute(sql_category_combiner, (blog_id, category_id))

            conn.commit()

            flash('Your post has been successfully updated!', 'success')
            return redirect(url_for('blog.post', blog_id=blog_id))

        if request.method == 'GET':
            form.picture.data = post['blog_fotoUrl']
            form.content.data = post['blog_content']
            form.title.data = post['blog_title']
            form.categories.data = [category['blog_category_id'] for category in categories]

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        flash('Failed to update post. Please try again.', 'danger')
    except Exception as e:
        print(f"Unexpected Error: {e}")
        flash('An unexpected error occurred. Please try again.', 'danger')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

    return render_template('update.html', title='Update Post', form=form, blog_id=blog_id)




@blog.route("/blog/<int:blog_id>/delete", methods=['POST'])
@login_required
def delete_post(blog_id):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM blog WHERE blog_id = %s", (blog_id,))
        post = cursor.fetchone()

        if not post:
            abort(404)

        if post['user_id'] != current_user.id:
            abort(403)

        deletion_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("UPDATE blog SET blog_deleteTime = %s WHERE blog_id = %s", (deletion_time, blog_id))
        conn.commit()

        flash('Your post has been successfully deleted!', 'success')

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        flash('Failed to delete post. Please try again.', 'danger')
    except Exception as e:
        print(f"Unexpected Error: {e}")
        flash('An unexpected error occurred. Please try again.', 'danger')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

    return redirect(url_for('blog.blog_home'))