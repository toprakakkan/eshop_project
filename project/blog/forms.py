from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, URLField, validators, SelectMultipleField, EmailField
from wtforms.validators import DataRequired
from wtforms.widgets import ListWidget, CheckboxInput

class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    picture = URLField('Image URL', [validators.DataRequired(), validators.URL()])
    categories = MultiCheckboxField('Categories', coerce=int)
    submit = SubmitField('Post')
    
class AddComment(FlaskForm):
    
    content = TextAreaField('Content', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('E-mail', validators=[DataRequired()])
    submit = SubmitField('Post')

