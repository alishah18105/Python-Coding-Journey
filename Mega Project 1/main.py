import speech_recognition as sr
import webbrowser
import pyttsx3

speech_recognizer = sr.Recognizer()

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
