from speedyserv import app
from flask import render_template

from speedyserv.models import category_model
from speedyserv.models import meal_model

@app.route('/meals')
def meals():
    meals = meal_model.Meal.get_all_meals()
    return render_template("meals.html", meals = meals)

@app.route('/meals/new')
def new_meal():
    return render_template("add_meal.html")