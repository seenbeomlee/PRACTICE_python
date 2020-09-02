import requests
from flask import Flask, render_template, request

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
  URL = f"{base_url}/items/{id}"
  result = requests.get(URL).json()

  return result

db = {}
app = Flask("DayNine")

def getNews(query):
  if query.find("new") != -1:
    URL = new
  else:
    URL = popular
  result = requests.get(URL).json()['hits']

  return result

@app.route("/")
def home():
  query = request.args.get('order_by')
  if query:
    existingNews = db.get(query)
    if existingNews:
      newsTable = existingNews
    else:
      newsTable = getNews(query)
      db[query] = newsTable
  else:
    query = "popular"
    newsTable = getNews(query)
    db[query] = newsTable

  return render_template("index.html", newsTable=newsTable)

@app.route("/<objectID>")
def detail(objectID):

    commentsTable = make_detail_url(objectID)

    return render_template("detail.html", commentsTable=commentsTable)

app.run(host="0.0.0.0")