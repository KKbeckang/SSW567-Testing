import requests
import json

def GithubRepoInfo(UserId):
    
    access_token = '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'
    if not isinstance(UserId, str):
        return "The User ID should be a String"
    if UserId == '':
        return "The Input cannot be empty"
    FullURL = "https://api.github.com/users/"+ UserId +"/repos"
    read = requests.get(FullURL,
                        headers={'Authorization': f'token {access_token}'})
    record = read.json()
    
    if not isinstance(record,list):
        return "The Input User is Invalid"
    RepoInfo=[]
    RepoNames=[]
    RepoCommitsNum =[]
    RepoURL = "https://api.github.com/repos/"
    for i in range(len(record)):
        RepoURL = "https://api.github.com/repos/" +UserId +"/"+record[i]['name']+"/commits"
        RepoCommit = requests.get(RepoURL,
                        headers={'Authorization': f'token {access_token}'})
        RepoCommit = RepoCommit.json()
        RepoNames.append(record[i]['name'])
        RepoCommitsNum.append(len(RepoCommit))
    for i in range(len(record)):{
        RepoInfo.append("Repo: {} Number of commits: {}".format(RepoNames[i],str(RepoCommitsNum[i])))
    }
    return RepoInfo

