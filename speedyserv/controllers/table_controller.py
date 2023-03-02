from speedyserv import app
from flask import render_template, session, redirect, request

from speedyserv.models import table_model

@app.route('/')
def dashboard():
    if 'user_id' not in session:
        return redirect('/signin')
    return render_template("index.html")

@app.route('/tables')
def tables():
    if 'user_id' not in session:
        return redirect('/signin')
    tables = table_model.Table.get_all_tables()
    table_model.Table.get_meals_with_table_id({'id':1})
    return render_template("tables.html", tables = tables)

@app.route('/tables/new')
def new_table_page():
    if 'user_id' not in session:
        return redirect('/signin')
    return render_template("add_table.html")

@app.route('/tables/add', methods=['post'])
def add_table():
    data = request.form
    table_model.Table.add_table(data)
    return redirect('/tables')

@app.route('/tables/order')
def table_order():
    if 'user_id' not in session:
        return redirect('/signin')
    return render_template("table_order.html")