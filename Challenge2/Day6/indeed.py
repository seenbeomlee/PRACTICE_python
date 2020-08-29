import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limir={LIMIT}"

def extract_indeed_pages():
  result = requests.get(URL)

  soup = BeautifulSoup(result.text, "html.parser")

  pagination = soup.find("div", {"class": "pagination"})

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

  return last_page

def extract_indeed_jobs(last_page):
  jobs = []
  # for page in range(last_page):
  result = requests.get(f"{URL}&start={0*LIMIT}")
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
  
  for result in results:
    title = result.find("h2", {"class": "title"}).find("a")["title"]
    
    company = result.find("span", {"class": "company"})
    company_anchor = company.find("a")
    if company_anchor is not None:
      company = str(company_anchor.string)
    else:
     company = str(company.string)
    company = company.strip()
    print(title, company)

  return jobs