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
def textconver():
    global filename
    print(len(filename))
    if(len(filename)==0):
        Output.delete("1.0","end")
        Output.insert(END, "Please choose voice recording file first")
    else:
        Output.delete("1.0","end")
        Output.insert(END, "Converting....Wait for while")
        print('Converting....Wait for while')
        m4a_file = filename
        wav_filename = "random.wav"
        track = AudioSegment.from_file(m4a_file,  format= 'm4a')
        file_handle = track.export(wav_filename, format='wav')
    try:
            audio_file = sr.AudioFile(file_handle)
            with audio_file as source:
                r.adjust_for_ambient_noise(source)
                audio = r.record(source)
            result = r.recognize_google(audio)
            num = random.randrange(1,1000000000000000000)
            a=(str)(num)
            INPUT = 'random'+a+'.txt'
            with open(INPUT,mode ="w") as file:
                file.write("Recognized text:")
                file.write("\n")
                file.write(result)
                print("Conversion is completed and file is saved as ",INPUT)
            Output.delete("1.0","end")
            Output.insert(END, f"Conversion is completed and file is saved as {INPUT}")
    except:
            Output.delete("1.0","end")
            Output.insert(END, f"You have choosen a file {filename} which is not voice recording file")
def voicerec():
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16 
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 15
    filename = "output.wav"
    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = [] 
    j=0
    while 1:
        if(j==4):
            break
        for i in range(0, int(fs / chunk * seconds)):
            stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()
    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
def callback():
    link='https://speechtotex.netlify.app/'
    Output.delete("1.0","end")
    Output.insert(END,f"You have clicked on the Live Recording")
    webbrowser.open_new_tab(link)
    
if __name__ == "__main__" :
    r = sr.Recognizer()
    today = date.today()
    root = Tk()
    root.title("Text-Recording")
    filename =''

        
        
        
        