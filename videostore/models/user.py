from datetime import datetime

from ..db import db
from .timestamped_mixin import TimestampedModelMixin


class User(TimestampedModelMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(
        db.String(255), nullable=False, unique=True, index=True
    )
    email = db.Column(db.String(255), nullable=False, index=True)
    _password = db.Column("password", db.String(255), nullable=False)
