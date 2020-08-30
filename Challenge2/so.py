import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python&sort=i"

def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")

  pages = soup.find("div", {"class": "s-pagination"}).find_all('a')
  last_page = pages[-2].get_text(strip=True)
  return int(last_page)
  
def extract_job(html):
  title = html.find("h2").text.strip()

  # span
  #   span
  # 구조로 되어있는데, recursive=False를 사용해서, find_all이 첫번 째 span만 가져오게 설정한 것이다.
  company, location = html.find("h3", {"class":"fc-black-700"}).find_all("span",recursive=False)
  company = company.get_text(strip=True)
  location = location.get_text(strip=True)
  # above code is same as below
  # company_row = ...
  # compnay = company_raw[0] ..
  # location = company_raw[1] ..

  return {'title':title}

def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    result = requests.get(f"{URL}&pg={page+1}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "-job"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
    return jobs


def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs