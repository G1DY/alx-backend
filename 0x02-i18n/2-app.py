#!/usr/bin/env python3
"""Flask app that implements babel library"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config():
    """has languanges english and french"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)
app.url_map.strict_slashes = False


@app.route("/", methods=["GET"], strict_slashes=False)
def hello_world():
    """renders templates"""
    return render_template("1-index.html")


@babel.localeselector
def get_locale():
    """determine the best match with our supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
