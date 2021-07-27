# pennchatsproject/core/views.py
# includes routing code for two views (homepage view and the about us view)
# Audra's main.py line 7-10 (Audra)

import jinja2
from flask import render_template, Blueprint
from pennchatsproject.models import TimeOption


core = Blueprint('core', __name__)


# home page
@core.route('/')
def index():
    # more to come
    return render_template("index.html")


# about us page
@core.route('/info')
def info():
    return render_template('info.html')


@jinja2.contextfilter
@core.app_template_filter()
def query_time(context, time_id):
    time = TimeOption.query.get(time_id)
    return time.time_option
