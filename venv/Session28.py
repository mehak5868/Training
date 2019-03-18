import requests
from bs4 import BeautifulSoup

url="https://www.ndtv.com/india?pfrom=home-topnavigation"
response=requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
print(soup.prettify())

print("fetching title")
print(soup.title.text)

divtags=soup.find_all("div",class_="nstory_header")
for tags in divtags:
    print(tags.text)