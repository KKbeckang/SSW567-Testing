import unittest
from hw04a import GithubRepoInfo

class TestHW4(unittest.TestCase):
    def testGitUser(self):
        self.assertEqual(GithubRepoInfo("KKbeckang"),['Repo: avi-clothing Number of commits: 8', 'Repo: Banking Number of commits: 2', 'Repo: Boston_HackRan Number of commits: 6', 'Repo: Covid19_repo Number of commits: 3', 'Repo: crwn-clothing-v2 Number of commits: 5', 'Repo: CS391-Web-Audit Number of commits: 5', 'Repo: HW02a_TestingLagacyProgram Number of commits: 10', 'Repo: KK-CS412 Number of commits: 6', 'Repo: KKbeckang Number of commits: 13', 'Repo: KKbeckang.github.io Number of commits: 1', 'Repo: Monster-Contact-Book Number of commits: 5', 'Repo: project_hoobank Number of commits: 9', 'Repo: python-circleCI Number of commits: 2', 'Repo: RentPipe Number of commits: 30', 'Repo: Rentpiplib Number of commits: 2', 'Repo: SSW567-HW4 Number of commits: 9', 
'Repo: VOICEDATA Number of commits: 2'],'Fail')

    def testNonString(self):
        self.assertEqual(GithubRepoInfo(21312412312),'The User ID should be a String','Fail')
    def testNonUser(self):
        self.assertEqual(GithubRepoInfos('esdsadasesxxzcxzczsdae232o'),'The Input User is Invalid','Fail')



if __name__ == '__main__':
    unittest.main(exit=False)