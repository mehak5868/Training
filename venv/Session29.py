import requests
from bs4 import BeautifulSoup

url="https://www.imdb.com/india/top-rated-indian-movies/"
response=requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
#print(soup.prettify())

movies=[]
dt = soup.find_all("td",class_="titleColumn")
for m in dt:
    mov=m.text.strip()
    #print(mov)
    mov1= mov[0:4]
    print(mov1.strip())
    movies.append(mov1.strip())

print(movies)
movies1=[]
for n in dt :
    mov2 = n.text.strip()
    #print(mov2)
    mov3 = mov2[9:41]
    print(mov3.strip())
    movies1.append(mov3.strip())
print(movies1)

#for m2 in movies1:
