# pennchatsproject/__init__.py
# this will hold a lot of our flask application logic and blueprint logic
# to be worked on between Audra, Efua and Jimmy

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()

app = Flask(__name__)

################################
######## Database Setup ########
################################
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:pbNdO#cdxtskP7Da9d7@@localhost/pennchats'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


#####################################
######## Login Configuration ########
#####################################

login_manager.init_app(app)
login_manager.login_view = 'login'




##################################################
##### Register Blueprints for different pages#####
##################################################

from pennchatsproject.core.views import core
from pennchatsproject.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(error_pages)
