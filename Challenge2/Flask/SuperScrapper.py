from flask import Flask

app = Flask("SuperScrapper")

@app.route("/")
def home():
  return "Hello! Welcome to mi casa!"

@app.route("/contact")
def anyName():
  return "Contact me!"

app.run()