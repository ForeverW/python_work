import requests

import pygal

from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS


url = 'https://api.github.com/search/repositories?q=language:python&sort=starts'

r = requests.get(url)
#print("Status code: ",r.status_code)

response_dict = r.json()

print("Total repositories:",response_dict['total_count'])

repo_dicts = response_dict['items']

print("Number of items:",len(repo_dicts))

names,plot_dicts = [],[]
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	#stars.append(repo_dict['stargazers_count'])
	
	plot_dict = {
	'value':repo_dict['stargazers_count'],
	'label':repo_dict['description']
	}
	plot_dicts.append(plot_dict)
	
my_style = LS('#333366',base_style = LCS)
chart = pygal.Bar(style = my_style,x_label_rotation=45,show_legend = False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.xlabels = names

#chart.add('',stars)
chart.add('',plot_dicts)
chart.render_to_file('python_repos_new.svg')

'''


repo_dict = repo_dicts[0]

print("\nSelected information about first repository:")
print('Name:',repo_dict['name'])
print('Owner:',repo_dict['owner']['login'])
print('Stars:',repo_dict['stargazers_count'])
print('Repository:',repo_dict['html_url'])
print('Created:',repo_dict['created_at'])
print('Updated:',repo_dict['updated_at'])
print('Description:',repo_dict['description'])
'''

'''
print("\nKeys:",len(repo_dict))
for key in sorted(repo_dict.keys()):
	print(key)
'''
