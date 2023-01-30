from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp

class EnterNumberForm(FlaskForm):
    arabicNumber = StringField('Enter the number here: ', validators = [DataRequired(), Length(min = 1, max = 12, message = 'Numbers can only be up to 12 digits in length'), Regexp('^[0-9]+$', message = 'We can\'t convert letters!')])
    submit = SubmitField('Convert')