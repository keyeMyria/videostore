from flask.ext.script import Manager

from flask_alembic.cli.script import manager as alembic_manager
from videostore import create_app, environments

#  models, scripts, services)

# from videostore.db import db, factories
# from videostore.settings import constants

if __name__ == '__main__':
    manager = Manager(create_app)

    manager.add_command('db', alembic_manager)

    manager.add_option(
        '-e', '--environment',
        default='development',
        choices=environments.keys(),
        dest='config_environment',
        required=False,
    )

    # Add some more stuff to manager shell so we don't need to import that
    # manually every time
    # @manager.shell
    # def make_shell_context():
    #     context = dict(app=create_app, db=db)
    #     context.update(vars(constants))
    #     context.update(vars(models))
    #     context.update(vars(factories))
    #     context.update(vars(helpers))
    #     return context

    manager.run()
