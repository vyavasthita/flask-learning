from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    hobby = StringField('Hobby:')
    person_id = IntegerField('Id of Person')
    submit = SubmitField('Add Hobby')

