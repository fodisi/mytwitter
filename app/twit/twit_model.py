#!/usr/bin/env python3

from marshmallow import fields

from app import db, ma


class Twit(db.Model):
    """Define a Twit model"""

    __tablename__ = 'twits'

    id_ = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp()
    )

    message = db.Column(db.String(280), nullable=False)
    picture = db.Column(db.String(280), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id_'), nullable=False)
    user = db.relationship('User', backref=db.backref('user_twits', lazy=True))

    retwit_from = db.Column(
        db.Integer, db.ForeignKey('twits.id_'), nullable=True)
    retwit = db.relationship(
        'Twit', backref=db.backref('original_twit', remote_side=[id_]))

    # New instance instantiation procedure

    def __init__(self,
                 user_id: int,
                 message: str) -> None:

        self.user_id = user_id
        self.message = message
        self.picture = None
        self.retwit_from = None

    def __repr__(self) -> str:
        return 'Twit: {}'.format(self.message)


class TwitSchema(ma.Schema):

    class Meta:
        fields = (
            'id_',
            'date_created',
            'date_modified',
            'message',
            'picture',
            'user',
            'original_twit'
        )

    user = ma.Nested('UserSchema')
    original_twit = ma.Nested('TwitSchema')


#   {
#     "date_created": "2018-07-20T18:04:24+00:00",
#     "date_modified": "2018-07-20T18:04:24+00:00",
#     "id_": 4,
#     "message": "My first twit",
#     "original_twit": {
#       "date_created": "2018-07-20T16:06:42+00:00",
#       "date_modified": "2018-07-20T17:47:41+00:00",
#       "id_": 0,
#       "message": "My first twit",
#       "original_twit": null,
#       "picture": null,
#       "user": {
#         "email": "a@g.c",
#         "id_": 1,
#         "last_name": "l",
#         "picture": null
#       }
#     },
#     "picture": null,
#     "user": {
#       "email": "a@g.c",
#       "id_": 1,
#       "last_name": "l",
#       "picture": null
#     }
#   }
