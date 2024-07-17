
from wtforms import  IntegerField, StringField, BooleanField, TextAreaField, validators, SelectField, URLField
from flask_wtf import FlaskForm
from project.product.validators import OptionalURL

class AddProducts(FlaskForm):
    category_id = SelectField('Category', coerce=int)
    name = StringField('Name',[validators.DataRequired()])
    price = IntegerField('Price',[validators.DataRequired()])
    description = TextAreaField('Description',[validators.DataRequired()])
    image_url = URLField('Image URL (Cover Picture)', [validators.DataRequired(), validators.URL()])
    image_url2 = URLField('Image URL 2', [OptionalURL()])
    image_url3 = URLField('Image URL 3', [OptionalURL()])
    
    
    