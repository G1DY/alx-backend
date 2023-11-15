#!/usr/bin/env python3
"""Basic Flask App"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)

babel = Babel(app)


class Config:
    """has languanges english and french"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object("1-app.Config")


@app.route("/", methods=["GET"], strict_slashes=False)
def hello_world():
    """renders templates"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
