import unittest
from hw04a import GithubRepoInfo

class TestHW4(unittest.TestCase):
    def testGitUser(self):
        self.assertEqual(GithubRepoInfo("KKbeckang")[0],['Repo: avi-clothing Number of commits: 8'],'Fail')

    def testNonString(self):
        self.assertEqual(GithubRepoInfo(21312412312),'The User ID should be a String','Fail')
    def testNonUser(self):
        self.assertEqual(GithubRepoInfo('esdsadasesxxzcxzczsdae232o'),'The Input User is Invalid','Fail')



if __name__ == '__main__':
    unittest.main(exit=False)