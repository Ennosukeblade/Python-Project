from speedyserv import app
from flask import render_template, request, redirect
from speedyserv.models import category_model

@app.route('/categories')
def categories():
    categories = category_model.Category.get_all_categories()
    return render_template("category.html", categories = categories)

@app.route('/categories/new')
def new_category():
    return render_template("add_category.html")

@app.route('/categories/add', methods=['POST'])
def add_category():
    data = request.form
    category_model.Category.add_category(data)
    return redirect('/categories')
