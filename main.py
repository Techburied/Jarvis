import pyttsx3 # pip install pyttsx3

def speak(Text):
    engine = pyttsx3.init("sapi5") # module windows
    voice = engine.getProperty("voices") # property chahiye voice
    engine.setProperty("voice", voice[0].id) # set property "voice"
    engine.setProperty("rate", 200)
    print(f"jarvis: {Text}")
    engine.say(text=Text)
    engine.runAndWait()

speak("hello world!")

# speech recognition module / engine