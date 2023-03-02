from speedyserv import app
from flask import render_template, request, session, redirect
from speedyserv.models import meal_model, category_model, table_model

@app.route('/menu/<int:id>')
def meals_by_category(id):
    data = {'id': id}
    category_meals = category_model.Category.get_category_with_meals(data)
    #print(category)
    return render_template("category_meals.html", category_meals = category_meals)

@app.route('/menu')
def menu():
    categories = category_model.Category.get_all_categories()
    meals = meal_model.Meal.get_all_meals()
    return render_template("menu.html", categories = categories, meals = meals)

@app.route('/menu/order/add', methods=['post'])
def order():
    data = request.form
    pass
    
@app.route('/session', methods=['post'])
def table_session():
    id = request.form
    session['table_id'] = id['id']
    data = {
        **request.form,
        'status': 1    
        }
    table_model.Table.update_table_status(data)
    return redirect('/menu')


