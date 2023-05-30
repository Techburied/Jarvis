from items import speak, listen
import bs4, requests, datetime # pip install bs4 requests pyautogui datetime -> cmd
from pyautogui import *

def tasks():
    while True:
        query = listen() # jo mai bolne wala hu

        if "time" in query:
            # time = datetime.datetime.now().strftime("%H:%M:%S %p") # 24 hour format
            time = datetime.datetime.now().strftime("%I:%M:%S %p") # 12 hour format
            speak(time)
        
        elif "date" in query:
            date = datetime.datetime.now().strftime("%D")
            speak(date)
            
        elif "day" in query:
            day = datetime.datetime.now().strftime("%A")
            speak(day)
            
        elif "temperature" in query:
            q = "temperature in jaipur"
            r = requests.get(f"https://www.google.com/search?q={q}")
            data = bs4.BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"the temperature outside is {temp}")
            
            speak("do you want another place temperature")
            place = listen()
            if "yes" in place:
                speak("tell me the name of the place")
                next = listen()
                r = requests.get(f"https://www.google.com/search?q={next}")
                data = bs4.BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f"the temperature outside is {temp}")
            else:
                speak("no problem!")

        elif "open" in query: # open cmd
            query = query.replace("open","") # cmd
            press("win")
            sleep(.2)
            typewrite(query)
            sleep(.2)
            press("enter")

#next topic play songs on youtube

        

tasks()