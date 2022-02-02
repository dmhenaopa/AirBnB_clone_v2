#!/usr/bin/python3
""" Module that starts a Flask web application """
from flask import Flask, escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_greeting():
    """Function that returns a greeting"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_name():
    """Function that returns name of console"""
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def display_c_text(text):
    """Function that returns text variable"""
    return 'C {}'.format(escape(text.replace('_', ' ')))


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def display_python_text(text):
    """Function that returns text variable"""
    return 'Python {}'.format(escape(text.replace('_', ' ')))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
