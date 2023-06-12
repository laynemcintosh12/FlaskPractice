from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return "<h1>Welcome!</h1>"

@app.route('/welcome/home')
def home():
    return "<p>Welcome to the Home Screen!</p>"

@app.route('/welcome/back')
def back():
    return "<p>Welcome Back!</p>"