from speedyserv import app
from flask import render_template

@app.route('/categories')
def categroies():
    return render_template("category.html")