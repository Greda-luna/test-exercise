import requests
url = 'https://contest.gitlab.ceba.ceshiren.com/api/v4/projects/id1162/issues'
headers = {
    'PRIVATE-TOKEN':'glpat-QfZs-RpyGyseE3edSjZk'
}

r = requests.get(url,headers=headers)
print(r.text)
