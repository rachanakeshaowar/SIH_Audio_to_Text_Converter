import speech_recognition as sr
import boto3
import speech_recognition as sr
import os
import datetime
r = sr.Recognizer()


audio_file = sr.AudioFile("harsh.wav")
with audio_file as source:
     r.adjust_for_ambient_noise(source)
     audio = r.record(source)
result = r.recognize_google(audio)
with open("harsh.txt",mode ="w") as file:
     file.write("Recognized text:")
     file.write("\n")
     file.write(result)
     print("Hurray! conversion is completed")
     r = sr.Recognizer()

audio_file = sr.AudioFile("download.wav")
with audio_file as source:
  r.adjust_for_ambient_noise(source)
  audio = r.record(source)
result = r.recognize_google(audio)
with open("test.txt",mode ="w") as file:
    file.write("Recognized text:")
    file.write("\n")
    file.write(result)
    print("Hurray! conversion is completed")
    
    now = datetime.datetime.now()
fileun=str(now)
file_loc=os.path.abspath('test.txt') 
print(file_loc)
client = boto3.client(
    's3',
    aws_access_key_id='',  
    aws_secret_access_key='',
    
)

 