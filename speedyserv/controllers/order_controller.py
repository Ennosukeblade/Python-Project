from speedyserv import app
from flask import render_template, request, session, redirect
from speedyserv.models import order_model

@app.route('/order/meal', methods=['POST'])
def add_meal_to_order():
    data = {
            **request.form,
            'table_id': session['table_id']
            }

    # create order with the table_id
    order_model.Order.create_order(data)
    # get the meal_id from add to card in menu "request.form"
    # and add the order_id
    # data = {
    #     **request.form,
    #     'order_id': order_id
    # }
    #order_meal_model.OrderMeal.create_order_meal(data)
    return redirect("/menu")
