from project.config import db_connection

class ProductModel:

    @staticmethod
    def get_categories():
        conn, cursor = db_connection()
        
        cursor.execute("SELECT category_id, category_name FROM category ORDER BY category_name ASC")
        categories = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        return categories

    @staticmethod
    def add_product(category_id, name, price, description, image_urls):
        conn, cursor = db_connection()
        
        sql_product = """
        INSERT INTO Product (category_id, product_name, product_price, product_description) 
        VALUES (%s, %s, %s, %s)
        """
        values_product = (category_id, name, price, description)
        
        cursor.execute(sql_product, values_product)
        product_id = cursor.lastrowid

        sql_image = """
        INSERT INTO Product_Picture (product_id, product_picture_url, product_picture_url2, product_picture_url3)
        VALUES (%s, %s, %s, %s)
        """
        values_image = (product_id, *image_urls)
        
        cursor.execute(sql_image, values_image)
        
        conn.commit()
        
        cursor.close()
        conn.close()
        
        return product_id

    @staticmethod
    def get_product_detail(product_id):
        conn, cursor = db_connection()
        
        cursor.execute("""
            SELECT p.product_id, p.product_name, p.product_description, p.product_price, pp.product_picture_url, pp.product_picture_url2, pp.product_picture_url3
            FROM Product p
            LEFT JOIN Product_Picture pp ON p.product_id = pp.product_id
            WHERE p.product_id = %s
        """, (product_id,))
        product = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        return product
