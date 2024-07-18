from wtforms import  TextAreaField, EmailField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired

class CreateTicket(FlaskForm):
    content = TextAreaField('Content', validators=[DataRequired()])
    email = EmailField('E-mail', validators=[DataRequired()])
    submit = SubmitField('Submit')
    