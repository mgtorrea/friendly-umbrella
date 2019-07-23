from flask import Flask
import calculations
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World_again! {} from commit: {}'.format(calculations.inc(2), os.env["COMMIT_ID"])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')