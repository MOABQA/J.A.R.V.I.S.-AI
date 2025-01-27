'''Welcome to J.A.R.V.I.S. visit https://github.com/MOABQA''' 
###############################################
''' IMPORTING MODULES '''

import speech_recognition as sr           # for listening
import pyttsx3 as sp                      # for speaking
import datetime as dt                     # for time
import webbrowser as wb                   # for opening links
import os                                 # for opening files

###################################################
''' VOICE SETUP '''

engine = sp.init()
voices = engine.getProperty('voices')           # get voices
speaking_speed = engine.getProperty('rate')     # get speaking speed
volume = engine.getProperty('volume')           # get volume
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',130)
engine.setProperty('volume',1)

#######################################################
''' LEARNING ZONE '''
activation_name = 'jarvis'
websites = {'google':'www.google.com','youtube':'www.youtube.com',
            'igeass':'www.igeaas.com','gmail':'www.gmail.com',
            'classroom':'https://classroom.google.com/h',
            'maths class':'link',
            'physics class':'link',
            'chemistry class':'link',
            'computer class':'link',
            'english class':'link',
            "principal's class":'link'}

apps = {'calculator':'calc','powerpoint':'powerpnt','file explorer':'explorer',
        'browser':'msedge','word':'winword','access':'msaccess','settings':'control',
        'python':'path'}

music_path = 'path'

google_search_link = 'https://google.com/search?q='

#################################################
''' FUNCTIONS '''
def speak(text):
    engine.say(text)
    engine.runAndWait()
    print('Jarvis:',text)

def say_something(text):
    index = text.index('say ')
    l = text[index+4:]
    speak(l)
    return l

def record_anything(text):
    index = text.index('record ')
    l = text[index+7:]
    speak('recording sir...')
    file = open('python recording.txt','w')
    file.write(l)

def text_input():
    answer = input('Please enter your query...')
    print('User:',answer)
    return answer.lower()

def listen():
    r = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                answer_audio = r.listen(source)
                answer = r.recognize_google(answer_audio , language = 'en-in').lower()
            if activation_name in answer:
                answer = answer.replace(activation_name+' ','')
                print('User:',answer)
                return answer
        except sr.UnknownValueError:
            print('...')
            continue
        except sr.RequestError:
            global count
            if count == 1:
                count += 1
                speak('Sorry sir my services are down...')
                speak('Let me switch to text based input...')
            text_input()

def greeting():
    hour = dt.datetime.today().hour
    speak('Assalamualaikum')
    if hour >= 0 and hour < 12:
        speak('Good morning sir')
    elif hour >= 12 and hour <= 15:
        speak('Good afternoon sir')
    else:
        speak('Good evening sir')

def time_now():
    speak('the time is ')
    speak(dt.datetime.today().time().strftime('%H hours %M minutes'))

def date_now():
    speak("today's date is")
    speak(dt.datetime.today().date().strftime('%dth %B %Y'))

def day():
    a = dt.datetime.today().day().strftime('%A')
    speak("it's",a)
    
def search(a):
    index = a.index('search ')
    speak('Just searching...')
    l = google_search_link + a[index+7:]
    wb.open_new_tab(l)

def open_anything(a):
    index = a.index('open ')
    l = a[index+5:]
    l = l.strip()
    speak('here you go...')
    if l in websites:
        website = websites[l]
        wb.open_new_tab(website)
    elif l in apps:
        app = apps[l]
        os.startfile(app)
    else:
        os.startfile(l.strip())

def close_anything(a):
    index = a.index('close ')
    l = a[index+6:]
    termination = 'TASKKILL /F /IM '+ l.strip() + '.exe'
    speak('terminating task...')
    os.system(termination)

def play_music():
    musics = os.listdir(music_path)
    for i in range (len(musics)):
        musics[i] = musics[i].lower()
    speak('which one sir')
    answer = listen()
    answer += '.mp3'
    if answer.startswith('s'):
        os.startfile(music_path + '\\' + musics[1])
    elif answer in musics:
        os.startfile(music_path + '\\' + musics[musics.index(answer)])

def add(a):
    index = a.index('add ')
    numbers = a[index+4:].split(',')
    result = 0
    speak('ok')
    for i in numbers:
        result += float(i)
    return result

def subtract(a):
    index = a.index('subtract ')
    numbers = a[index+9:].split(',')
    result = 0
    speak('ok')
    for i in range(len(numbers)-1,-1,-1):
        result = float(numbers[i]) - result
    return result
            
################################################
''' CODE '''

greeting()
count = 1
while True:
    try:
        answer = listen()
        if 'search' in answer:
            search(answer)
            
        elif 'open' in answer:
            open_anything(answer)

        elif 'close' in answer:
            close_anything(answer)

        elif 'play' in answer or 'music' in answer:
            play_music()

        elif 'say' in answer:
            say_something(answer)
            
        elif 'time' in answer:
            time_now()
            
        elif 'date' in answer:
            date_now()
            
        elif 'day' in answer:
            speak(day())

        elif 'add' in answer:
            speak(add(answer))
                
        elif 'subtract' in answer:
            speak(subtract(answer))
           
        elif 'your name' in answer or 'who are you' in answer:
            speak('My name is',activation_name,'your personal assistant')

        elif 'how are you' in answer:
            speak('Alhamdullilah fine!!')
            
        elif ('exit' in answer) or ('bye' in answer) or ('close' in answer):
            speak('bye bye sir')
            exit()
        
        else:
            speak("Sorry sir!!!! I don't know")
    except Exception as e:
        speak('Sorry sir there was an unexpected error')
        speak('the error was')
        speak(e)
        continue
