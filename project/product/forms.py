
from wtforms import  IntegerField, StringField, BooleanField, TextAreaField, validators, SelectField, URLField
from flask_wtf import FlaskForm

class AddProducts(FlaskForm):
    category_id = SelectField('Category', coerce=int)
    name = StringField('Name',[validators.DataRequired()])
    price = IntegerField('Price',[validators.DataRequired()])
    description = TextAreaField('Description',[validators.DataRequired()])
    image_url = URLField('Image URL', [validators.DataRequired(), validators.URL()])
    image_url2 = URLField('Image URL 2', [validators.URL()])
    image_url3 = URLField('Image URL 3', [validators.URL()])
    
    
    