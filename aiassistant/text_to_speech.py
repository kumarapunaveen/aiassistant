import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 'rate-70') # Setting up a speech rate
    engine.say(text)
    engine.runAndWait()
