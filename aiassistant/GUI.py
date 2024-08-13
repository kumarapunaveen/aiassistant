#building userinterface using tkinter
from tkinter import *
from PIL import Image,ImageTk


import speech_to_text
import action
import battery

root = Tk() #object
root.title("AI Assistant")
root.geometry("550x675") #width and length, but with this we can resize
root.resizable(False,False)
root.config(bg="#F5F5DC")


#functions defined below
def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.Action(user_val)
    text.insert(END,'User-->'+user_val+"\n")
    if bot_val != None:
        text.insert(END,"Bot<--"+str(bot_val)+"\n")
    if bot_val == "ok sir":
        root.destroy()

def enter():
    enter = entry.get()
    bot = action.Action(enter)
    text.insert(END,'User-->'+enter+"\n")
    if bot != None:
        text.insert(END,"Bot<--"+str(bot)+"\n")
    if bot == "ok sir":
        root.destroy()


def delete():
    text.delete('1.0', "end")


#making a frame
frame = LabelFrame(root , padx=100, pady=7, borderwidth=3, relief="raised") #relief is the styling
frame.config(bg="#36454F")
#put frame in root directory by 2 methods called grid or packed
frame.grid(row = 0, column=1, padx=55, pady=10)

#inserting details in the frame
#text label
text_label= Label(frame ,  text="AI Assistant" , font=("comic Sans" , 14, "bold") , bg="#ffffff" )
text_label.grid(row=0 , column=0 , padx=20 , pady=10)
#to integrate jpg or png images into tkinter we have to install 'pillow' in rhe terminal

image = ImageTk.PhotoImage(Image.open("images/img3.jpeg"))
image_label = Label(frame , image=image)
image_label.grid(row=1, column=0, pady=20)

#adding a text widget
text = Text(root, font=('courier 10 bold'), bg="#C8E6C9")
text.grid(row=2 , column=0)
text.place(x=100 , y=420 , width=375, height=100) #usedfor placing the text ; x,y are locations(x is the place form left end, y is from top); width and height space inside the box

#entry widget
entry = Entry(root , justify=CENTER)
entry.place(x=100, y= 545, width=350 , height=30)

#buttons
button1 = Button(root, text="ASK", bg="#FF6F61", pady=16, padx=40, border=3 , relief=SOLID, command=ask) #command is the function to done while clcking on button
button1.place(x=70 , y=600)

button2 = Button(root, text="ENTER", bg="#FF6F61", pady=16, padx=40, border=3 , relief=SOLID, command=enter) #command is the function to done while clcking on button
button2.place(x=400 , y=600)

button3 = Button(root, text="DELETE", bg="#FF6F61", pady=16, padx=40, border=3 , relief=SOLID, command=delete) #command is the function to done while clcking on button
button3.place(x=225 , y=600)

root.mainloop()

#this is the complete UI
#part 2 is speech to text, for this import some libraries
#1.speechrecognition- pip install SpeechRecognition==3.8.1
#2.pyaudio - pip install PyAudio
#3.for texttospeech install pyttsx3 2.90