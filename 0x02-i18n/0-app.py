#!/usr/bin/env python3
"""Flask app that implements babel"""
from flask_babel import Babel
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world():
    """outputs welcome to holberton"""
    return render_template('0-app.py')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')