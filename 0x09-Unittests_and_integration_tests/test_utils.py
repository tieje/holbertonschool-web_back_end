#!/bin/env python3
'''Test utils functions'''
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    '''Test Access Nested Map'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''Test normal function'''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        '''Test KeyError exception'''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''Test get_json from utils'''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload):
        '''Test get_json'''
        mock_request = Mock()
        mock_request.json.return_value = test_payload
        # not patch will otherwise return a MagicMock, not Mock
        with patch('requests.get', return_value=mock_request):
            # when the request.get method is used by get_json()
            # It will be replace by our custom mock.
            # The get_json accesses the json getter method.
            # In the mock, json() method returns test_payload
            response = get_json(test_url)
            mock_request.json.assert_called_once()
        self.assertEqual(response, test_payload)


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
