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
def pythonisFun(text):
    """returns Python + text if text else is cool"""
    Text = text if text else Text = "is_cool"
    return 'python' + text.replace('_', ' ')

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """returns n is a number if n is int"""
    return "{:d} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def numandtemplate(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
    """display html page only if n is int"""
    if n % 2 == 0:
        evenness = 'even'
    else:
        evenness = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           evenness=evenness)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
