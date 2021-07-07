# ---- Jarvis Ai assistance---
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import  webbrowser
import os


#  to take voice we use sapi5 of windows
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Stark Sir. Please tell me how may i help you")
def takeCommand():
    '''
    it takes command from the user by micophone and returns string output
    '''
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("Listning...........")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        # print(e)
        print(" Say that again please")
        return "None"
    return query

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia.....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'play music' in query:
            # Enter the directory of your songs folder
            music_dir = 'G:\\music'
            songs =os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time 'in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'time is {strTime}')
