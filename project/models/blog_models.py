from project.config import db_connection
from datetime import datetime

class BlogModel:

    @staticmethod
    def get_blog_home(page, per_page):
        offset = (page - 1) * per_page

        conn, cursor = db_connection()

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

        return total_posts, posts, categories

    @staticmethod
    def get_post_categories(blog_id):
        conn, cursor = db_connection()

        cursor.execute("""
            SELECT bc.blog_category_name
            FROM blog_category_combiner bcc
            JOIN blog_category bc ON bcc.blog_category_id = bc.blog_category_id
            WHERE bcc.blog_id = %s
        """, (blog_id,))
        categories = [category['blog_category_name'] for category in cursor.fetchall()]

        cursor.close()
        conn.close()

        return categories

    @staticmethod
    def create_post(picture, content, title, user_id, categories):
        conn, cursor = db_connection()

        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        sql_post = """
        INSERT INTO blog (blog_fotoUrl, blog_content, blog_title, user_id, blog_date) 
        VALUES (%s, %s, %s, %s, %s)
        """
        values_post = (picture, content, title, user_id, current_date)

        cursor.execute(sql_post, values_post)
        post_id = cursor.lastrowid

        sql_category_combiner = "INSERT INTO blog_category_combiner (blog_id, blog_category_id) VALUES (%s, %s)"
        for category_id in categories:
            cursor.execute(sql_category_combiner, (post_id, category_id))

        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_post(blog_id):
        conn, cursor = db_connection()

        cursor.execute("""
            SELECT b.blog_id, b.blog_fotoUrl, b.blog_content, b.blog_title, b.blog_date, b.blog_readCount, b.user_id, u.user_username AS author
            FROM blog b
            JOIN user u ON b.user_id = u.user_id
            WHERE b.blog_id = %s
        """, (blog_id,))
        post = cursor.fetchone()

        cursor.close()
        conn.close()

        return post

    @staticmethod
    def update_read_count(blog_id):
        conn, cursor = db_connection()

        cursor.execute("""
            UPDATE blog
            SET blog_readCount = blog_readCount + 1
            WHERE blog_id = %s
        """, (blog_id,))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_comments(blog_id):
        conn, cursor = db_connection()

        cursor.execute("""
            SELECT blogcom_id, blogcom_content, blogcom_date, blogcom_name AS author
            FROM blog_comments
            WHERE blog_id = %s AND blogcom_isDeleted = 0
            ORDER BY blogcom_date DESC
        """, (blog_id,))
        comments = cursor.fetchall()

        cursor.close()
        conn.close()

        return comments

    @staticmethod
    def add_comment(blog_id, content, name, email):
        conn, cursor = db_connection()

        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        sql_comment = """
        INSERT INTO blog_comments (blog_id, blogcom_content, blogcom_name, blogcom_email, blogcom_date) 
        VALUES (%s, %s, %s, %s, %s)
        """
        values_comment = (blog_id, content, name, email, current_date)

        cursor.execute(sql_comment, values_comment)
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def update_post(blog_id, picture, content, title, categories):
        conn, cursor = db_connection()

        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        sql_update_post = """
        UPDATE blog 
        SET blog_fotoUrl = %s, blog_content = %s, blog_title = %s, blog_updateTime = %s
        WHERE blog_id = %s
        """
        values_update_post = (picture, content, title, current_date, blog_id)

        cursor.execute(sql_update_post, values_update_post)

        cursor.execute("DELETE FROM blog_category_combiner WHERE blog_id = %s", (blog_id,))
        sql_category_combiner = "INSERT INTO blog_category_combiner (blog_id, blog_category_id) VALUES (%s, %s)"
        for category_id in categories:
            cursor.execute(sql_category_combiner, (blog_id, category_id))

        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def delete_post(blog_id):
        conn, cursor = db_connection()

        deletion_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("UPDATE blog SET blog_deleteTime = %s WHERE blog_id = %s", (deletion_time, blog_id))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def delete_comment(blogcom_id):
        conn, cursor = db_connection()

        deletion_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("UPDATE blog_comments SET blogcom_deleteTime = %s, blogcom_isDeleted = 1 WHERE blogcom_id = %s", (deletion_time, blogcom_id))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_categories():
        conn, cursor = db_connection()

        cursor.execute("SELECT blog_category_id, blog_category_name FROM blog_category")
        categories = cursor.fetchall()

        cursor.close()
        conn.close()

        return categories

    @staticmethod
    def get_comment(blogcom_id):
        conn, cursor = db_connection()

        cursor.execute("SELECT * FROM blog_comments WHERE blogcom_id = %s", (blogcom_id,))
        comment = cursor.fetchone()

        cursor.close()
        conn.close()

        return comment
