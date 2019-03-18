import requests
from tkinter import*
import json

#from bs4 import BeautifulSoup

#url="http://www.json-generator.com/api/json/get/chQLxhBjaW?indent=2"
def onclick():

    cityName=entryCity.get()
    url = "https://openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22".format(cityName)
    response=requests.get(url)
    print(response.text)
    data=json.loads(response.text)
    aa=data["main"]["temp"]
    labelShow.config(text='Temperature:'+str(aa))

window=Tk()

labelTitle= Label(window,text="Weather report")
labelTitle.pack()

labelCity=Label(window,text="Enter City :")
labelCity.pack()

entryCity=Entry(window)
entryCity.pack()

buttonShow=Button(window,text="Show",command=onclick)
buttonShow.pack()

labelShow=Label(window)
labelShow.pack()

window.mainloop()



