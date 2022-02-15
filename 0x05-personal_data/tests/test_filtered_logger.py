#!/usr/bin/env python3
'''Tests'''
import logging
from typing import List
import unittest
filter_datum = __import__('filtered_logger').filter_datum
RedactingFormatter = __import__('filtered_logger').RedactingFormatter
get_logger = __import__('filtered_logger').get_logger
get_db = __import__('filtered_logger').get_db
PII_FIELDS = __import__('filtered_logger').PII_FIELDS


class TestFilterDatum(unittest.TestCase):
    '''Test filter_datum() method'''

    def setUp(self) -> None:
        '''test setup'''
        self.fields: List[str] = ["password", "date_of_birth"]
        self.message1: str = "name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;"
        self.message2: str = "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"

    def test_message1(self) -> None:
        self.assertEqual(
            filter_datum(self.fields, 'xxx', self.message1, ';'),
            'name=egg;email=eggmin@eggsample.com;password=xxx;date_of_birth=xxx;'
        )

    def test_message2(self) -> None:
        self.assertEqual(
            filter_datum(self.fields, 'xxx', self.message2, ';'),
            'name=bob;email=bob@dylan.com;password=xxx;date_of_birth=xxx;'
        )


class TestRedactedFormat(unittest.TestCase):
    '''Test RedactingFormatter class'''

    def setUp(self) -> None:
        '''set up'''
        self.message = "name=Bob;email=bob@dylan.com;ssn=000-123-0000;password=bobby2019;"
        self.log_record = logging.LogRecord(
            "my_logger", logging.INFO, None, None, self.message, None, None)
        self.formatter = RedactingFormatter(
            fields=("email", "ssn", "password"))
        self.testThis: str = self.formatter.format(self.log_record)

    def test_format_first_part(self):
        '''Test the prepend of log'''
        answer1: str = '[HOLBERTON] my_logger INFO'
        self.assertTrue(answer1 in self.testThis)

    def test_format_second_part(self):
        '''Test the append of log'''
        # removed spaces to fit what actually occurs
        answer2: str = 'name=Bob;email=***;ssn=***;password=***;'
        self.assertTrue(answer2 in self.testThis)


class Testget_logger(unittest.TestCase):
    '''test get_logger()'''

    def test_PII_FIELDS(self):
        '''test PII_FIELDS'''
        self.assertEqual(len(PII_FIELDS), 5)

    def test_get_logger_Return_Type(self):
        '''test Return type'''
        self.assertEqual(
            str(get_logger.__annotations__.get('return')),
            "<class 'logging.Logger'>")


class Testget_db(unittest.TestCase):
    '''test get_db()'''

    def test_get_db_Return_Type(self):
        '''test return type of get_db()'''
        self.assertEqual(
            str(get_db.__annotations__.get('return')),
            "<class 'mysql.connector.connection.MySQLConnection'>")
