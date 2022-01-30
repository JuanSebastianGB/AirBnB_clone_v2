#!/usr/bin/python3
"""
Start Flask web application
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Rendering template to show states list """
    return render_template('8-cities_by_states.html', states=storage.all('State'))


@app.teardown_appcontext
def teardown(exc):
    """Remove the current session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
