import speech_recognition as sr # for speaking response
import pyttsx3 # for understandig commands
import datetime # for current date and time 
import webbrowser # for basic feature on Google search.

# Setup
engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio).lower()
    except:
        speak("Sorry, I didn't catch that.")
        return ""

# Assistant logic
speak("Hi! I am your assistant. How can I help?")

while True:
    command = listen()

    if "hello" in command:
        speak("Hello there!")
    elif "time" in command:
        speak(datetime.datetime.now().strftime("It is %I:%M %p"))
    elif "date" in command:
        speak(datetime.datetime.now().strftime("Today is %B %d, %Y"))
    elif "search" in command:
        query = command.replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching for {query}")
    elif "stop" in command or "exit" in command:
        speak("Goodbye!")
        break
    else:
        speak("Please say that again.")
