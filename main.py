import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechrecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib

print("Initializing jarvis")

MASTER = "harshit sir"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# speak function will pronuce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()
# This function will wish you as per the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning" + MASTER)

    elif hour >= 12 and hour < 18:
        speak("Good AfterNoon" + MASTER)

    else:
        speak("Good Evining" + MASTER)

   

 # speak("I am jarvis. how may i help you?" + MASTER)
 
# This function will take command from the microphone


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that angin plase")
        query = None

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('22harshitj@gmail.com', 'Sjiis@1008')
    server.sendmail("shreyansh@121insurance.in ", to, content)
    server.close()

# Main program start here..

def main():
    # speak("initializing jarvis")
    wishMe()
    qurey = takeCommand()

    # logic for executing tasks as per the qurey 
    if 'wikipedia' in qurey.lower():
        speak('Searching  wikipedia...')
        qurey = qurey.replace("wikipedia", "")
        results = wikipedia.summary(qurey, sentences =2)
        print(results)
        speak(results)

    elif 'youtube' in qurey.lower():
        speak("opening youtube")
        webbrowser.open("https://www.youtube.com/")

    elif 'google' in qurey.lower():
        speak("opening google")
        webbrowser.open("https://www.google.com/")

    elif 'ryan' in qurey.lower():
        speak("opening topper os for study")
        webbrowser.open("https://ryangroup.toppr.school/")
        
    elif 'topper' in qurey.lower():
        speak("opening topper for live class")
        webbrowser.open("https://www.toppr.com/") 

    elif 'gmail' in qurey.lower():
        speak("opening gmail of connectharshitjain@gmail.com")       
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox") 

    elif 'harshit' in qurey.lower():
        speak("opening gmail of 22harshitj7e@gmail.com")
        webbrowser.open("https://mail.google.com/mail/u/1/#inbox")

    elif 'white hat' in qurey.lower():
        speak("opening white hat for coding")  
        webbrowser.open("https://code.whitehatjr.com/s/dashboard")

    elif 'class' in qurey.lower():
        speak("opening byjus for class")  
        webbrowser.open("https://learn.byjus.com/home/dashboard")

    elif 'exam' in qurey.lower():
        speak("opening google met for exam")  
        webbrowser.open("https://meet.google.com/kts-vspg-krr")

    elif 'drive' in qurey.lower():
        speak("opening drive")  
        webbrowser.open("https://drive.google.com/drive/u/0/my-drive")

    elif 'play music' in qurey.lower():
        songs_dir = "C:\\Users\\shrey\\Desktop\\jarvis\\what app danger"
        songs = os.listdir(songs_dir)
        speak("playing whatapp danger")
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'play up' in qurey.lower():
        songs_dir = "C:\\Users\\shrey\\Desktop\\jarvis\\way up"
        songs = os.listdir(songs_dir)
        speak("playing Way Up")
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'play hide' in qurey.lower():
        songs_dir = "C:\\Users\\shrey\\Desktop\\jarvis"
        songs = os.listdir(songs_dir)
        speak("playing hide")
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))
        
    elif 'time' in qurey.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak("telling time")
        print(strTime)
        speak(f"{MASTER} the time is {strTime}") 

    elif 'open code' in qurey.lower():
        codePath = "C:\\Users\\shrey\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        speak("please wait opening code")
        os.startfile(codePath)

    elif 'open discord' in qurey.lower():
        codePath = "C:\\Users\\shrey\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc"
        speak("please wait opening discord")
        os.startfile(codePath)    

    elif 'open web server' in qurey.lower():
        codePath = "C:\\Users\\shrey\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Chrome Apps"
        speak("please wait opening web server for chrome")
        os.startfile(codePath) 

    elif 'open power' in qurey.lower():
        codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Windows PowerShell"
        speak("please wait opening powersell window")
        os.startfile(codePath)      

    elif 'sunflower' in qurey.lower():
        songs_dir = "C:\\Users\\shrey\\Desktop\\jarvis\\sunflower\\"
        songs = os.listdir(songs_dir)
        speak("playing sunflower")
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'email to papa' in qurey.lower():
        try:
            speak("What should I send")
            content = takeCommand()
            to = "shreyansh@121insurance.in"
            sendEmail(to, content)
            speak("Email has been sent successfully")
        except Exception as e:
            print(e)

main()