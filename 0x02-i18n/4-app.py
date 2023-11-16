#!/usr/bin/env python3
"""Flask app that implements babel library"""
from flask import Flask, render_template, request
from flask_babel import gettext, ngettext, Babel, get_locale

app = Flask(__name__)
babel = Babel(app)


class Config():
    """has languanges english and french"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    # BABEL_TRANSLATION_DIRECTORIES = 'translations'


app.config['BABEL_DEFAULT_LOCALE'] = 'en'


#@babel.localeselector
def get_locale():
    """determine the best match with our supported languages."""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    print(request.accept_languages)
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route("/", methods=["GET"], strict_slashes=False)
def hello_world():
    """renders templates"""
    locale = get_locale()
    return render_template('4-index.html', locale=locale)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
