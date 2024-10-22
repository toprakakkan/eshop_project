from flask import Blueprint, render_template, request, flash, redirect, url_for, abort
from project.users.decorators import admin_required
from flask_login import login_required, current_user
from project.models.ticket_models import TicketModel  

tickets = Blueprint('tickets', __name__)

TICKETS_PER_PAGE = 20  

@tickets.route("/tickets", methods=['GET'])
@login_required
@admin_required
def tickets_page():
    page = request.args.get('page', 1, type=int)
    offset = (page - 1) * TICKETS_PER_PAGE

    total_tickets = TicketModel.get_total_tickets()
    total_pages = (total_tickets + TICKETS_PER_PAGE - 1) // TICKETS_PER_PAGE

    tickets = TicketModel.get_tickets(offset, TICKETS_PER_PAGE)

    return render_template('tickets.html', title='Ticket Page', tickets=tickets, page=page, total_pages=total_pages)

@tickets.route("/ticket/<int:ticket_id>")
@login_required
@admin_required
def ticket_detail(ticket_id):
    ticket = TicketModel.get_ticket_detail(ticket_id)

    if ticket is None:
        abort(404)

    return render_template('ticket_detail.html', title='Ticket Detail', ticket=ticket)

@tickets.route("/ticket/delete/<int:ticket_id>", methods=['POST'])
@login_required
@admin_required
def delete_ticket(ticket_id):
    TicketModel.delete_ticket(ticket_id, current_user.id)

    flash('Ticket has been successfully marked as deleted.', 'success')
    return redirect(url_for('tickets.tickets_page'))
