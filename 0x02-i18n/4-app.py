#!/usr/bin/env python3
"""Flask app that implements babel library"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """has languanges english and french"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_TRANSLATION_DIRECTORIES = "translations"


app = Flask(__name__)
app.config.from_object(Config)


babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """determine the best match with our supported languages."""
    locale = request.args.get("locale", "").split()
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", methods=["GET"], strict_slashes=False)
def hello_world() -> str:
    """renders templates"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
