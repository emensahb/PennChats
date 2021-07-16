# pennchatsproject/students/views.py
# contains routing code for eight views
# register, login, logout, sign-up for next week's chat, thank you, account, edit profile, <username> profile page
# from Audra's main.py file lines 12-44

# register
# dummy signup page
@app.route('/register', methods=["POST", "GET"])
def signup():
    form = SignUpForm()
    return render_template("register.html", form = form)

# login
# dummy login page
@app.route('/login', methods=["POST", "GET"])
def login():
    form = SignUpForm()
    return render_template("login.html", form = form)

# logout
@app.route('/logout')
def logout():
    return 'You are now logged out. Come back soon!'


# sign up-for next week's chat
@app.route('/next_week')
def next_week():
    form = SignUpForm()
    return render_template("next_week.html", form = form)

# thank you
@app.route('/thank_you')
def thank_you():
    return 'Thanks for signing up!'

# account
@app.route('/account')
def member_area():
    return render_template("account.html")

#create profile
@app.route('create_profile')
def create_profile():

    return render_template('create_profile')

# edit profile
@app.route('/account/<name>')
def edit_profile(name):
    return 'edit profile'

# <username> profile page
@app.route("/name/<name>")
def get_user_name(name):
    return render_template("get_user_name.html", name = name)