import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init('sapi5') # sapi5 used to take voice
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id) # it sets the male and female voices
def speak(audio):
    engine.say(audio) #it will help to speak the audio given as input
    engine.runAndWait() 

def wishme():
    hour=int(datetime.datetime.now().hour) #date and time function is used to get hour format
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Voxxa sir,How may i help you")

def take():
    '''
    It takes microphone inputs from the user and returns string output
    '''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1 # seconds of non-speaking audio before a phrase is considered complete
        r.energy_threshold=500 # minimum audio energy to consider for recording
        audio=r.listen(source)

    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        #print(e)

        print("say that again please....")
        return 'None'
    return query
def sendEmail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('allenlivephysics@gmail.com','y8acszecv')
    server.sendmail('allenlivephysics@gmail.com',to,content)
    server.close()

if __name__== '__main__':
    #speak("Hey Ashutosh , Good Job")
    wishme()
    #while True:
    if 1:
        query=take().lower()
        #logic for executing  tasks based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia....")
            query=query.replace("Wikipedia",'')
            result=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'play music' in query:
            music_dir='C:\\Users\\imash\\OneDrive\\Desktop\\music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")
        elif 'open code' in query:
            codepath="C:\\Users\\imash\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'email to ashutosh' in query:
            try:
                speak("What should I say")
                content = take()
                to = "ashutoshdhawan2003@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                speak("I am not able to send this email")
            