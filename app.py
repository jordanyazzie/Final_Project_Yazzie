from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')




@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'YouAre' or request.form['password'] != 'Awesome':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error=error)




# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# @app.route('/mystery')
# def mystery():
#     return render_template('mystery.html')
#


if __name__ == '__main__':
    app.run(debug=True)