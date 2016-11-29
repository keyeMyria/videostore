from datetime import datetime

from sqlalchemy.ext.hybrid import hybrid_property

from ..db import db
from .timestamped_mixin import TimestampedModelMixin


class User(TimestampedModelMixin, db.Model):
    __tablename__ = 'users'

    def __init__(self, *args, **kwargs):
        self.plaintext_password = None
        super().__init__(*args, **kwargs)

    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(
        db.String(255), nullable=False, unique=True, index=True
    )
    email = db.Column(db.String(255), nullable=False, index=True)
    _password = db.Column("password", db.String(255), nullable=False)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self.plaintext_password = new_password
        # self._password = password_hash(new_password)
        self._password = new_password
