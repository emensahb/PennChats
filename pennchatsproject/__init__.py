# pennchatsproject/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)


################################
######## Database Setup ########
################################

# Using SQLite for now, configuration code for PostgreSQL commented out
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:Jf_CSAx^ld192@localhost/pennchats'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


#####################################
######## Login Configuration ########
#####################################

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'
#login_manager.login_view = 'students.login'

######################################


from pennchatsproject.core.views import core
from pennchatsproject.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(error_pages)
