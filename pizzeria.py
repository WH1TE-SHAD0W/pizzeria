import os
from tokenize import Token
from venv import logger

from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from app.models.order import Order
from app.models.pizza import Pizza
from database.migration import engine

template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app', 'templates')

app = Flask(__name__, template_folder=template_dir)
app.secret_key = Token  # Set a secret key for session management

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

Session = sessionmaker(bind=engine)
session = Session()

@app.route('/')
def index():
    return render_template('index.html.j2')

@app.route('/my-orders')
def my_orders():
    orders = session.query(Order).all()
    orders_with_pizzas = []
    for order in orders:
        pizzas = session.query(Pizza).filter_by(order_id=order.order_id).all()
        orders_with_pizzas.append({'order': order, 'pizzas': pizzas})

    return render_template('history.html.j2', orders_with_pizzas=orders_with_pizzas)

@app.route('/create-order-pizza', methods=['GET', 'POST'])
def create_order_pizza():
    if request.method == 'POST':
        highest_order_id = session.query(func.max(Order.order_id)).scalar()
        if highest_order_id is None:
            highest_order_id = 1
        order = Order(highest_order_id + 1)
        session.add(order)
        # Extract data from the request
        name = request.form['pizza']
        pizza = Pizza(order.order_id, name, size='Medium', price=10.00)
        session.add(pizza)
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
        try: session.commit()
        except Exception as e:
            logger.error(e)
            session.rollback()
        finally:
            session.close()
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