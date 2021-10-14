# Interactive Bar Chart using data from GitHub API
# Using requests library and plotly
import requests
from plotly.graph_objs import Bar
from plotly import offline
import pandas as pd

# Get today's date for data visual
today  = pd.to_datetime('today').date()
#Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code:{r.status_code}")

#Store API in response variable
response_dict = r.json()
# print(f"Total respositories: {response_dict['total_count']}")
# Explore information about the repositories
repo_dicts = response_dict['items']
# print(f"Respositories returned: {len(repo_dicts)}") #to check the count
# repo_dict = repo_dicts[0] #placed here when i only wanted information from one repo
repo_names, stars = [],[]
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
# Make bar chart
data = [{
'type': 'bar',
'x':repo_names,
'y':stars,
}]

my_layout = {
    'title':f"Most-Starred Python Projects on GitHub as of {today}",
    'xaxis':{'title': 'Repository Name'},
    'yaxis':{'title': 'Stars'},
}

fig = {'data':data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
#Examining the first repository  returned from the printed responses
# print("\nSelected information about first respository:")
# Getting information from more than just top repo
# for repo_dict in repo_dicts:
#     # Name
#     print(f"Name: {repo_dict['name']}")
#     # Owner of the top repo
#     print(f"Owner: {repo_dict['owner']['login']}")
#     # Number of times people have stared the top repo
#     print(f"Stars: {repo_dict['stargazers_count']}")
#     # URL
#     print(f"Repository:{repo_dict['html_url']}")
#     # Create Date
#     print(f"Created: {repo_dict['created_at']}")
#     # Last Date the top repo was updated
#     print(f"Updated: {repo_dict['updated_at']}")
#     # Description
#     print(f"Description: {repo_dict['description']}")


# print(f"\nKeys:{len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)

# #process results
# print(response_dict.keys())
