import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limir=50")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class": "pagination"})

pages = pagination.find_all('a')
spans = []

for page in pages:
  spans.append(page.find("span"))

#get lists of pages to cutting the last item.
print(spans[:-1])

#[-1] : means the last 1 item of the list
#print(spans[-1])

#[0:-1] : means 0 to except last 1 item of the list
#print(spans[0:-1])
