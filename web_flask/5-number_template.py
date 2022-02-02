#!/usr/bin/python3
""" Module that starts a Flask web application """
from flask import Flask, escape, render_template


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


@app.route('/number/<int:number>', strict_slashes=False)
def display_number(number):
    """Function that returns a number"""
    return '{} is a number'.format(escape(number))


@app.route('/number_template/<int:number>', strict_slashes=False)
def display_html_number(number):
    """Function that display a html page"""
    return render_template('5-number.html', number=number)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
