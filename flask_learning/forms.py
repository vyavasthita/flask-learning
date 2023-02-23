from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    name = StringField('Name of Human:')
    submit = SubmitField('Add Human')

class DelForm(FlaskForm):
    id = IntegerField('If of the human to be removed:')
    submit = SubmitField('Remove Human')