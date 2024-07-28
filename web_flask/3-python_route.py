#!/usr/bin/python3
"""
    starts a flask webapplication
"""

from flask import Flask
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def index():
    """returns Hello HBNB"""
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """returns C + text"""
    return 'C' + text.replace('_', ' ')


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonisFun(text='is_cool'):
    """returns Python + text if text else is cool"""
    return 'Python' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
