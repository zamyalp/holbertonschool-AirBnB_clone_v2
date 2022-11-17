#!/usr/bin/python3
"""Starts a Flask web application"""


from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Returns a string at the root route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """Returns a string at the root route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hbnb_2(text):
    """ Function that displays C followed by the value of the text"""
    return ("C {}".format(text.replace("_", " ")))


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def hbnb_3(text):
    """ Function that displays python """
    return ("Python {}".format(text.replace("_", " ")))


@app.route('/number/<int:n>', strict_slashes=False)
def hbnb_4(n):
    """ Function that shows n is a number """
    return ("{} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def show_page(n):
    """ this will display an html page """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
