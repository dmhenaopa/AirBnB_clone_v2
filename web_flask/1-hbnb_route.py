#!/usr/bin/python3
""" Module that starts a Flask web application """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_greeting():
    """Function that returns a greeting"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_name():
    """Function that returns name of console"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
