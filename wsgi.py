# My first Flask web server
from flask import Flask, url_for, request, \
render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return "Index Page"

@app.route("/login_no_cred", methods=['GET','POST'])
def login_no_cred():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


def do_the_login():
    return "login procedure start..."

def show_the_login_form():
    return "login form:"



@app.route("/login", methods=['POST', 'GET'])
def login():
    error = None
    args = request.args.get("foo") + request.args.get("bar")
    if request.method == 'POST':
        if valid_login(request.form['username'],
        request.form['password']):
            return render_template('login.html', username = request.form['username'] + args)
        else:
            error = "Invalid username/password"

    return render_template('login.html', username = "BAD BOY NOT LOGGED or GET REQUEST. I KNOW YOU!" + args)

def log_the_user_in(username=None):
    if not username:
        raise ValueError("No username field in http request data form!")
    else:
        return      

def valid_login(username,password):
    if username == "user" and password == "pwd":
        return True
    else:
        return False



@app.route('/hello/')
@app.route("/hello/<name>")
def hello(name=None):
    return render_template('hello.html', person=name)