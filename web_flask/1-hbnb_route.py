#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes=False

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Returns a string at the root route"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """Returns a string at the root route"""
    return 'HBNB'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

