from sqlalchemy.ext.hybrid import hybrid_property

from ..db import db
from ..lib import generate_api_key, password_hash
from .base_query import BaseQuery
from .timestamped_mixin import TimestampedModelMixin


class UserQuery(BaseQuery):
    def find_by_username_or_email(self, username_or_email):
        return self.filter(
            or_(
                self.model.username == username_or_email,
                self.model.email == username_or_email,
            )
        )


class User(TimestampedModelMixin, db.Model):
    __tablename__ = 'users'
    query_class = UserQuery

    STATUSES = {
        'archived': -1,
        'locked': 0,
        'active': 1,
    }

    ROLES = {
        'user': 1,
        'admin': 2
    }

    def __init__(self, *args, **kwargs):
        self.plaintext_password = None
        super().__init__(*args, **kwargs)

    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(
        db.String(255), nullable=False, unique=True, index=True
    )
    email = db.Column(db.String(255), nullable=False, index=True)
    role = db.Column(
        db.SmallInteger, nullable=False,
        default=ROLES['user'], server_default=str(ROLES['user'])
    )
    status = db.Column(
        db.SmallInteger, nullable=False,
        default=STATUSES['locked'], server_default=str(STATUSES['locked'])
    )
    _password = db.Column("password", db.String(255), nullable=False)

    api_key = db.Column(
        db.String(255), nullable=False, index=True, unique=True,
        default=generate_api_key
    )

    __table_args__ = (
        db.CheckConstraint(
            status.in_(STATUSES.values())
        ),
        db.CheckConstraint(
            role.in_(ROLES.values())
        ),
    )

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self.plaintext_password = new_password
        self._password = password_hash(new_password)

    @hybrid_property
    def is_active(self):
        return self.status == self.STATUSES['active']
