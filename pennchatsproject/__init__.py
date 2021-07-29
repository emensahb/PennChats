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
#print(basedir)


## Cloud testing ##
SQLALCHEMY_DATABASE_URI = 'postgres://croqfcixiufmgv:f8caeaa60ed22208124855e753629d5439edd16d5a356481832e6db15ff2fa92@ec2-18-204-101-137.compute-1.amazonaws.com:5432/d76k1g0ggj8muo'
if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

## Local testing ##
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:CW72Ec#EdIHpoFsOGrtf@localhost/pennchats'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Jf_CSAx^ld192@localhost/pennchats'

# Cloud and local
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)



#####################################
######## Login Configuration ########flask
#####################################

login_manager.init_app(app)
login_manager.login_view = 'login'


##################################################
##### Register Blueprints for different pages#####
##################################################

from pennchatsproject.core.views import core
from pennchatsproject.students.views import students
from pennchatsproject.meetings.views import meetings
from pennchatsproject.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(students)
app.register_blueprint(meetings)
app.register_blueprint(error_pages)