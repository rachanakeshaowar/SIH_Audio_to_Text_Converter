import speech_recognition as sr
import boto3
import speech_recognition as sr
import os
import datetime
r = sr.Recognizer()


audio_file = sr.AudioFile("download.wav")
with audio_file as source:
     r.adjust_for_ambient_noise(source)
     audio = r.record(source)
result = r.recognize_google(audio)