from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms.fields import (StringField, SubmitField, 
        BooleanField, DateTimeField, 
        RadioField, SelectField,
        TextAreaField)
from wtforms.validators import DataRequired


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    breed = StringField('What breed are you ?', validators=[DataRequired()])
    oota = BooleanField("Oota Aaita ?")
    mood = RadioField("Please choose your mood: ",
                choices=[('mood_one', 'Happy'), ('mood_two', 'Exited')])
    food_choice = SelectField('Pick your favourite Food: ',
                            choices=[('NE', 'Uttar Bhartiya'), ('SE', 'Dakshin Bhartiya')])
    feedback = TextAreaField()

    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = InfoForm()

    if form.validate_on_submit():
        flash('Thank you for submitting...')
        session['breed'] = form.breed.data
        session['oota'] = form.oota.data
        session['mood'] = form.mood.data
        session['food_choice'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('thankyou'))

    return render_template('home.html', form=form)

@app.route('/milk')
def milk():
    return render_template('milk.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/thankyou', methods=['GET', 'POST'])
def thankyou():
    email = request.args.get('email')
    password = request.args.get('password')

    return render_template('thankyou.html', email=email, password=password)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/info/<name>')
def name(name):
    return '100th Letter is {} </h1>'.format(name[100])

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
