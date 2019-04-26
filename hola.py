from flask import (
    Flask, 
    render_template, 
    request, 
    redirect, 
    url_for,
    make_response,
    session
)
# instance of flask class
# __name__ tells flask which module it is running from
app = Flask(__name__)

# app.secret_key = 'shhhh_this_is_a_secret'
# but really you should get your secret from the settings file
app.config.from_pyfile('settings.py')

# a better way to get a secret:
# $ python -c 'import os; print(os.urandom(16))'

# this is a decorator
@app.route('/')
def index():
    # render_template looks to templates directory for page to return
    return render_template('index.html')

# this is another route
# it's got an url param
@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', t_name=name)

# param types can be specified
# note that return types are limited
@app.route('/add/<int:addend1>/<int:addend2>')
def add(addend1, addend2):
    return str(addend1 + addend2)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        # return f'FirstName: { first_name }, Last Name: { last_name }'
        # return redirect(url_for('registered'))
        # response = make_response(redirect(url_for('registered')))
        # response.set_cookie('first_name', first_name)
        # return response
        session['first_name'] = first_name
        return redirect(url_for('registered'))
    return render_template('form.html')

@app.route('/thank_you')
def registered():
    first_name = session.get('first_name')
    return f'Thank You, {first_name}'
