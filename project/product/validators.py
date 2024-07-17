from wtforms.validators import URL, ValidationError

class OptionalURL(URL):
    def __call__(self, form, field):
        if field.data and field.data.strip():
            super(OptionalURL, self).__call__(form, field)
        else:
            field.data = None