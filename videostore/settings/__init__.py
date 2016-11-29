from unipath import Path
import os


class ConfigBase:
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
    # Flask-Alembic config
    # --------------------------------------------------------------------------
    ALEMBIC = {
        'script_location': APPLICATION_PACKAGE_ROOT.child('db').child('migrations')
    }


class Test(ConfigBase):
    SQLALCHEMY_DATABASE_URI = "postgresql://videostore:videostore@localhost:5432/videostore_test"


class Development(ConfigBase):
    SQLALCHEMY_DATABASE_URI = "postgresql://videostore:videostore@localhost:5432/videostore_dev"


class Production(ConfigBase):
    SQLALCHEMY_DATABASE_URI = "postgresql://videostore:videostore@localhost:5432/videostore"


environments = {
    'test': Test,
    'development': Development,
    'production': Production,
}
