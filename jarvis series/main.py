from items import speak, listen
import bs4, requests, datetime, webbrowser, GoogleNews # pip install bs4 requests pyautogui webbrowser datetime googlenews -> cmd
from pyautogui import *
import pywhatkit as kit # pip install pywhatkit -> cmd
import speedtest # pip install speedtest-cli -> cmd


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
            
        elif "news of" in query: 
            query = query.replace("news of ","")
            new = GoogleNews.GoogleNews()
            speak(f"getting news of {query}")
            new.get_news(query)
            new.result()
            a = new.gettext()
            speak(a[1:5])

        elif "headlines" in query or "headline" in query: 
            new = GoogleNews.GoogleNews()
            speak("getting fresh headlines")
            new.get_news("headlines")
            new.result()
            a = new.gettext()
            speak(a[1:10])
        
        elif "speed test" in query:
            speed = speedtest.Speedtest()
            speak("checking")
            ul = speed.upload()
            ul = int(ul/800000)
            dl = speed.download()
            dl = int(dl/800000)
            speak(f"your upload speed is {ul} mbp s and your download speed is {dl} mbp s")
        
#changed heeheh
        
tasks()
