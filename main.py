from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def penn_chats():
    return render_template('index.html', quote='You are on the home page')

@app.route('/profile')
def profile():
    return render_template('index.html', quote='This is the landing page for all profiles')

@app.route('/profile/jimmy')
def profile_jimmy():
    return render_template('index.html', quote='This is the profile page for Jimmy')


if __name__ == '__main__':
    app.run()

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
