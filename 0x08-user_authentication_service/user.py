#!/usr/bin/env python3
'''User authentication'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class User(Base):
    '''Model of User'''
    __tablename__ = 'users'
    id: Column = Column(Integer, primary_key=True)
    email: Column = Column(String(250), nullable=False)
    hashed_password: Column = Column(String(250), nullable=False)
    session_id: Column = Column(String(250), nullable=True)
    reset_token: Column = Column(String(250), nullable=True)
