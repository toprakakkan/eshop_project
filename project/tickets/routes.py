from flask import Blueprint, render_template, request, flash, redirect, url_for, abort
import mysql.connector
from project.config import Config
from project.users.decorators import admin_required
from flask_login import login_required, current_user
from datetime import datetime

tickets = Blueprint('tickets', __name__)

db_config = {
    'user': Config.DB_USER,
    'password': Config.DB_PASS,
    'host': Config.DB_HOST,
    'database': Config.DB_NAME
}

TICKETS_PER_PAGE = 20  # Set the number of tickets per page

@tickets.route("/tickets", methods=['GET'])
@login_required
@admin_required
def tickets_page():
    page = request.args.get('page', 1, type=int)
    offset = (page - 1) * TICKETS_PER_PAGE

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)

    # Query to get the total count of tickets
    count_query = "SELECT COUNT(*) AS count FROM contact_tickets WHERE ticket_isDeleted = 0"
    cursor.execute(count_query)
    total_tickets = cursor.fetchone()['count']
    total_pages = (total_tickets + TICKETS_PER_PAGE - 1) // TICKETS_PER_PAGE

    # Main query to get tickets with pagination
    query = """
    SELECT ticket_id, ticket_email, ticket_content 
    FROM contact_tickets 
    WHERE ticket_isDeleted = 0 
    ORDER BY ticket_id DESC 
    LIMIT %s OFFSET %s
    """
    cursor.execute(query, (TICKETS_PER_PAGE, offset))
    tickets = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('tickets.html', title='Ticket Page', tickets=tickets, page=page, total_pages=total_pages)

@tickets.route("/ticket/<int:ticket_id>")
@login_required
@admin_required
def ticket_detail(ticket_id):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)

    query = "SELECT ticket_id, ticket_email, ticket_content FROM contact_tickets WHERE ticket_id = %s AND ticket_isDeleted = 0"
    cursor.execute(query, (ticket_id,))
    ticket = cursor.fetchone()

    cursor.close()
    connection.close()

    if ticket is None:
        abort(404)

    return render_template('ticket_detail.html', title='Ticket Detail', ticket=ticket)

@tickets.route("/ticket/delete/<int:ticket_id>", methods=['POST'])
@login_required
@admin_required
def delete_ticket(ticket_id):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    update_query = """
    UPDATE contact_tickets 
    SET ticket_isDeleted = 1, ticket_deleteUid = %s, ticket_deleteTime = %s 
    WHERE ticket_id = %s
    """
    cursor.execute(update_query, (current_user.id, datetime.now(), ticket_id))
    connection.commit()

    cursor.close()
    connection.close()

    flash('Ticket has been successfully marked as deleted.', 'success')
    return redirect(url_for('tickets.tickets_page'))
