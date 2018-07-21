#!/usr/bin/env python3

from app import db, ma


class User(db.Model):
    """Define a User model"""

    __tablename__ = 'users'

    id_ = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    # Identification Data: email & password
    email = db.Column(db.String(128),  nullable=False, unique=True)
    password = db.Column(db.String(192),  nullable=False)

    first_name = db.Column(db.String(55), nullable=False)
    last_name = db.Column(db.String(55), nullable=False)
    picture = db.Column(db.String(55), nullable=True)

    # Authorization Data: role & status
    role = db.Column(db.SmallInteger, nullable=False)
    status = db.Column(db.SmallInteger, nullable=False)

    # New instance instantiation procedure
    def __init__(self,
                 email: str,
                 password: str,
                 first_name: str,
                 last_name: str) -> None:

        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.picture = None
        self.role = 0
        self.status = 0

    def __repr__(self) -> str:
        return 'User: {}'.format(self.id_)


class UserSchema(ma.Schema):
    class Meta:
        fields = (
            'id_',
            'email',
            'first_name',
            'last_name',
            'picture'
        )
