from speedyserv import app
from flask import render_template

@app.route('/meals')
def meals():
    return render_template("meals.html")