#!/usr/bin/env python3
""" a basic flask app for Parametrize templates
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)


class Config(object):
    """ Config class for Babel object
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def hello():
    """ render a basic html file for test
    """
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """
    a function to determine the best match with the supported
    languages
    Use the _ or gettext function to parametrize your templates.
    Use the message IDs home_title and home_header.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])
    '''return Babel(app, locale_select=get_locale)'''


if __name__ == '__main__':
    app.run()
