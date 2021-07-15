# pennchatsproject/__init__.py
# this will hold a lot of our flask application logic and blueprint logic
# to be worked on between Audra, Efua and Jimmy

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

################################
######## Database Setup ########
################################








#####################################
######## Login Configuration ########
#####################################








##################################################
##### Register Blueprints for different pages#####
##################################################

from pennchatsproject.core.views import core
from pennchatsproject.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(error_pages)
