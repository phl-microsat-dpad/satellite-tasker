from imagery_request import app
from imagery_request import models
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/orders')
def list():
    return render_template('orders.html')


@app.route('/orders/<int:order_id>')
def view(order_id):
    results = models.Order.query.get(order_id)
    print results.serialize
    return render_template('view.html', data=results.serialize)


@app.route('/thanks')
def thanks():
    return "Success!"
