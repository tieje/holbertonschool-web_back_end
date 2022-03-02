#!/bin/env python3
'''Test client functions'''
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    '''Test GithubOrgClient method'''
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org, mock):
        '''Test org()'''
        url = 'https://api.github.com/orgs/{}'.format(org)
        test = GithubOrgClient(org)
        test.org()
        mock.assert_called_once_with(url)
    
    def test_public_repos_url(self):
        '''Test public repos url'''
        expected = 'fang'
        url = 'https://api.github.com/orgs/{}'.format(expected)
        val = {'repos_url': url}
        mock = 'client.GithubOrgClient.org'
        with patch(mock, PropertyMock(return_value=val)):
            response = GithubOrgClient(expected)._public_repos_url
            self.assertEqual(response, url)
