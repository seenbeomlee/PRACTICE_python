import requests
from bs4 import BeautifulSoup

def extract_sojob(html):
  title = html.find("h2").text.strip()

  company = html.find("h3", {"class":"fc-black-700"}).find("span",recursive=False)
  company = company.get_text(strip=True)

  job_id = html['data-jobid']

  return {
    'title': title,
    'company': company,
    'link': f"  https://stackoverflow.com/jobs/{job_id}",
    }

def extract_wwrjob(html):
  title = html.find("span", {"class": "title"}).text

  company = html.find("span", {"class":"company"}).text

  link = html.find("a")['href']

  return {
      'title': title,
      'company': company,
      'link': f"https://weworkremotely.com{link}",
    }

def extract_rojob(html):

  title = html['data-search']
  company = html['data-company']
  job_id = html['data-id']

  return {
      'title': title,
      'company': company,
      'link': f"https://remoteok.io/l/{job_id}",
    }

def extract_jobs(soURL, wwrURL, roURL):
  jobs = []

  print("Scrapping so")
  result = requests.get(soURL)
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("div", {"class": "-job"})
  for result in results:
    job = extract_sojob(result)
    jobs.append(job)

  print("Scrapping wwr")
  result = requests.get(wwrURL)
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find("section", {"class": "jobs"}).find_all("li", {"class": "feature"})
  for result in results:
    job = extract_wwrjob(result)
    jobs.append(job)

  print("Scrapping ro")
  result = requests.get(roURL)
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find("table", {"id": "jobsboard"})
  results = results.find_all("tr", {"class": "job"})

  for result in results:
    job = extract_rojob(result)
    jobs.append(job)
      
  return jobs

def get_jobs(word):
  soURL = f"https://stackoverflow.com/jobs?r=true&q={word}"
  wwrURL = f"https://weworkremotely.com/remote-jobs/search?term={word}"
  roURL = f"https://remoteok.io/remote-dev+{word}-jobs"

  jobs = extract_jobs(soURL, wwrURL, roURL)
  return jobs
