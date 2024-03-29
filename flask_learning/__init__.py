from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from flask_login import LoginManager


base_dir = os.path.abspath(os.path.dirname(__file__))

login_manager = LoginManager()


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager.init_app(app)
login_manager.login_view = 'login'

from flask_learning.person.views import person_blueprint
from flask_learning.hobby.views import hobby_blueprint

app.register_blueprint(person_blueprint)
app.register_blueprint(hobby_blueprint)

