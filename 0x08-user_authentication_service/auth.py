#!/usr/bin/env python3
'''Auth module'''
from db import DB
from bcrypt import hashpw, gensalt
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    return hashpw(password.encode('utf-8'), gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self) -> None:
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        '''Return user object'''
        try:
            self._db.find_user_by(email=email)
            raise ValueError('User ' + email + ' already exists')
        except NoResultFound:
            return self._db.add_user(email, str(_hash_password(password)))
