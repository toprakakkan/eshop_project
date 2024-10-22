from project.config import db_connection

class MainModel:

    @staticmethod
    def get_home_products():
        conn, cursor = db_connection()
        
        cursor.execute("""
            SELECT p.product_name, pp.product_picture_url
            FROM product p
            LEFT JOIN product_picture pp ON p.product_id = pp.product_id
            WHERE p.product_coverPictureUrl IN (1, 2, 3)
        """)
        
        products = cursor.fetchall()
        cursor.close()
        conn.close()
        return products
