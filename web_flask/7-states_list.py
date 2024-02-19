#!/usr/bin/python3
"""using flask to list the list of states"""
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Display the list of states"""
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exc):
    """close the current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
