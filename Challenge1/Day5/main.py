import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

print("Hello! Please choose select a country by number:")

URL = "https://www.iban.com/currency-codes"
result = requests.get(URL)
soup = BeautifulSoup(result.text, "html.parser")
tbody = soup.find("tbody")
tr = tbody.find_all('tr')

count = 0
contents = []

for td in tr:
  #contents.append(td.string)
  td1 = td.get_text()
  contents.append(td1)
#print(contents)

nation_list = []
for content in contents:
  lines = content.split("\n")
  put = []
  #print(lines)
  for line in lines:
    #print(line)
    put.append(line)
  if put[4] == "":
    continue
  else:
    nation_list.append(put)
    count = count + 1
#print(nation_list)

#print(count)
#print(nation_list[0][1])
#print(nation_list[1][1])

index = 0
for _ in range(count):
  nation_list[index][4] = index
  print(f"# {nation_list[index][4]} {nation_list[index][1]}")
  index = index+1

while True:
  user_input = (input("#: "))
  try:
    answer = int(user_input)
    if answer >= 265:
      print("Choose a number from the list")
      continue
    else:
      index = 0
      for _ in range(count):
        if nation_list[index][4] == answer:
          print(f"You chose {nation_list[index][1]}")
          print(f"The curreny code is {nation_list[index][3]}")
          break
        else:
          index = index + 1
          continue
      break

  except:
    print("That wasn't a number.")
    continue