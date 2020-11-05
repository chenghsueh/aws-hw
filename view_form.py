#view_form.py

from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, PasswordField, validators
from wtforms.fields.html5 import EmailField

from wtforms.validators import DataRequired, Email, Length, EqualTo

class UserForm(FlaskForm):
    username = StringField('UserName', validators=[DataRequired(message='Not Null')])
    password = PasswordField('Password', validators=[Length(min=4, max=25), DataRequired(message='Not Null')])
    confirm = PasswordField('confirm', validators=[DataRequired(message='Not Null'), EqualTo('password', message='Passwords must match')])
    telephone = StringField('Telephone', validators=[DataRequired(message='Not Null')])
    email = EmailField('Email', validators=[DataRequired(message='Not Null')])
    address = StringField('Address')
    submit = SubmitField('Submit')
