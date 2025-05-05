# My first Flask web server
from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import request

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

# @app.get('/login')
# def login_get():
#     return show_the_login_form()

# @app.post('/login')
# def login_post():
#     return do_the_login()


def do_the_login():
    return "login procedure start..."

def show_the_login_form():
    return "login form:"