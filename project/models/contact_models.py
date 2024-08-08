from project.config import db_connection

class ContactModel:

    @staticmethod
    def create_ticket(email, content):
        conn, cursor = db_connection()

        cursor.execute("""
            INSERT INTO contact_tickets (ticket_email, ticket_content)
            VALUES (%s, %s)
        """, (email, content))

        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_contact_info():
        conn, cursor = db_connection()
        
        cursor.execute("SELECT contact_address, contact_phone, contact_supEmail FROM contact WHERE contact_isDeleted = 0")
        contact_info = cursor.fetchone()
        
        cursor.close()
        conn.close()

        return contact_info
