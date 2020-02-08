from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "HELLO WORLD"

@app.route('/test')
def hello():
    return "HELLOOOOOOO WORLD"
