# My first Flask web server
from flask import Flask, url_for, request, \
render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return "Index Page"

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

def do_the_login():
    return "login procedure start..."

def show_the_login_form():
    return "login form:"


@app.route('/hello/')
@app.route("/hello/<name>")
def hello(name=None):
    return render_template('hello.html', person=name)