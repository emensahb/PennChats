
# app.py
# to be called to run the __init__.py file under pennchatsproject
# and start server for web app

from pennchatsproject import app

if __name__ == '__main__':
    app.run(debug=True)
