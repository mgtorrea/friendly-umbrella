from flask import Flask
import calculations
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World_again! {}'.format(calculations.inc(2))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')