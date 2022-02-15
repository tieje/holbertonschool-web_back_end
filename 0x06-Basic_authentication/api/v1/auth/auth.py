#!/usr/bin/env python3
"""
Auth module for the API
"""
from flask import request
from typing import List, TypeVar


class Auth:
    '''Auth class'''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''Return bool for paths'''
        bool_list: List[bool] = [
            path is None,
            excluded_paths is None,
            excluded_paths == []
        ]
        if any(bool_list):
            return True
        path = path.rstrip('/')
        excluded_paths = [
            i.rstrip('/') if type(i) == str else i for i in excluded_paths
        ]
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        '''Return Flask request object'''
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        '''Return Flask request object'''
        return None
