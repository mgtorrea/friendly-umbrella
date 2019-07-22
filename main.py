from flask import Flask
import calculations
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! {}'.format(calculations.inc(2))