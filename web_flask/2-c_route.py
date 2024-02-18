#!/usr/bin/python3
"""Flask On host 0.0.0.0 and port 5000"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays "Hello HBNB!" on the root path"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays "HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Display C followed by the value of text"""
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
