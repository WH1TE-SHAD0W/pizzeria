import os
from venv import logger

from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy.orm import sessionmaker
from app.models.pizza import Pizza
from database.migration import engine

template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app', 'templates')

app = Flask(__name__, template_folder=template_dir)

Session = sessionmaker(bind=engine)
session = Session()

@app.route('/')
def index():
    return render_template('index.html.j2')

@app.route('/my-orders')
def my_orders():
    return render_template('history.html.j2')

@app.route('/create-order-pizza', methods=['GET', 'POST'])
def create_order_pizza():
    if request.method == 'POST':
        # Extract data from the request
        name = request.form['pizza']
        pizza = Pizza(name, size='Medium', price=10.00)
        session.add(pizza)
        session.commit()
        return redirect(url_for('create_order_side'))
    return render_template('create/pizza.html.j2')

@app.route('/create-order-side', methods=['GET', 'POST'])
def create_order_side():
    if request.method == 'POST':
        # Handle order creation logic here
        return redirect(url_for('create_order_drink'))
    return render_template('create/side.html.j2')

@app.route('/create-order-drink', methods=['GET', 'POST'])
def create_order_drink():
    if request.method == 'POST':
        # Handle order creation logic here
        return redirect(url_for('create_order_dessert'))
    return render_template('create/drink.html.j2')

@app.route('/create-order-dessert', methods=['GET', 'POST'])
def create_order_dessert():
    if request.method == 'POST':
        # Handle order creation logic here
        return redirect(url_for('my_orders'))
    return render_template('create/dessert.html.j2')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        return redirect(url_for('index'))
    return render_template('login.html.j2')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle registration logic here
        return redirect(url_for('index'))
    return render_template('register.html.j2')


app.run(debug=True, host="0.0.0.0", port=3000)