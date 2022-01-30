#!/us/bin/python3
"""
Starting Flask application
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Showing full hbnb web page """
    states = storage.all('State')
    amenities = storage.all('Amenity')
    places = storage.all('Place')
    return render_template('100-hbnb.html', states=states, amenities=amenities,
                           places=places)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
