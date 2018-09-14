import requests
url = 'https://www.behance.net/HabbenINK'
headers = {'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X)'}
response = requests.get(url, headers=headers)
from bs4 import BeautifulSoup as BS
soup = BS(response.content, 'html.parser')
soup.prettify
ul_lists = soup.find_all('ul')
