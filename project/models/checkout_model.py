from project.config import db_connection

class CheckoutModel:

    @staticmethod
    def get_cart_items(cart):
        cart_items = []
        total_price = 0
        conn, cursor = db_connection()

        for product_id, quantity in cart.items():
            cursor.execute("SELECT * FROM product WHERE product_id = %s", (product_id,))
            product = cursor.fetchone()
            if product:
                product['quantity'] = quantity
                product['total_price'] = product['product_price'] * quantity
                cart_items.append(product)
                total_price += product['total_price']

        cursor.close()
        conn.close()

        return cart_items, total_price
