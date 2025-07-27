import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio

# Initialising the engine:
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Function to speak the text:
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Wish me function:
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        wish = "Good Morning sir"
        speak(wish)
        print(wish)

    elif hour >= 12 and hour < 18:
        wish = "Good Afternoon sir"
        speak(wish)
        print(wish)
    else:
        wish = "Good Evening sir"
        speak(wish)
        print(wish)

# Jarvis introduction:
def intro():
    speak("Hello I am Jarvis, Please tell me how may I help you?") 

# Function to take command from the user using microphone and convert it into string:
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    # Recognize using google:
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

# Main function:
if __name__ == "__main__":
    wishMe()
    intro()
    takeCommand()
