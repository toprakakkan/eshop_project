from flask import Blueprint, render_template, redirect, url_for, flash
from project.contact.forms import CreateTicket
from project.models.contact_models import ContactModel  

contact = Blueprint('contact', __name__)

@contact.route("/contact", methods=['GET', 'POST'])
def contact_page():
    form = CreateTicket()
    if form.validate_on_submit():
        email = form.email.data
        content = form.content.data

        ContactModel.create_ticket(email, content)

        flash('Your message has been sent!', 'success')
        return redirect(url_for('contact.contact_page'))
    
    contact_info = ContactModel.get_contact_info()

    return render_template('contact.html', title='Contact Page', form=form, contact_info=contact_info)
