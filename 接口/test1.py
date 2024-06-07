import requests
url = 'https://contest.gitlab.ceba.ceshiren.com/api/v4/projects/id1162/issues'
headers = {
    'PRIVATE-TOKEN':'glpat-QfZs-RpyGyseE3edSjZk'
}
data = {
    'id':1162,
    "title":'一个标题',
    'assignee_id':1203
}
r = requests.post(url,headers=headers,json=data)
print(r.text)
