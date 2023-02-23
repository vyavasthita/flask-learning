from flask import Blueprint, render_template, redirect, url_for
from flask_learning import db
from flask_learning.models import Hobby
from flask_learning.hobby.forms import AddForm

hobby_blueprint = Blueprint('hobby', __name__, 
                    template_folder='templates/hobby')


@hobby_blueprint.route('/add', methods=['GET', 'POST'])
def add_human():
    form = AddForm()

    if form.validate_on_submit():
        hobby = form.hobby.data
        person_id = form.person_id.data

        hobby = Hobby(hobby, person_id)
        db.session.add(hobby)
        db.session.commit()

        return redirect(url_for('list_human'))
    return render_template('add_owner.html', form=form)