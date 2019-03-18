import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.cricbuzz.com/live-cricket-scorecard/21533/ind-vs-aus-2nd-odi-australia-tour-of-india-2019"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
print("Fetching title of page :")
print(soup.title.text)
print(soup.prettify())


divTags=soup.find_all("div",class_="cb-col cb-col-100 cb-ltst-wgt-hdr")
for tags in divTags:
    print(tags.text)





