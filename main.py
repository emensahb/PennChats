from flask import Flask, render_template
from forms import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'

# home page
@app.route('/')
def penn_chats():
    return render_template("home.html")

# example profile page
@app.route('/profile')
def test_profile():
    return 'Profile goes here'

# example login (registered user main screen) page
@app.route('/login')
def test_login():
    return 'Login'

# example signup page
@app.route('/signup', methods=["POST", "GET"])
def test_signup():
    form = SignUpForm()
    return render_template("signup.html", form = form)


@app.route("/name/<name>")
def get_user_name(name):
    return "name : {}".format(name)

if __name__ == '__main__':
    app.run()

# check pull request - Audra

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
 #   print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
 #   print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
