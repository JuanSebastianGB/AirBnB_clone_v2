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


@app.route('/', strict_slashes=False)
def hbnb():
    """ Defining hbnb route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Defining c route with an input"""
    return 'C {}'.format(text.replace('_', ' '))


app.run(host='0.0.0.0', port='5000')
