#!/bin/env python3
'''Test utils functions'''
from typing import Dict, Mapping, Sequence
import unittest
from unittest.mock import Mock
from unittest.mock import patch
from parameterized import parameterized
from nose.tools import assert_equal, raises

from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    '''Test Access Nested Map'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, expected):
        '''Test normal function'''
        assert_equal(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    @raises(KeyError)
    def test_access_nested_map_exception(self, nested_map: Mapping, path: Sequence):
        '''Test KeyError exception'''
        access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''Test get_json from utils'''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: Dict):
        '''Test get_json'''
        mock_request = Mock()
        mock_request.json.return_value = test_payload
        # not patch will otherwise return a MagicMock, not Mock
        with patch('requests.get', return_value=mock_request):
            # when the request.get method is used by get_json()
            # It will be replace by our custom mock.
            # The get_json accesses the json getter method.
            # In the mock, json() method returns test_payload
            response: Dict = get_json(test_url)
            mock_request.json.assert_called_once()
        assert_equal(response, test_payload)


class TestMemoize(unittest.TestCase):
    '''Test memoize method'''

    def test_memoize(self):
        '''Test memoize'''
        class TestClass:
            '''Test class'''

            def a_method(self):
                '''test method'''
                return 42

            @memoize
            def a_property(self):
                '''check memoization'''
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mock.assert_called_once()
