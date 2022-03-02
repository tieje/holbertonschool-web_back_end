#!/bin/env python3
'''Test client functions'''
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    ''' self descriptive '''

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, data, mock):
        ''' self descriptive '''
        endpoint = 'https://api.github.com/orgs/{}'.format(data)
        spec = GithubOrgClient(data)
        spec.org()
        mock.assert_called_once_with(endpoint)
    
    def test_public_repos_url(self):
        '''Test public repos url'''
        expected = 'fang'
        url = 'https://api.github.com/orgs/{}'.format(expected)
        val = {'repos_url': url}
        mock = 'client.GithubOrgClient.org'
        with patch(mock, PropertyMock(return_value=val)):
            response = GithubOrgClient(expected)._public_repos_url
            self.assertEqual(response, url)
