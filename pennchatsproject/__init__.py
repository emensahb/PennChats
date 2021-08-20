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


## Cloud testing 8/19##
SQLALCHEMY_DATABASE_URI = 'postgres://ssldqbppegmblq:9287ee9524c32eaeac5ad6d7dfbd7eae744fe8c1d6f7822ef77f9d6c84dbdcc3@ec2-54-159-35-35.compute-1.amazonaws.com:5432/'
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