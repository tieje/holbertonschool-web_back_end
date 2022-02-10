#!/usr/bin/env python3
'''0. Regex-ing'''
import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]) -> None:
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''Return formatted string.'''
        message: str = filter_datum(
            self.fields, self.REDACTION, super().format(record), self.SEPARATOR)
        return message


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    '''Return log message obfuscated'''
    for field in fields:
        message = re.sub(f'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}',
                         message)
    return message

def get_logger() -> logging.Logger:
    logging
    pass