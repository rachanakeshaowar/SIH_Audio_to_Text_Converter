import speech_recognition as sr
import pyaudio
import wave
from tkinter import *
from threading import *
from pydub import AudioSegment
from tkinter import filedialog
from datetime import date
import webbrowser
import random
def changeOnHover(button, colorOnHover, colorOnLeave):
        button.bind("<Enter>", func=lambda e: button.config(
            background=colorOnHover))
        button.bind("<Leave>", func=lambda e: button.config(
            background=colorOnLeave))
def changetextOnHover(button, colorOnHover, colorOnLeave):
        button.bind("<Enter>", func=lambda e: button.config(
            fg=colorOnHover))
        button.bind("<Leave>", func=lambda e: button.config(
            fg=colorOnLeave))
def threading():
        t1=Thread(target=textconver)
        t1.start()
def browseFiles():
    global filename
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    if(len(filename)==0):
        pass
    else:
        label_file_explorer.configure(text="File Opened: "+filename)
        
        