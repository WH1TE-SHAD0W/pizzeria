import os

from flask import Flask, render_template, request, redirect, url_for
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app', 'templates')

app = Flask(__name__, template_folder=template_dir)

# Sample data
pizzas = [
    {'id': 1, 'name': 'Margherita'},
    {'id': 2, 'name': 'Pepperoni'},
    {'id': 3, 'name': 'Hawaiian'}
]

orders = [
    {'id': 1, 'date': '2023-10-01', 'total': 20.00},
    {'id': 2, 'date': '2023-10-02', 'total': 15.50}
]

@app.route('/')
def index():
    return render_template('index.html.j2')

@app.route('/my-orders')
def my_orders():
    return render_template('history.html.j2', orders=orders)

@app.route('/create-order', methods=['GET', 'POST'])
def create_order():
    if request.method == 'POST':
        # Handle order creation logic here
        return redirect(url_for('my_orders'))
    return render_template('create.html.j2', pizzas=pizzas)

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