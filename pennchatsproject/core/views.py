# pennchatsproject/core/views.py
# includes routing code for two views (homepage view and the about us view)
# Audra's main.py line 7-10 (Audra)

from flask import render_template, request, Blueprint

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
