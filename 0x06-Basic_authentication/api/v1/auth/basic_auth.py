#!/usr/bin/env python3
"""
Basic Auth module for the API
"""
from typing import List, TypeVar
from api.v1.auth.auth import Auth
from base64 import b64decode
from models.user import User


class BasicAuth(Auth):
    '''Basic authentication'''

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        '''Return the basic auth part of the auth header
        auth header should look like the following string:
        Authorization: Basic YWxhZGRpbjpvcGVuc2VzYW1l
        '''
        bool_list: List[bool] = [
            authorization_header is None,
            type(authorization_header) != str,
        ]
        if any(bool_list):
            return None
        auth_list: List[str] = authorization_header.split(' ')
        if auth_list[0] != 'Basic':
            return None
        return auth_list[1]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        '''Return decoded base64 string'''
        bool_list: List[bool] = [
            base64_authorization_header is None,
            type(base64_authorization_header) != str,
        ]
        if any(bool_list):
            return None
        try:
            header_decoded: bytes = b64decode(base64_authorization_header)
        except:
            return None
        return header_decoded.decode('utf-8')

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        '''Return username, password'''
        bool_list: List[bool] = [
            decoded_base64_authorization_header is None,
            type(decoded_base64_authorization_header) != str,
        ]
        if any(bool_list):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        username_password = [
            i.strip(' ') for i in decoded_base64_authorization_header.split(':')]
        username = username_password[0]
        password = username_password[1]
        return username, password

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        '''Return user with matching credentials'''
        if user_email is None or type(user_email) != str:
            return None
        if user_pwd is None or type(user_pwd) != str:
            return None
        try:
            users = User.search({'email': user_email})
        except:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''Return User instance'''
        header = self.authorization_header(request)
        base64_header = self.extract_base64_authorization_header(header)
        decoded_header = self.decode_base64_authorization_header(base64_header)
        username, password = self.extract_user_credentials(decoded_header)
        return self.user_object_from_credentials(username, password)
