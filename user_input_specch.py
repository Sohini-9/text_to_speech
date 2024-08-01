from gtts import gTTS
import os
from tkinter import *

root = Tk()
canvas = Canvas(root,width=400,height=300)
canvas.pack()

def textToSpech():
    text = entry.get()
    language = 'en'
    output = gTTS(text=text,lang=language,slow=False)
    output.save('output1.mp3')
    os.system("start output1.mp3")

entry = Entry(root)
canvas.create_window(200,180,window=entry)

button = Button(text="Start",command=textToSpech)
canvas.create_window(200,230,window=button)

root.mainloop()