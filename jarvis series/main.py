from items import speak, listen
import bs4, requests, datetime, webbrowser # pip install bs4 requests pyautogui webbrowser datetime -> cmd
from pyautogui import *
import pywhatkit as kit # pip install pywhatkit -> cmd

def tasks():
    while True:
        query = listen() # jo mai bolne wala hu
        query = query.replace("jarvis","")

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

        elif "open" in query: 
            query = query.replace("open","")
            press("win")
            sleep(.2)
            typewrite(query)
            sleep(.2)
            press("enter")

        elif "play" in query: 
            query = query.replace("play ","")
            kit.playonyt(query)
            speak(f"ok boss, playing {query}")

        elif "website" in query: 
            query = query.replace("website","") 
            query = query.replace(" ","") 
            webbrowser.open(f"https://www.{query}.com")
            speak(f"ok boss, opening {query}")
            
        # specific news topic, headlines
        
tasks()