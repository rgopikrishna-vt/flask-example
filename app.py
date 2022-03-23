from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return "welcome to the index page"


@app.route("/hi/")
def who():
    return "Who are you?"


@app.route("/hi/<username>")
def greet(username):
    return f"Hi there, {username}!"
