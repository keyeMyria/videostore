import configparser
import os

from unipath import Path


class ImproperlyConfiguredError(RuntimeError):
    pass


class ConfigBase:
    APPLICATION_NAME = 'videostore'

    # --------------------------------------------------------------------------
    # Application directories
    # --------------------------------------------------------------------------
    APPLICATION_PACKAGE_ROOT = Path(os.path.dirname(os.path.realpath(__file__))).ancestor(1)
    APPLICATION_REPO_ROOT = APPLICATION_PACKAGE_ROOT.ancestor(1)

    # Where wsgi.py is found
    APPLICATION_PACKAGE_ROOT = APPLICATION_PACKAGE_ROOT
    # Where manage.py is found
    APPLICATION_REPO_ROOT = APPLICATION_REPO_ROOT
    # Directory for logs if local logging is configured
    LOGS_ROOT = APPLICATION_REPO_ROOT.child('log')
    # Temporary directories
    TEMP_ROOT = APPLICATION_REPO_ROOT.child('tmp')
    CACHE_ROOT = TEMP_ROOT.child('cache')

    # --------------------------------------------------------------------------
    # Flask config
    # --------------------------------------------------------------------------
    SECRET_KEY = None

    # --------------------------------------------------------------------------
    # Flask-Alembic config
    # --------------------------------------------------------------------------
    ALEMBIC = {
        'script_location': APPLICATION_PACKAGE_ROOT.child('db').child('migrations')
    }

    # --------------------------------------------------------------------------
    # Flask-SQWLAlchemy config
    # --------------------------------------------------------------------------
    SQLALCHEMY_DATABASE_URI = None

    def read_config_file(self):
        config_parser = configparser.ConfigParser()
        if not config_parser.read(self.config_files):
            raise ImproperlyConfiguredError('No config file found')

        section = config_parser['Flask']
        self.SECRET_KEY = section.get('secret_key', fallback='')

        section = config_parser['Database']
        self.SQLALCHEMY_DATABASE_URI = section.get(
            'sqlalchemy_uri', fallback=''
        )

    def validate(self):
        errors = dict()

        if not self.SQLALCHEMY_DATABASE_URI:
            errors['SQLALCHEMY_DATABASE_URI'] = "Can't be blank"

        if errors:
            raise ImproperlyConfiguredError(errors)

    def init_app(self, app):
        if app:
            self.read_config_file()
            self.validate()
            app.config.from_object(self)
