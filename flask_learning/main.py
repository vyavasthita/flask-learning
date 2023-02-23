from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms.fields import (StringField, SubmitField, 
        BooleanField, DateTimeField, 
        RadioField, SelectField,
        TextAreaField)
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from forms import AddForm, DelForm


base_dir = os.path.abspath(os.path.dirname(__file__))
print(base_dir)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Human(db.Model):
    __tablename__ = 'human'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    # One to One
    education = db.relationship('Education', backref='person', uselist=False)

    # One to Many
    hobbies = db.relationship('Hobby', backref='person', lazy='dynamic')

    def __init__(self, name, age, city) -> None:
        super().__init__()
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"Person {self.name} is {self.age} years old"

    def report_hobbies(self):
        print("Here are my hobbies...")
        
        for h in self.hobbies:
            print(h.hobby)

class Education(db.Model):
    __tablename__ = 'education'
    id = db.Column(db.Integer, primary_key=True)
    qualification = db.Column(db.Text)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))

    def __init__(self, qualification, person_id) -> None:
        super().__init__()
        self.qualification = qualification
        self.person_id = person_id

class Hobby(db.Model):
    __tablename__ = 'hobby'

    id = db.Column(db.Integer, primary_key=True)
    hobby = db.Column(db.Text)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))

    def __init__(self, hobby, person_id) -> None:
        super().__init__()
        self.hobby = hobby
        self.person_id = person_id

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

@app.route('/add', methods=['GET', 'POST'])
def add_human():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        human = Human(name)
        db.session.add(human)
        db.session.commit()

        return redirect(url_for('list_human'))
    return render_template('add.html', form=form)

@app.route('/delete', methods=['GET', 'POST'])
def delete_human():
    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        human = Human.query.get(id)
        db.session.delete(human)
        db.session.commit()

        return redirect(url_for('list_human'))
    return render_template('delete.html', form=form)

@app.route('/list', methods=['GET', 'POST'])
def list_human():
    humans = Human.query.all()
    print(humans)
    return render_template('list.html', humans=humans)

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
