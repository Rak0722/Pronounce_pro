import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
from tkinter import messagebox
import pyttsx3
import wikipedia
import os



root = Tk()
root.title("Phonetics Pro")
root.geometry("500x500")
root.resizable(False,False)
root.config(bg="#577284")


##icon......................................................  #939597   #577284   #E08119
image_icon=PhotoImage(file = ('icon.png'))

# root.iconbitmap('icon.ico')
root.iconphoto(False  ,image_icon)


##top frame........................................................................
Top_frame=Frame(root,bg="#EDF1FE",width=500,height=120)
Top_frame.place(x=0,y=0)

Logo=PhotoImage(file=('mic.png'))
Label(Top_frame,image=Logo,bg="#EDF1FE").place(x=10,y=5)


#main declaration..................................................................
speech = pyttsx3.init()


#define function for text to speech.........................................
def mySpeak():
    text=Text.get()
    gender=gender_combobox.get()
    speed=speed_box.get()
    voices=speech.getProperty("voices")

    
    def setvoice():
        if (gender == "MALE"):
            speech.setProperty("voice",voices[0].id)
            speech.setProperty("volume",1)
            speech.say(text)
            speech.runAndWait()
        else:
            speech.setProperty("voice",voices[1].id)
            speech.setProperty("volume",1)
            speech.say(text)
            speech.runAndWait()


    if(text):
        if(speed == "FAST"):
            speech.setProperty("rate",250)
            setvoice()
        elif(speed == "MEDIUM"):
            speech.setProperty("rate",150)
            setvoice()
        else:
            speech.setProperty("rate",60)
            setvoice()

def download():
    text=Text.get()
    gender=gender_combobox.get()
    speed=speed_box.get()
    voices=speech.getProperty("voices")

    
    def setvoice():
        if (gender == "MALE"):
            speech.setProperty("voice",voices[0].id)
            speech.setProperty("volume",1)
            path = filedialog.askdirectory()
            os.chdir(path)
            speech.save_to_file(text,"text.mp3")    
            speech.runAndWait()
        else:
            speech.setProperty("voice",voices[1].id)
            speech.setProperty("volume",1)
            path = filedialog.askdirectory()
            os.chdir(path)
            speech.save_to_file(text,"text.mp3")
            speech.runAndWait()


    if(text):
        if(speed == "FAST"):
            speech.setProperty("rate",250)
            setvoice()
        elif(speed == "MEDIUM"):
            speech.setProperty("rate",150)
            setvoice()
        else:
            speech.setProperty("rate",60)
            setvoice()

# HEADING........................................................................
Label(root, text = " Phonetics Pro ", font=("Times 25 bold italic "),bg="#EDF1FE",fg="black").place(x=150,y=40)
frame1 = Frame(root)

#footer....................................................................................
Label(root, text = " \u00A9 Rights Reserved", font=("Helvetica 9 bold italic"),bg="#577284",fg="#EDF1FE").place(x=370,y=480)
frame2 = Frame(root)

#LABEL AND ENTRY BOX................................................
Label(frame1,text="Type Something...",font=("Helvetica 16 bold italic")).pack(pady=5)

Text = Entry(frame1,width=40, textvariable=Text,font=("Helvetica 15"))
Text.place(x=10,width=50,height=250)
frame2.place(x=30,y=205)
Text.pack(side=LEFT,expand=True)
frame1.pack(pady=150)


#gender ..................................................................................
gender_combobox=Combobox(root,values=["MALE","FEMALE"],font="arial 14 bold",state="r",width=16)
gender_combobox.place(x=270,y=250)
gender_combobox.set("MALE")

#speed ...................................................................................
speed_box=Combobox(root,values=["FAST","MEDIUM","SLOW"],font="arial 14 bold",state="r",width=16)
speed_box.place(x=30,y=250)
speed_box.set("MEDIUM")

#speak button......................................................................
btn=Button(root, text="Speak",font=("helvetica 15 bold "),fg = "#577284",bg="light blue",command=mySpeak,width=16)
btn.place(x=30,y=300)

#clear button........................................................................
def delete():
    Text.delete("0","end")

Button(root, text="Clear ",font=("Helvetica 15 bold "),fg = "#577284",bg="light blue",command=delete,width=16).place(x=30,y=350)

#Exit command.......................................................................
def on_exit():
    answer = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if answer:
        root.destroy()

btn=Button(root, text=" Exit ",font=("Helvetica 15 bold "),fg = "white",bg="red",command=on_exit,width=16)
btn.place(x=270,y=350)

#SAVE BUTTON.......................................................................
btn=Button(root, text="SAVE",font=("helvetica 15 bold "),fg = "#577284",bg="light blue",command=download,width=16)
btn.place(x=270,y=300)




root.mainloop()


## Pronounce Pro python project executed sucessfully 

