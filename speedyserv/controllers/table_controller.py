from speedyserv import app
from flask import render_template

@app.route('/')
def dashboard():
    return render_template("index.html")
@app.route('/tables')
def tables():
    return render_template("tables.html")