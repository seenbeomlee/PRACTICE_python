from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

app = Flask("SuperScrapper")

#fake DB must be outside of route
db = {}

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  if word:
    word = word.lower()
    fromDB = db.get(word)
    if fromDB:
      jobs = fromDB
    else:
      jobs = get_jobs(word)
      #save results inside of fask DB (Dynamic Programming..? maybe)
      db[word] = jobs
  else:
    return redirect("/")
  return render_template("report.html", searchingBy=word, resultsNumber = len(jobs), potato='imPotato')

app.run(host="0.0.0.0")