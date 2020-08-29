import os
import requests
#from bs4 import BeautifulSoup

#days = ("Mon", "Tue", "Wed", "Thu", "Fri")

#for day in days:
  #if day == "Wed":
    #break
  #else:
    #print(day)

#from math import ceil, fsum

#print(ceil(1.2))
#print(fsum([1, 2, 3, 4, 5, 6, 7]))

#from math import fsum as f_nickname

#print(f_nickname([1, 2, 3, 4, 5, 6, 7]))

## how to get another file ##
#from calculator import plus

#print(plus(1,2))
## how to get another file ##

#indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")


# s.strip = erase the blankspace
# s.lower = make all alphabets to lower-case
# s.split(',') = divide the string betweent ',' to list contents




while True:

  check = 0

  print("Welcome to IsItDown.py!")
  print("Please wirte a URL or URLs you want to check. (separted by comma)")

  s = input("").replace(" ","")
  s = s.lower()

  letter = s.split(',')

  try:
    for Web in letter:
      if '.com' not in Web:
        print(f"{Web} is not a valid URL")
      else:
        if 'http://' not in Web:
          Web = 'http://' + Web
        if requests.get(Web).status_code == 200:
          print(f"{Web} is up!")
  except:
    print(f"{Web} is down!")
  #### #### #### #### ####
  while True:
    answer = input("Do you want to start over? y/n ")
    if answer == "y":
      check = 1
      break
    elif answer == "n":
      break
    else:
      print("That's not a valid answer")
  
  if check == 1:
    continue

  print("k, bye!")
  break