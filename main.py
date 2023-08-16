import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import subprocess
import operator
import pyjokes
import pywhatkit
import ctypes
import os
import time
import requests
import pyautogui
from bs4 import BeautifulSoup
from datetime import date
from urllib.request import urlopen
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)



def temperature():
    city=qry.split("in",1)
    soup=BeautifulSoup(requests.get(f"https://www.google.com/search?q=weather+in+{city[1]}").text,"html.parser")
    region=soup.find("span",class_="BNeawe tAd8D AP7Wnd")
    temp=soup.find("div",class_="BNeawe iBp4i AP7Wnd")
    day=soup.find("div",class_="BNeawe tAd8D AP7Wnd")
    weather=day.text.split("m", 1)
    temperature= temp.text.split("C", 1)
    speak("Its currently "+weather[1]+" and "+temperature[0]+"celcius"+"in"+region.text)
    print("Its currently "+weather[1]+" and "+temperature[0]+"celcius"+"in"+region.text)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    h=int (datetime.datetime.now().hour)
    if h>=0 and h<12:
       speak("Good Morning!")

    elif h>=12 and h<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hello I am Zolo. How can I assist you?")

def command():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening speech...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing speech...")
        qry=r.recognize_google(audio,language='en-in'or 'hi-In')
        print(f"User said: {qry}\n")
    except Exception as e:
        print("Can you repeat please...")
        return "Sorry I didn't get that!"
    return qry
if __name__ == "__main__":
    wish()
    while True:
        qry= command().lower()
        if "how are you"in qry or'tum kaise ho' in qry:
            speak("I'm fine sir, how may i help you ?")
            

        elif "university name"in qry or 'tum kahan se ho' in qry:
            speak("Jaypee institute of information technology")
            

        elif "names of group members" in qry or 'who made you'in qry or 'tumhen kisne banaya hai' in qry:
            speak("I was made by Mohit, Ashwin, Archit and Janvi")
            


        elif "what can you do" in qry or 'tum kya kar sakte ho' in qry:
            speak('''i represent the theme BACK TO THE FUTURE. i can do anything you want me to. just give me command''')
            

        elif "who are you" in qry or 'tum kaun ho' in qry:
            speak("Sir I am your personal assistant Xolo")
            


        elif 'who is' in qry or 'what is' in qry or 'wikipedia' in qry:
            speak('Searching...please wait')
            qry = qry.replace("wikipedia", "")
            results =  wikipedia.summary(qry, sentences = 2)
            speak("Accoroding to google")
            print(results)
            speak(results)
            


        elif'open youtube' in qry or 'youtube kholo' in qry:
            webbrowser.open("youtube.com")
            

            
        elif 'play' in qry or 'bajao' in qry:
            song=qry.replace('play',"")
            speak('playing')
            pywhatkit.playonyt(song)
            


        elif 'open google' in qry or 'google kholo' in qry:
            webbrowser.open('https://www.google.co.in/')
            


        elif 'what is the time' in qry or 'can you tell the time' in qry or 'time batao' in qry or 'kya time' in qry or 'time batao' in qry:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")
            speak(f"Sir, the time is {strTime}")
            


        elif 'what is the date' in qry or 'can you tell the date' in qry or 'kya din' in qry:
            strdate = date.today()
            speak(f"Sir, the date is {strdate}")
            


        elif 'search' in qry :
            qry = qry.replace("search", "")
            webbrowser.open(qry)
            


        elif 'why were you made' in qry or 'reason for your existence' in qry:
            speak("I was created as a project for O S D HACK 2023  ")
            


        elif '143' in qry:
            speak("I Love You ")
            


        elif '5401314' in qry:
            speak("I will Love You for a lifetime. i will love you forever")
            

        

        elif 'lock window' in qry or 'lock system' in qry or 'system lock kar do' in qry:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
                



        
        elif "open" in qry:
            qry = qry.replace("open","")
            qry= qry.replace("xolo","")
            pyautogui.press("super")
            pyautogui.typewrite(qry)
            pyautogui.press("enter")
            



        
        elif 'shutdown system' in qry or 'computer band kar do' in qry:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                os.system('shutdown /s /t 1')
                

                
        elif "temperature" in qry or "weather forecast" in qry:
             temperature()
             


        elif "do some calculations" in qry or "can you calculate" in qry:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("say what you want to calculate, example: 3 plus 3")
                print("Listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string=r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return {
                    '+' : operator.add,
                    '-' : operator.sub,
                    'x' : operator.mul,
                    'divided': operator.__truediv__,
                    }[op]
            def eval_binary_expr(op1, oper, op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("your result is")
            speak(eval_binary_expr(*(my_string.split())))
            

            

        elif "hibernate" in qry or "sleep" in qry or 'sleep mode me jaao'in qry:
            speak("Hibernating")
            os.system(r'rundll32.exe powrprof.dll,SetSuspendState Hibernate')
            


        elif "joke sunao" in qry or 'tell jokes' in qry or 'joke' in qry :
            speak(pyjokes.get_joke())
            


        elif "log of" in qry or "sign out" in qry:
            speak("Make sure all the application are closed before sign-out")
            subprocess.call(["shutdown", "/l"])
            

        elif 'Xolo shutdown' in qry or 'bi' in qry or 'buy' in qry or 'close yourself' in qry or'bye xolo' in qry or 'bye solo' in qry:
            speak("it was nice serving you but it's time to say good bye")
            os._exit(0)  


       

