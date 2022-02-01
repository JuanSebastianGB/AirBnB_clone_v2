#!/us/bin/python3
"""
Starting Flask application
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ Implmenting filter """
    states = storage.all('State')
    amenities = storage.all('Amenity')
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
