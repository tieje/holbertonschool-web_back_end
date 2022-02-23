#!/usr/bin/env python3
'''Auth module'''
from db import DB
from bcrypt import hashpw, gensalt, checkpw
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    '''Return Hash password'''
    return hashpw(password.encode('utf-8'), gensalt())


def _generate_uuid() -> str:
    '''Generate uuid'''
    return str(uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        '''Valid Login'''
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return checkpw(password.encode('utf-8'), user.hashed_password)
