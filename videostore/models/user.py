from sqlalchemy.ext.hybrid import hybrid_property

from ..db import db
from ..lib import password_hash
from .timestamped_mixin import TimestampedModelMixin


class User(TimestampedModelMixin, db.Model):
    __tablename__ = 'users'

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

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self.plaintext_password = new_password
        self._password = password_hash(new_password)
