import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source: #whatever user says it will convert into text
        audio = r.listen(source)
    try:
        voice_data = ""
        voice_data = r.recognize_google(audio)
        print(voice_data)
        return voice_data
    except sr.UnknownValueError:
        print("Sorry,It is an error ")
    except sr.RequestError:
        print("Sorry,It is an Request error ")






