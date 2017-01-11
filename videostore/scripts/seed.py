from flask import current_app
from flask.ext.script import Command

from ..db import db, factories


class Seed(Command):
    """Seeds database with fake but realistic data"""

    def run(self):
        current_app.logger.info('Seeding database with test data...')

        test_user = factories.UserFactory(**factories.test_user_params())
        test_admin = factories.UserFactory(**factories.test_admin_user_params())
        test_user.password = test_admin.password = 'test'
        db.session.add(test_user)
        db.session.add(test_admin)

        categories = [
            factories.CategoryFactory(name='Action'),
            factories.CategoryFactory(name='SciFi'),
            factories.CategoryFactory(name='Horror')
        ]

        for category in categories:
            db.session.add(category)
            for i in range(1, 10):
                db.session.add(
                    factories.MovieFactory(category=category)
                )

        db.session.commit()
