import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the TTS engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print("You said:", query)
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, there was a network issue.")
        return ""

def get_time():
    return datetime.datetime.now().strftime("%I:%M %p")

def get_date():
    return datetime.datetime.now().strftime("%A, %B %d, %Y")

def search_web(query):
    speak(f"Searching for {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")

def handle_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "time" in command:
        speak(f"The time is {get_time()}")
    elif "date" in command:
        speak(f"Today's date is {get_date()}")
    elif "search" in command:
        query = command.replace("search", "").strip()
        if query:
            search_web(query)
        else:
            speak("What would you like me to search for?")
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        return False
    else:
        speak("I didn't understand that command.")
    return True

def run_assistant():
    speak("Voice assistant is now active.")
    while True:
        command = listen()
        if command:
            if not handle_command(command):
                break

# Start the assistant
run_assistant()
