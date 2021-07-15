# pennchatsproject/core/views.py
# includes routing code for two views (homepage view and the about us view)
# Audra's main.py line 7-10 (Audra)

# home page
@app.route('/')
def penn_chats():
    return render_template("index.html")