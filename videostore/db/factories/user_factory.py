from factory import LazyAttribute, RelatedFactory, Sequence, SubFactory

from ...models import User
from .base_factory import BaseFactory, fake


class UserFactory(BaseFactory):
    class Meta:
        model = User

    username = LazyAttribute(lambda x: fake.user_name())
    email = LazyAttribute(lambda x: fake.email())
    password = LazyAttribute(lambda x: fake.password())


def test_user_params():
    return dict(
        username='test', email='test@test.local.com',
        role=User.ROLES['user'], status=User.STATUSES['active']
    )


def test_admin_user_params():
    return dict(
        username='test_admin', email='test_admin@test.local.com',
        role=User.ROLES['admin'], status=User.STATUSES['active']
    )
