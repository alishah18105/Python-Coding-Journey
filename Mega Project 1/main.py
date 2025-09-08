import requests
import speech_recognition as sr
import webbrowser
import pyttsx3
import google.generativeai as genai
from music import musicLibrary

speech_recognizer = sr.Recognizer()
news_api_key = 'f23cc03a3eb74e469df4ad3e9517af5a'

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def processCommand(c):
    print(f"Processing command: {c}")  

    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open linkedin" in c.lower():
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
    elif "open facebook" in c.lower():
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
    elif c.lower().startswith("play music"):
        song_name = c.split("play music",1)[1].strip().lower()
        if song_name in musicLibrary:
            link = musicLibrary[song_name]
            webbrowser.open(link)
            speak(f"Playing {song_name}")
        else:
            speak(f"Sorry, I don't have {song_name} in the music library.")
    elif "news" in c.lower():
        speak("Fetching the latest news")
        news = requests.get(f'https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}')
        if news.status_code == 200:
            articles = news.json().get('articles', [])
            for article in articles:
                speak(article['title'])
    else:
            genAi(c)

def genAi(command):

    API_KEY = "AIzaSyDtFvOygqfyqcUMEbOov3tsrbxR8o5_1DI"

    genai.configure(api_key=API_KEY)

    try:
        # Create a model instance
        model = genai.GenerativeModel("gemini-1.5-flash")

        # Send a test prompt
        response = model.generate_content(command)

        # Print the output
        speak(response.text)

    except Exception as e:
        print("❌ API Key Test Failed")
        print("Error:", e)


        
if __name__ == "__main__":
    speak("Hello, how can I assist you today?") 
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        try:
            word  = r.recognize_google(audio)
            print(f"You said: {word}")
            if word.lower() == "jarvis":
                speak("Yes Sir")

                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command  = r.recognize_google(audio)
                    processCommand(command)



        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            continue
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            continue
