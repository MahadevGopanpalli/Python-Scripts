
import requests
from bs4 import BeautifulSoup

url="https://www.worldometers.info/coronavirus/"

r = requests.get(url)

s= BeautifulSoup(r.text,"html.parser")

data= s.find_all("div",class_='maincounter-number')

print("Total Case :",data[0].text.strip())
print("Total Deaths :",data[1].text.strip())
print("Total Recoveries :",data[2].text.strip())
