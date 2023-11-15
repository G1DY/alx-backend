#!/usr/bin/env python3
"""Flask app that implements babel library"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config():
    """has languanges english and french"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


# @babel.localeselector
def get_locale():
    """determine the best match with our supported languages."""
    print(request.accept_languages)
    return request.accept_languages.best_match(app.Config['LANGUAGES'])


babel.init_app(app)


@app.route("/", methods=["GET"], strict_slashes=False)
def hello_world():
    """renders templates"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
