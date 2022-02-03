#!/usr/bin/python3
""" Module that starts a Flask web application """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def remove_session(self):
    """Function that remove the current SQLALchemy
       Session
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def display_():
    """Function that display a html page"""
    states = storage.all('State').values()
    return render_template('7-states_list.html',
                           states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
