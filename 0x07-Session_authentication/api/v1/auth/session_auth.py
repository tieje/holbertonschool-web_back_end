#!/usr/bin/env python3
'''Session authentication'''
from api.v1.auth.auth import Auth
from models.user import User
from typing import Dict, TypeVar
from uuid import uuid4


class SessionAuth(Auth):
    '''Session Authentication'''
    user_id_by_session_id: Dict = {}

    def create_session(self, user_id: str = None) -> str:
        '''Return Session ID'''
        if user_id is None or type(user_id) != str:
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        '''Return User Id based on session ID'''
        if session_id is None or type(session_id) != str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> TypeVar('User'):
        '''Return User instance from session Id cookie'''
        session_cookie = self.session_cookie(request)
        user_id = self.user_id_by_session_id.get(session_cookie)
        return User.get(user_id)
