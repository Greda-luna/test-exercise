import requests
url = 'https://contest.gitlab.ceba.ceshiren.com/api/v4/projects/id1162/issues/issue_iid变量/'
headers = {
    'PRIVATE-TOKEN':'glpat-QfZs-RpyGyseE3edSjZk'
}
data = {
    'id':1162,
    "issue_iid":'',
    'state_event':'no'
}
r = requests.put(url,headers=headers,data=data)
print(r.text)
