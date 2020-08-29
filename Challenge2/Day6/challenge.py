import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")

url = "https://www.iban.com/currency-codes"

countries = []

request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")

tbody = soup.find("tbody")
#table
# thead
#   tr
#     th
#     th
#     th
#     th
# body
#   tr
#   tr
#   ...

rows = tbody.find_all("tr")

for row in rows:
  items = row.find_all("td")
  name = items[0].text
  code =items[2].text
  currency =items[1].text
  if name and code:
    if name != "No universal currency":
      country = {
        'name':name.capitalize(),
        'code': code,
        'currency': currency.capitalize(),
      }
      countries.append(country)

def ask():
  try:
    print("Where are you from? Choose a country by number.\n")
    choice = int(input("#: "))
    if choice > len(countries):
      print("Choose a number from the list.")
      ask()
    else:
      first_country = countries[choice]
      print(f"{first_country['name']}\n")

      print("Now choose another country.\n")
      choice = int(input("#: "))

      second_country = countries[choice]
      print(f"{second_country['name']}\n")

      print(f"How many {first_country['code']} do you want to convert to {second_country['code']}?\n")

      amount = int(input(""))

### if success ###

      exchange_url = f"https://transferwise.com/gb/currency-converter/{first_country['code'].lower()}-to-{second_country['code'].lower()}-rate?amount={amount}"
      print(exchange_url)

      exchange_request = requests.get(exchange_url)
      print(exchange_request.status_code)
      exchange_soup = BeautifulSoup(exchange_request.text, "html.parser")

      rate = (exchange_soup.find("span", {"class": "text-success"}).string)
      print(rate)

      res = amount * float(rate)

      conv = format_currency(res, "KRW", locale="ko_KR")

      print(f"{first_country['code']}{amount} is {conv}")

### ###

  except ValueError:
    print("That wasn't a number.")
    ask()


print("Welcome to CurrencyConvert PRO 2000")
for index, country in enumerate(countries):
  print(f"#{index} {country['name']}")

ask()