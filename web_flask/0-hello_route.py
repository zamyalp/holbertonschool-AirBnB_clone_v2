#!/usr/bin/python3
<<<<<<< HEAD
"""Starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Returns a string at the root route"""
    return 'Hello HBNB!'

if __name__ == '__main__':
=======
"""this will start a flask web application tuned
to 0.0.0.0, port 5000"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """this displays "hello hbnb"""
    return "Hello HBNB!"


if __name__ == "__main__":
>>>>>>> 7b13fa883303f4b45ec1f248ea9606bc13e0b01a
    app.run(host="0.0.0.0")
