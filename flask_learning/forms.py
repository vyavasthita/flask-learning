from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from .models import User
from wtforms import ValidationError


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
   
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password_confirm', message='Password must match.')])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has already been registered.')

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username is taken.')
    

class AddForm(FlaskForm):
    name = StringField('Name of Human:')
    submit = SubmitField('Add Human')

class DelForm(FlaskForm):
    id = IntegerField('If of the human to be removed:')
    submit = SubmitField('Remove Human')