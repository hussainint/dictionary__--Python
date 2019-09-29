import requests
from bs4 import BeautifulSoup
inp=input("Enter the word")
web = requests.get('https://en.oxforddictionaries.com/definition/'+inp)

data = web.content

soup = BeautifulSoup(data,features="lxml")

tag = soup.find_all("span","ind")
a=1
for i in tag:
	print(a,". ",i.text)
	a=a+1
