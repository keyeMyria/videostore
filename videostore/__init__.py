from flask import Flask
from .settings import environments
from .db import db
from flask_alembic import Alembic

from .models import *


def create_app(config_environment):
    app = Flask('videostore')

    config_object = environments[config_environment]()
    app.config.from_object(config_object)

    db.init_app(app)

    # Initialize flask-alembic
    alembic = Alembic()
    alembic.init_app(app)

    return app
