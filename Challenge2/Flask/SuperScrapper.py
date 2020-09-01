from flask import Flask

app = Flask("SuperScrapper")

@app.route("/")
def home():
  return "Hello! Welcome to mi casa!"

@app.route("/<username>")
def anyName(username):
  return f"{username} hello!"

app.run("0.0.0.0")