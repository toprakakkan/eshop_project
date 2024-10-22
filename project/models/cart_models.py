from project.config import db_connection

class CartModel:

    @staticmethod
    def get_product_details(product_id):
        conn, cursor = db_connection()
        
        cursor.execute("""
            SELECT p.product_id, p.product_name, p.product_price, pp.product_picture_url
            FROM product p
            LEFT JOIN product_picture pp ON p.product_id = pp.product_id
            WHERE p.product_id = %s
        """, (product_id,))
        product = cursor.fetchone()
        
        cursor.close()
        conn.close()

        return product
