#!/usr/bin/python3
"""
Start Flask web application
"""
from models import storage
from flask import Flask
from flask import render_template
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Rendering template to show states list """
    return render_template('7-states_list.html',
                           states=storage.all('State'))


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Rendering template to show cities list by states  """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_session(exc):
    """Remove the current session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
