#!/usr/bin/python3
"""
flask application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ Defining index route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Defining hbnb route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Defining c route with an input"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """ Defining python with an optional input """
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
