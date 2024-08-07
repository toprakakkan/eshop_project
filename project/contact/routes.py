from flask import Blueprint, render_template, redirect, url_for, flash
import mysql.connector
from project.contact.forms import CreateTicket
from project.config import Config
from flask_jwt_extended import jwt_required

contact = Blueprint('contact', __name__)

db_config = {
    'user': Config.DB_USER,
    'password': Config.DB_PASS,
    'host': Config.DB_HOST,
    'database': Config.DB_NAME
}


@contact.route("/contact", methods=['GET', 'POST'])
def contact_page():
    form = CreateTicket()
    if form.validate_on_submit():
        email = form.email.data
        content = form.content.data

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO contact_tickets (ticket_email, ticket_content)
            VALUES (%s, %s)
        """, (email, content))

        conn.commit()

        cursor.close()
        conn.close()

        flash('Your message has been sent!', 'success')
        return redirect(url_for('contact.contact_page'))
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT contact_address, contact_phone, contact_supEmail FROM contact WHERE contact_isDeleted = 0")
    contact_info = cursor.fetchone()
    cursor.close()
    conn.close()

    return render_template('contact.html', title='Contact Page', form=form, contact_info=contact_info)


