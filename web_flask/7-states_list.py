#!/usr/bin/python3
"""
Stars Flask web application
"""
from flask import Flask, render_template
from models import storage
""" from models import storage """
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Rendering template to show states list """
    return render_template('7-states_list.html', states=storage.all('State'))


@app.teardown_appcontext
def teardown(exc):
    """Remove the current session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
