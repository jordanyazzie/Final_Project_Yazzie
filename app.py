from flask import Flask, render_template, redirect, url_for, request
import random

app = Flask(__name__)

eatout_healthy = ['Zupas', 'Chipotle', 'Panera Bread', 'Jamba Juice']
eatout_splurge = ['KFC', 'Cheesecake Factory', 'Betos', 'Dominos', 'Wendys', 'Taco Bell', 'McDonalds', 'Olive Garden']
home_healthy_main = ['Grilled Chicken', 'Steak', 'Salmon', ' Grilled Tofu', 'Chicken Noodle Soup', 'Veggie Burger', 'Fresh Mozzeralla']
home_healthy_side = ['Steamed Broccoli', 'Sliced Apples', 'Kale Chips', 'Grilled Carrots', 'Sweet Potato Fries', 'Green Beans', 'Orange Slices']
home_splurge_main = ['Ben and Jerrys', 'Fried Chicken', 'Mac N Cheese', 'Lasagna', 'Friend Pork Chops', 'Cheesy Potatoes', 'Cake']
home_splurge_side = ['Cookie Dough', 'Doritos', 'Baked Beans', 'Buttery White Bread', 'Potato Salad', 'Macaroni Salad', 'Fried Rice', 'Hush Puppies']


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'YouAre' or request.form['password'] != 'Awesome':
            error = 'Invalid Credentials. Hint, Look at the hint!'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/EatOut')
def eatout():
    return render_template('EatOut.html')

@app.route('/StayHome')
def stayhome():
    return render_template('StayHome.html')

@app.route('/eatOutHealthy')
def eohealthy():
    suggestion = random.choice(eatout_healthy)
    return render_template('eatOutHealthy.html', suggestion=suggestion)

@app.route('/eatOutSplurge')
def eosplurge():
    suggestion = random.choice(eatout_splurge)
    return render_template('eatOutSplurge.html', suggestion=suggestion)

@app.route('/homeSplurge')
def homesplurge():
    suggestionmain = random.choice(home_splurge_main)
    suggestionside = random.choice(home_splurge_side)
    return render_template('homeSplurge.html', suggestionmain=suggestionmain, suggestionside=suggestionside)

@app.route('/homeHealthy')
def homehealthy():
    suggestionmain = random.choice(home_healthy_main)
    suggestionside = random.choice(home_healthy_side)
    return render_template('homeHealthy.html', suggestionmain=suggestionmain, suggestionside=suggestionside)


if __name__ == '__main__':
    app.run(debug=True)


# venv\Scripts\activate