from project.config import db_connection

class ShopModel:

    @staticmethod
    def get_products(category_id=None):
        conn, cursor = db_connection()

        if category_id:
            cursor.execute("""
                SELECT product_id, product_name, product_description, product_price, product_coverPictureUrl
                FROM product 
                WHERE category_id = %s
            """, (category_id,))
        else:
            cursor.execute("""
                SELECT product_id, product_name, product_description, product_price, product_coverPictureUrl
                FROM product
            """)

        products = cursor.fetchall()
        cursor.close()
        conn.close()
        return products

    @staticmethod
    def get_product_pictures():
        conn, cursor = db_connection()
        
        cursor.execute("""
            SELECT product_id, product_picture_url, product_picture_url2, product_picture_url3 
            FROM Product_Picture
        """)
        
        pictures = cursor.fetchall()
        cursor.close()
        conn.close()
        return pictures