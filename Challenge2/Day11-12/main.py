import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup
from operator import itemgetter

"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""

subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]


app = Flask("DayEleven")

db = {}

def extract_content(html, sub):
  link = '#'

  title = html.find("h3", {"class": "_eYtD2XCVieq6emjKBH3m"}).text
  if html.find("a", {"class": "SQnoC3ObvgnGjWt90zD9Z"}):
    link = html.find("a", {"class": "SQnoC3ObvgnGjWt90zD9Z"})["href"]
  votes = html.find("div", {"class": "_1rZYMD_4xY3gRcSS3p8ODO"}).text

  votes.replace('•', '0')

  if 'k' in votes:
    votes = votes.replace('k', '')
    votesArray = votes.split('.')
    votes = (int(votesArray[0]) * 1000 + int(votesArray[1]) * 100)

  return {
    'sub': 'r/' + sub,
    'title': title,
    'link': 'https://www.reddit.com/' + link,
    'votes': int(votes)
  }

def extract_contents(url, sub):
  contents = []

  print("extracting url: " + url)
  result = requests.get(url, headers=headers)
  soup = BeautifulSoup(result.text, "html.parser")

  contents_divs = soup.find_all("div", {"class": "_1poyrkZ7g36PawDueRza-J"})

  for contents_div in contents_divs:
    content = extract_content(contents_div, sub)
    contents.append(content)
  
  return contents
  
  # title
  # link
  # votes

  # from

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/r")
def read_page():
  args = request.args.to_dict()
  readingHeader = ''
  contents = {}
  tempRes = []
  for sub in subreddits:
    if sub in args:
      if sub not in db:
        readingHeader = readingHeader + "r/" + sub + " "
        url = "https://www.reddit.com/r/"+sub+"/top/?t=month"
        content = extract_contents(url, sub)
        contents[sub] = content
        db[sub] = content
      else:
        contents[sub] = db[sub]

  for arr in contents:
    tempRes.extend(contents[arr])

  res = sorted(tempRes, key=(lambda x: x['votes']))

  return render_template("read.html", readingHeader = readingHeader, res = reversed(res))


app.run(host="0.0.0.0")