from flask_learning import app, db
from flask import render_template, request, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms.fields import (StringField, SubmitField, 
        BooleanField, 
        RadioField, SelectField,
        TextAreaField)
from wtforms.validators import DataRequired
from flask_login import login_required, login_user, logout_user
from flask_learning.forms import LoginForm, RegistrationForm
from flask_learning.models import User


class Human(db.Model):
    __tablename__ = 'human'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

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

@app.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user is not None and user.check_password(form.password.data):
            login_user(user)
            flash('Logged in successfully')

            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('welcome')

            return redirect(next)

    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registration')

        return redirect(url_for('login'))

    return render_template('register.html', form=form)

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

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
