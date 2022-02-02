#!/usr/bin/python3
""" Module that starts a Flask web application """
from flask import Flask, escape, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_greeting():
    """Function that returns a greeting"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
