import unittest
from unittest import mock
from unittest.mock import Mock,patch,MagicMock

from hw04a import GithubRepoInfo


class TestHW4(unittest.TestCase):
    """mock the result of GIthubrepo info"""

    @mock.patch('requests.get')
    def test_mock_Test_API_get1(self,mock_Req):
        """example 1"""
        mock_Req.return_value = Mock(json_data = {"name":"Rentpip","name": "Jacksun"})
        self.assertEqual(GithubRepoInfo("KKbeckang"), ['Rentpip','Jacksun'])

    @mock.patch('requests.get')
    def test_mock_Test_API_get2(self,mock_Request):
        """example 2"""
        mock_Request.return_value = Mock(status_code = 200, text = '[{"name":"Rentpip"}, {"name": "Jacksun"}.{"name": "Jacksun1"}.{"name": "Jacksun2"}{"name": "Jacksun3"}]')
        self.assertEqual(len(GithubRepoInfo("KKbeckang")),5)
        self.assertEqual(GithubRepoInfo("KKbeckang"), ['Rentpip','Jacksun','Jacksun1','Jacksun2','Jacksun3'])

    @mock.patch('requests.get')
    def test_mock_Test_API_Not_Found(self,mock_Request):
        """cannot be found message"""
        mock_Request.return_value = Mock(status_code = 404, text = {'message': 'Not Found', 'documentation_url': 'https://docs.github.com/rest/reference/repos#list-repositories-for-a-user'})
        self.assertEqual(GithubRepoInfo('esdsadasesxxzcxzczsdae232o'),'The Input User is Invalid','Fail')
   
    def test_EmptyString(self):
        self.assertEqual(GithubRepoInfo(''),'The Input cannot be empty','Fail')

    def test_NonUser(self):
        self.assertEqual(GithubRepoInfo('esdsadasesxxzcxzczsdae232o'),'The Input User is Invalid','Fail')


if __name__ == '__main__':
    unittest.main(exit=False) 