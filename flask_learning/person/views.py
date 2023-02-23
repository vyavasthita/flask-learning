from flask import Blueprint, render_template, redirect, url_for
from flask_learning import db
from flask_learning.models import Person
from flask_learning.person.forms import AddForm, DelForm


person_blueprint = Blueprint('person', __name__, 
                    template_folder='templates/person')


@person_blueprint.route('/add', methods=['GET', 'POST'])
def add_person():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data

        person = Person(name, age)

        db.session.add(person)
        db.session.commit()

        return redirect(url_for('person.list_person'))
    return render_template('add.html', form=form)

@person_blueprint.route('/delete', methods=['GET', 'POST'])
def delete_person():
    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        person = Person.query.get(id)
        db.session.delete(person)
        db.session.commit()

        return redirect(url_for('person.list_person'))
    return render_template('delete.html', form=form)

@person_blueprint.route('/list')
def list_person():
    persons = Person.query.all()
    return render_template('list.html', persons=persons)