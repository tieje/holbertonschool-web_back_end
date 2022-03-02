#!/usr/bin/env python3
'''Test client functions'''
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @patch('client.get_json')
    def test_public_repos(self, mock):
        '''Test public repos'''
        payload = [{'name': 'hum'}, {'name', 'herm'}]
        mock.return_value = payload
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_repos:
            mocked_repos = 'hun'
            response = GithubOrgClient('x').public_repos()
            self.assertEqual(response, ['hum', 'herm'])
            mocked_repos.assert_called_once()
            mocked_repos.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])
    def test_has_license(self, repo, key, expectation):
        '''self descriptive'''
        result = GithubOrgClient.has_license(repo, key)
        self.assertEqual(result, expectation)


@parameterized_class(['org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'], TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''Integration test'''
    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('requests.get', side_effect=[
            cls.org_payload, cls.repos_payload
        ])
        cls.mocked_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        '''test public repos '''

    def test_public_repos_with_license(self):
        '''test public with license'''


if __name__ == '__main__':
    unittest.main()
