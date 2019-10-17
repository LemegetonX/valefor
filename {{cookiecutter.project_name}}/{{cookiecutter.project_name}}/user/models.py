from passlib.hash import argon2
from slugify import slugify

from ..app import db


class User(db.Model):
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)

    username = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String, nullable=False)

    @db.validates("username")
    def validate_username(self, key, value) -> str:
        assert value == slugify(value), "Incorrect username!"

        return value
    
    @classmethod
    def lookup(cls, username) -> "User":
        return User.query.filter_by(username=username).first()

    @property
    def password(self) -> str:
        raise self._password_hash

    @password.setter
    def password(self, new_password: str) -> None:
        self._password_hash = argon2.hash(new_password)

    def check_password(self, candidate: str) -> bool:
        return argon2.verify(candidate, self._password_hash)

