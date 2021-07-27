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
SQLALCHEMY_DATABASE_URI = 'postgres://keecnygaavjarb:8edfaa4d280ecb61d741a959c94f9a9b0653181c3e3776efffcb1160e7b79a32@ec2-35-168-145-180.compute-1.amazonaws.com:5432/d7tnpd055lbiid?sslmode=require'
if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

## Local testing ##
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:CW72Ec#EdIHpoFsOGrtf@localhost/pennchats'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Jf_CSAx^ld192@localhost/pennchats'

# Cloud and local
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
from pennchatsproject.students.views import students
from pennchatsproject.meetings.views import meetings
from pennchatsproject.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(students)
app.register_blueprint(meetings)
app.register_blueprint(error_pages)