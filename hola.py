from flask import Flask, render_template

# instance of flask class
# __name__ tells flask which module it is running from
app = Flask(__name__)

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
