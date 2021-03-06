from ..db import db
from .timestamped_mixin import TimestampedModelMixin


class Role(TimestampedModelMixin, db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(
        db.String(255), nullable=False, unique=True, index=True
    )

    #: has_many User
    users = db.relationship('User', back_populates='role')
