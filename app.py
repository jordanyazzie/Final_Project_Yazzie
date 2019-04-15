from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

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
    return render_template('eatOutHealthy.html')

@app.route('/eatOutSplurge')
def eosplurge():
    return render_template('eatOutSplurge.html')

@app.route('/homeSplurge')
def homesplurge():
    return render_template('homeSplurge.html')

@app.route('/homeHealthy')
def homehealthy():
    return render_template('homeHealthy.html')






if __name__ == '__main__':
    app.run(debug=True)


# venv\Scripts\activate