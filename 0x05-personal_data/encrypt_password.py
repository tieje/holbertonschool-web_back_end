#!/usr/bin/env python3
'''
5. Encrypting passwords
6. Check valid password
'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''Return Hashed password.
    Does not work on M1 chip'''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''Return if passwords match'''
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
