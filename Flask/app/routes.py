from app import app
from flask import render_template

# that html file will open if after eg. 
# www.google.com there is '/' or '/index'


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/helloworld')
def sample():
    return '<h1>Hello World!</h1>'