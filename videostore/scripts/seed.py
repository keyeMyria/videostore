from flask import current_app
from flask.ext.script import Command

from ..db import db, factories
from ..models import User


class Seed(Command):
    """Seeds database with fake but realistic data"""

    def run(self):
        current_app.logger.info('Seeding database with test data...')

        admin_role = factories.RoleFactory(name="admin")
        user_role = factories.RoleFactory(name="user")

        test_admin = factories.UserFactory(
            role=admin_role, **factories.test_admin_user_params()
        )
        test_user = factories.UserFactory(
            role=user_role, **factories.test_user_params()
        )
        test_user.password = test_admin.password = 'test'

        db.session.add(admin_role)
        db.session.add(user_role)
        db.session.add(test_user)
        db.session.add(test_admin)

        for i in range(1, 10):
            db.session.add(factories.UserFactory(role=user_role))

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

        for user in User.query:
            db.session.add(factories.UserDetailFactory(user=user))

        db.session.commit()
