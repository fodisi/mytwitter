# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db
from app.base_model import BaseModel


class User(BaseModel):
    """Define a User model"""

    __tablename__ = 'users'

    # Identification Data: email & password
    email = db.Column(db.String(128),  nullable=False, unique=True)
    password = db.Column(db.String(192),  nullable=False)

    first_name = db.Column(db.String(55), nullable=False)
    last_name = db.Column(db.String(55),  nullable=False)

    # Authorization Data: role & status
    role = db.Column(db.SmallInteger, nullable=False)
    status = db.Column(db.SmallInteger, nullable=False)

    # New instance instantiation procedure
    def __init__(self,
                 username: str,
                 email: str,
                 password: str,
                 first_name: str,
                 last_name: str) -> None:

        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.role = 0
        self.status = 0

    def __repr__(self) -> str:
        return '<User %r>' % (self.name)
