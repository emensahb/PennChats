# pennchatsproject/__init__.py
# this will hold a lot of our flask application logic and blueprint logic
# to be worked on between Audra, Efua and Jimmy

import os
from flask import Flask,render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


# from students.forms import *
# from app import db
from config import Config
from models import *

app = Flask(__name__)

################################
######## Database Setup ########
################################
# Naming convention: Table and class names camel case. Field names with the dashes
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:pbNdO#cdxtskP7Da9d7@@localhost/pennchats'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


#####################################
######## Login Configuration ########
#####################################








##################################################
##### Register Blueprints for different pages#####
##################################################
