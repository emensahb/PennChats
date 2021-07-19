# pennchatsproject/__init__.py
# this will hold a lot of our flask application logic and blueprint logic
# to be worked on between Audra, Efua and Jimmy

import os

import sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import psycopg2

login_manager = LoginManager()

app = Flask(__name__)

################################
######## Database Setup ########
################################
basedir = os.path.abspath(os.path.dirname(__file__))
#print(basedir)

# DATABASE_URL = os.environ['postgres://keecnygaavjarb:8edfaa4d280ecb61d741a959c94f9a9b0653181c3e3776efffcb1160e7b79a32@ec2-35-168-145-180.compute-1.amazonaws.com:5432/d7tnpd055lbiid']

# psycopg2.connect("dbname=d7tnpd055lbiid user=keecnygaavjarb host=ec2-35-168-145-180.compute-1.amazonaws.com password=8edfaa4d280ecb61d741a959c94f9a9b0653181c3e3776efffcb1160e7b79a32 port=5432")
# app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres://tgaklhtynkryrk:65d07c4409fc9e936b7d195279c1258b0cdfe78282fc445a2e4fcf2f6ef49356@ec2-54-83-82-187.compute-1.amazonaws.com:5432/d8sv9jdoccv88c'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres://glqxwvunhpxhng:c0204ac6aa93d5a3ee38d477a38776ad91cca092daf7261d02c4d828fbed19f1@ec2-23-23-164-251.compute-1.amazonaws.com:5432/dac2t4avknpb9t'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://keecnygaavjarb:8edfaa4d280ecb61d741a959c94f9a9b0653181c3e3776efffcb1160e7b79a32@ec2-35-168-145-180.compute-1.amazonaws.com:5432/d7tnpd055lbiid'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:CW72Ec#EdIHpoFsOGrtf@localhost/pennchats'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Jf_CSAx^ld192@localhost/pennchats'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


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
from pennchatsproject.students.views import students

app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(students)




