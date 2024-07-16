from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length, Email
from flask_wtf import FlaskForm

class CheckoutForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    adress = PasswordField('Adress', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    credit_card = PasswordField('Credit Card Number', validators=[DataRequired()])
    submit = SubmitField('Place Order')