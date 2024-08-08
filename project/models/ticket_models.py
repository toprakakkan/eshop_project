from project.config import db_connection
from datetime import datetime

class TicketModel:

    @staticmethod
    def get_total_tickets():
        conn, cursor = db_connection()

        cursor.execute("SELECT COUNT(*) AS count FROM contact_tickets WHERE ticket_isDeleted = 0")
        total_tickets = cursor.fetchone()['count']

        cursor.close()
        conn.close()

        return total_tickets

    @staticmethod
    def get_tickets(offset, limit):
        conn, cursor = db_connection()

        cursor.execute("""
            SELECT ticket_id, ticket_email, ticket_content 
            FROM contact_tickets 
            WHERE ticket_isDeleted = 0 
            ORDER BY ticket_id DESC 
            LIMIT %s OFFSET %s
        """, (limit, offset))
        tickets = cursor.fetchall()

        cursor.close()
        conn.close()

        return tickets

    @staticmethod
    def get_ticket_detail(ticket_id):
        conn, cursor = db_connection()

        cursor.execute("""
            SELECT ticket_id, ticket_email, ticket_content 
            FROM contact_tickets 
            WHERE ticket_id = %s AND ticket_isDeleted = 0
        """, (ticket_id,))
        ticket = cursor.fetchone()

        cursor.close()
        conn.close()

        return ticket

    @staticmethod
    def delete_ticket(ticket_id, user_id):
        conn, cursor = db_connection()

        update_query = """
            UPDATE contact_tickets 
            SET ticket_isDeleted = 1, ticket_deleteUid = %s, ticket_deleteTime = %s 
            WHERE ticket_id = %s
        """
        cursor.execute(update_query, (user_id, datetime.now(), ticket_id))
        conn.commit()

        cursor.close()
        conn.close()
