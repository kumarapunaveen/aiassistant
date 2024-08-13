import text_to_speech
import speech_to_text

import datetime #for time and date
import webbrowser #for opening browser


import os

import battery
import evalu

import extractdetails
import translate


def Action(data):
    user_data = data.lower()

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is virtual assistant")
        return "My name is virtual assistant"

    elif "hello" in user_data:
        text_to_speech.text_to_speech("Hello, how can I assist you today?")  
        return   "Hello, how can I assist you today?"
    
    elif "good morning" in user_data:
        text_to_speech.text_to_speech("Good morning, how can I assist you today?")
        return "Good morning, how can I assist you today?"

    elif "time now" in user_data or "time" in user_data:
        current_time = datetime.datetime.now()
        Time = (str)(current_time) + "Hour :" , (str)(current_time.minute) + "Minute"
        text_to_speech.text_to_speech(Time)
        return Time

    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("ok sir")
        return "ok sir"

    elif "play music" in user_data:
        webbrowser.open("https://gaana.com/") #we can pass the link we want
        text_to_speech.text_to_speech("ganna is now ready for u to listen music")
        return "ganna is now ready for u to listen music"

    elif "open youtube" in user_data or "youtube" in user_data:
        webbrowser.open("https://youtube.com/") #we can pass the link we want
        text_to_speech.text_to_speech("you tube  is now ready for u ")
        return "you tube  is now ready for u "

    elif "open google" in user_data or "google" in user_data:
        webbrowser.open("https://google.com/") #we can pass the link we want
        text_to_speech.text_to_speech("google is now ready for u")
        return "google is now ready for u "


    elif "weather" in user_data:
        webbrowser.open("https://weather.com/") #we can pass the link we want
        text_to_speech.text_to_speech("weather is now ready for u ")
        return "weather is now ready for u"

    elif "myfiles" in user_data:
        directory = r"D:\aiassistant"
        files = os.listdir(directory)
        print(files)
        text_to_speech.text_to_speech("your files are now ready for u ")
        return "your files are now ready for u "
    
    elif 'music laptop' in user_data:
        url = 'D:\\music' 
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        text_to_speech.text_to_speech("playing songs in my laptop ")
        return "songs playing" 
    
    elif "good night" in user_data:
        text_to_speech.text_to_speech("Good night, sleep well!")
        return "Good night, sleep well!"

    
    elif "thank you" in user_data:
        text_to_speech.text_to_speech("You're welcome!")
        return "You're welcome!"
    
    elif "set timer" in user_data:
        time = int(re.findall(r'\d+', user_data)[0])
        text_to_speech.text_to_speech(f"Timer set for {time} minutes")
        time.sleep(time * 60)
        text_to_speech.text_to_speech("Time's up!")
        return "Timer ended"
    
    elif "battery status" in user_data or "battery" in user_data:
        battery_status = battery.get_battery_status()  
        text_to_speech.text_to_speech(f"The current battery status is {battery_status}%")
        return f"The current battery status is {battery_status}%"
    
    elif "translate" in user_data:
        phrase, target_language = extractdetails.extractdetails(user_data)  
        translated_phrase = translate.translate(phrase, target_language)  
        text_to_speech.text_to_speech(f"{phrase} in {target_language} is {translated_phrase}")
        return f"{phrase} in {target_language} is {translated_phrase}"
    
    elif "calculate" in user_data:
        expression = user_data.split("calculate")[-1].strip()
        result = evalu.evaluate(expression)
        text_to_speech.text_to_speech(f"The result of {expression} is {result}")
        return f"The result of {expression} is {result}"

    else:
        text_to_speech.text_to_speech("I am not able to understand")
        return "I am not able to understand"