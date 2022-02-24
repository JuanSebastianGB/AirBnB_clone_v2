#!/usr/bin/python3
"""
Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Defining Index route
    """
    return 'Hello HBNB!'


@app.route('/airbnb-onepage', strict_slashes=False)
def onepage():
    """
    Defining one-route
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
