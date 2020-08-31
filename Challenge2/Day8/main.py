import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"

def save_to_file(jobs, company):
  file = open(f"./jobs/{company}.csv", mode="w")

  writer = csv.writer(file)
  writer.writerow(["place", "title", "time", "pay", "date"])

  for job in jobs:
    writer.writerow(list(job.values()))

def extract_job(link):
  result = requests.get(link)
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find("tbody").find_all("tr", {"class": ""})
  jobs = []
  for result in results:
    td_block = result.find_all("td")
    length = len(td_block)

    if(td_block):
      if length > 1:
        if td_block[1].find_all("span"):
          title = td_block[1].find_all("span")[0].text
        else:
          title = "None"
      else:
        title = "None"

      job = {
        'place': td_block[0].text if td_block[0] else "None",
        'title': title,
        'time': td_block[2].text if length > 2 else "None",
        'pay': td_block[3].text if length > 3 else "None",
        'date': td_block[4].text if length > 4 else "None",
      }
    jobs.append(job)

  return jobs

def extract_jobs():
  
  result = requests.get(alba_url)
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find("div", {"id": "MainSuperBrand"}).find_all("a", {"class": "goodsBox-info"})
  
  for result in results:
    jobs = []
    link = result['href']
    company = result.find("span", {"class": "company"}).text
    
    if(link):
      jobs = extract_job(link)
      save_to_file(jobs, company)

def get_jobs():
  extract_jobs()

get_jobs()