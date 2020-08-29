import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limir=50")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class": "pagination"})

links = pagination.find_all('a')
pages = []

for link in links[:-1]:
  pages.append(int(link.string))

#get lists of pages to cutting the last item.

#[-1] : means the last 1 item of the list
#print(spans[-1])

#[0:-1] : means 0 to except last 1 item of the list
#print(spans[0:-1])

last_page = pages[-1]