'''Welcome to J.A.R.V.I.S.'''
###############################################
''' IMPORTING MODULES '''

import speech_recognition as sr  # for listening
import pyttsx3 as sp  # for speaking
import datetime as dt  # for time
import webbrowser as wb  # for opening links
import os  # for opening files
from time import sleep  # for waiting
from pyautogui import locateOnScreen, press, click  # for gui automation

###################################################
''' VOICE SETUP '''

engine = sp.init()
voices = engine.getProperty('voices')  # get voices
engine.setProperty('voice', voices[0].id)  # set default voice
engine.setProperty('rate', 130)  # speaking speed
engine.setProperty('volume', 1)  # volume

#######################################################
''' LEARNING ZONE '''
activation_name = 'jarvis'
websites = {
    'google': 'www.google.com',
    'youtube': 'www.youtube.com',
    'igeass': 'www.igeaas.com',
    'gmail': 'www.gmail.com',
    'classroom': 'link',
    'maths class': 'link',
    'math class': 'link',
    'physics class': 'link',
    'chemistry class': 'link',
    'computer class': 'link',
    'english class': 'link',
    "principal's class": 'link'
}

apps = {
    'calculator': 'calc',
    'powerpoint': 'powerpnt',
    'file explorer': 'explorer',
    'browser': 'msedge',
    'word': 'winword',
    'access': 'msaccess',
    'settings': 'control',
    'python': 'path'
}

music_path = 'path'
google_search_link = 'https://google.com/search?q='

#################################################
''' FUNCTIONS '''


def speak(text):
    """Speak and print the provided text."""
    engine.say(text)
    engine.runAndWait()
    print('Jarvis:', text)


def say_something(text):
    """Extract and speak text after 'say' command."""
    index = text.index('say ')
    l = text[index + 4:]
    speak(l)
    return l


def record_anything(text):
    """Record text to a file."""
    index = text.index('record')
    l = text[index + 7:]
    with open('python recording.txt', 'w') as file:
        file.write(l)
    speak('Recorded, sir...')


def text_input():
    """Get text input from user."""
    answer = input('Please enter your query... ')
    print('User:', answer)
    return answer.lower()


def listen():
    """Listen for voice commands."""
    r = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                answer_audio = r.listen(source)
                answer = r.recognize_google(answer_audio, language='en-in').lower()
            if activation_name in answer:
                answer = answer.replace(activation_name + ' ', '')
                print('User:', answer)
                return answer
        except sr.UnknownValueError:
            print('...')
        except sr.RequestError:
            global count
            if count == 1:
                count += 1
                speak('Sorry sir, my services are down...')
                speak('Let me switch to text-based input...')
            return text_input()


def greeting():
    """Greet based on the current time."""
    hour = dt.datetime.now().hour
    speak('Assalamualaikum')
    if hour >= 0 and hour < 12:
        speak('Good morning sir')
    elif hour >= 12 and hour <= 15:
        speak('Good afternoon sir')
    else:
        speak('Good evening sir')


def time_now():
    """Speak the current time."""
    speak('The time is ')
    speak(dt.datetime.now().strftime('%H hours %M minutes'))


def date_now():
    """Speak the current date."""
    speak("Today's date is")
    speak(dt.datetime.now().strftime('%dth %B %Y'))


def day():
    """Speak the current day."""
    speak("It's " + dt.datetime.now().strftime('%A'))


def search(a):
    """Perform a Google search."""
    index = a.index('search ')
    speak('Just searching...')
    l = google_search_link + a[index + 7:]
    wb.open_new_tab(l)


def open_anything(a):
    """Open websites or applications."""
    index = a.index('open ')
    l = a[index + 5:].strip()
    speak('Here you go...')
    if l in websites:
        wb.open_new_tab(websites[l])
    elif l in apps:
        os.startfile(apps[l])
    else:
        os.startfile(l)


def close_anything(a):
    """Close running applications."""
    index = a.index('close ')
    l = a[index + 6:].strip()
    termination = f'TASKKILL /F /IM {l}.exe'
    speak('Terminating task...')
    os.system(termination)


def play_music():
    """Play music from a specified directory."""
    musics = [file.lower() for file in os.listdir(music_path) if file.endswith('.mp3')]
    speak('Which one, sir?')
    answer = listen() + '.mp3'
    if answer in musics:
        os.startfile(os.path.join(music_path, answer))
    else:
        speak("Sorry, I couldn't find that song.")


def add(a):
    """Add numbers given in the command."""
    index = a.index('add ')
    numbers = [float(num) for num in a[index + 4:].split(',')]
    result = sum(numbers)
    speak(f'The result is {result}')
    return result


def subtract(a):
    """Subtract numbers given in the command."""
    index = a.index('subtract ')
    numbers = [float(num) for num in a[index + 9:].split(',')]
    result = numbers[-1]
    for num in reversed(numbers[:-1]):
        result = num - result
    speak(f'The result is {result}')
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
        elif 'record' in answer:
            record_anything(answer)
        elif 'switch to text input' in answer or 'switch to text based input' in answer:
            answer = text_input()
        elif 'time' in answer:
            time_now()
        elif 'date' in answer:
            date_now()
        elif 'day' in answer:
            day()
        elif 'add' in answer:
            add(answer)
        elif 'subtract' in answer:
            subtract(answer)
        elif 'your name' in answer or 'who are you' in answer:
            speak(f'My name is {activation_name}, your personal assistant')
        elif 'how are you' in answer:
            speak('Alhamdulillah, fine!!')
        elif 'exit' in answer or 'bye' in answer or 'close' in answer:
            speak('Bye bye, sir')
            break
        else:
            speak("Sorry sir!!!! I don't know")
    except Exception as e:
        speak('Sorry sir, there was an unexpected error')
        speak(f'The error was {str(e)}')
