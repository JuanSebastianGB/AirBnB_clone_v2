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
    """ Defining c route with and input """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/Python', strict_slashes=False)
@app.route('/Python/<text>', strict_slashes=False)
def pthon(text='is cool'):
    """ Defining python route with an optional input"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Defining number route with int conditional """
    if type(n) is int:
        return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
