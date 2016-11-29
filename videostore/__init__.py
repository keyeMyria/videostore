from flask import Flask
from .settings import environments


def create_app(config_environment):
    app = Flask('videostore')

    config_object = environments[config_environment]()
    app.config.from_object(config_object)

    return app
