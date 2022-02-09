#!/usr/bin/env python3
'''0. Regex-ing'''
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    '''Return log message obfuscated'''
    new_message: List[str] = []
    new_str: str
    for i in fields:
        new_s = re.sub('^' + i + '=.*' + separator + '$',
                       '=' + redaction + '', message)
        new_message.append(new_s)
    return ''.join(new_message)
