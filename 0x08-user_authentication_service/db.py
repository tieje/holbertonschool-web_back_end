#!/usr/bin/env python3
"""DB module
"""
from graphql import value_from_ast
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        '''Returns new user and adds to db'''
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **users) -> User:
        '''Returns first row found in users table
        about User'''
        try:
            record = self.__session.query(User).filter_by(**users).first()
        except:
            raise InvalidRequestError
        if record is None:
            raise NoResultFound
        return record

    def update_user(self, user_id, **kwargs) -> None:
        record = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if hasattr(record, key):
                setattr(record, key, value)
            else:
                raise ValueError
        self._session.commit()