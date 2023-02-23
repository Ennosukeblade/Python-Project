from speedyserv import app
from flask import render_template

@app.route('/')
def dashboard():
    return render_template("index.html")

@app.route('/tables')
def tables():
    return render_template("tables.html")

@app.route('/tables/new')
def new_table():
    return render_template("add_table.html")

@app.route('/tables/order')
def table_order():
    return render_template("table_order.html")