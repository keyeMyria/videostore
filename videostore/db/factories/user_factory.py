from factory import LazyAttribute, RelatedFactory, Sequence, SubFactory

from ...models import User
from .base_factory import BaseFactory, fake


class UserFactory(BaseFactory):
    class Meta:
        model = User

    username = LazyAttribute(lambda x: fake.user_name())
    email = LazyAttribute(lambda x: fake.email())
    password = LazyAttribute(lambda x: fake.password())
