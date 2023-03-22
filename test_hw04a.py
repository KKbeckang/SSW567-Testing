import unittest
from unittest import mock
from unittest.mock import Mock,patch,MagicMock

from hw04a import GithubRepoInfo


class TestHW4(unittest.TestCase):
    """mock the result of GIthubrepo info"""
    @mock.patch('hw04a.GithubRepoInfo')
    def testGitUser(self,mock_GithubRepoInfo):
        """mock our hw04a.py first see if it work"""
        mock_GithubRepoInfo.return_value = ['Repo: avi-clothing Number of commits: 8', 'Repo: Boston_HackRan Number of commits: 6', 'Repo: Covid19_repo Number of commits: 3', 'Repo: crwn-clothing-v2 Number of commits: 5', 'Repo: CS-555-project Number of commits: 28', 'Repo: CS391-Web-Audit Number of commits: 5', 'Repo: HW02a_TestingLagacyProgram Number of commits: 10', 'Repo: KK-CS412 Number of commits: 6', 'Repo: KKbeckang Number of commits: 13', 'Repo: KKbeckang.github.io Number of commits: 1', 'Repo: Monster-Contact-Book Number of commits: 5', 'Repo: project_hoobank Number of commits: 9', 'Repo: RentPipe Number of commits: 30', 'Repo: Rentpiplib Number of commits: 2', 'Repo: SSW567-Testing Number of commits: 12', 'Repo: VOICEDATA Number of commits: 2']
        self.assertEqual(GithubRepoInfo("KKbeckang")[0],'Repo: avi-clothing Number of commits: 8','Fail')

    @mock.patch('requests.get')
    def mock_Test_API_get1(self,mock_Request):
        """example 1"""
        mock_Request.return_value = Mock(status_code = 200, text = '[{"name":"Rentpip"}, {"name": "Jacksun"}]')
        self.assertEqual(len(GithubRepoInfo("KKbeckang")),2)
        self.assertEqual(GithubRepoInfo("KKbeckang"), ['Complexity','Jacksun'])

    @mock.patch('requests.get')
    def mock_Test_API_get2(self,mock_Request):
        """example 2"""
        mock_Request.return_value = Mock(status_code = 200, text = '[{"name":"Rentpip"}, {"name": "Jacksun"}.{"name": "Jacksun1"}.{"name": "Jacksun2"}{"name": "Jacksun3"}]')
        self.assertEqual(len(GithubRepoInfo("KKbeckang")),5)
        self.assertEqual(GithubRepoInfo("KKbeckang"), ['Complexity','Jacksun','Jacksun1','Jacksun2','Jacksun3'])

    @mock.patch('requests.get')
    def mock_Test_API_Not_Found(self,mock_Request):
        """cannot be found message"""
        mock_Request.return_value = Mock(status_code = 200, text = {'message': 'Not Found', 'documentation_url': 'https://docs.github.com/rest/reference/repos#list-repositories-for-a-user'})
        self.assertEqual(GithubRepoInfo('esdsadasesxxzcxzczsdae232o'),'The Input User is Invalid',)
   
    def testEmptyString(self):
        self.assertEqual(GithubRepoInfo(''),'The Input cannot be empty','Fail')



if __name__ == '__main__':
    unittest.main(exit=False) 