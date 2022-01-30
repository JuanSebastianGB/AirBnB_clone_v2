#!/usr/bin/python3
"""
Start Flask web application
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """ Rendering a list of all the states """
    return render_template('9-states.html', states=storage.all('State'))


@app.route('/states/<id>', strict_slashes=False)
def state(id):
    """ Rendering template to show a state"""
    states = storage.all('State').values()
    for single_state in states:
        if single_state.id == id:
            return render_template('9-states.html', single_state=single_state)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown(exc):
    """Remove the current session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
