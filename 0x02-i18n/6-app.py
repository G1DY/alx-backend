#!/usr/bin/env python3
"""Flask app that implements Babel translations"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union
from os import getenv

app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """has languanges english and french"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object("5-app.Config")


@app.before_request
def before_request():
    """find a user if any, and set it as a global on flask.g.user"""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """determine the best match with our supported languages."""
    locale = request.args.get("locale", "").strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", methods=["GET"], strict_slashes=False)
def hello_world() -> str:
    """renders templates"""
    return render_template("5-index.html")


def get_user() -> Union[dict, None]:
    """Returns a user dictionary"""
    if request.args.get("login_as"):
        user = int(request.args.get("login_as"))
        if user in users:
            return users.get(user)
    else:
        return None


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
