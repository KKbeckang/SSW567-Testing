import requests
import json

def GithubRepoInfo(UserId):
    if not isinstance(UserId, str):
        return "The User ID should be a String"
    if UserId == '':
        return "The Input cannot be empty"
    FullURL = "https://api.github.com/users/"+ UserId +"/repos"
    read = requests.get(FullURL)
    record = read.json()
    if not isinstance(record,list):
        return "The Input User is Invalid"
    RepoInfo=[]
    RepoNames=[]
    RepoCommitsNum =[]
    RepoURL = "https://api.github.com/repos/"
    for i in range(len(record)):
        RepoURL = "https://api.github.com/repos/" +UserId +"/"+record[i]['name']+"/commits"
        RepoCommit = requests.get(RepoURL)
        RepoCommit = RepoCommit.json()
        RepoNames.append(record[i]['name'])
        RepoCommitsNum.append(len(RepoCommit))
    for i in range(len(record)):{
        RepoInfo.append("Repo: {} Number of commits: {}".format(RepoNames[i],str(RepoCommitsNum[i])))
    }
    return RepoInfo

print(GithubRepoInfo('KKbeckang'))


    
