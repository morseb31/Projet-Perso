import multiprocessing
import queue
import RPi.GPIO as GPIO
import time
import smtplib
from datetime import datetime
from multiprocessing import *
from queue import Empty, LifoQueue
from multiprocessing.managers import BaseManager
from scipy.io.wavfile import read
import pyaudio
import wave
from Motor import distance

content = 'Distress'

soundpin = 3

tmp = 0

compte = 0

typo = 0

file = "sound.wav"

def ready():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(soundpin, GPIO.IN)

def Print(x):
    global tmp
    if x != tmp:
        if x == 1:
            print('**********')
            print('*    Turn off the lights*')
            print('**********')
    
        if x == 0:
            print('**********')
            print('* Turn on the light   *')
            print('**********')
        tmp = x

def Led():
    time.sleep(0.5)
    GPIO.output(7, GPIO.HIGH)
    GPIO.output(11, GPIO.HIGH)   
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(19, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(7, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    time.sleep(0.5)  


def results():
    now = datetime.now()

    print("now =", now)

    dt_string = now.strftime("%H")
   
    texte = "\n" + dt_string 

    with open("sdsn.results","a") as f:
        f.write(texte)
        f.close
        
class MyManager(BaseManager):
    pass
MyManager.register('LifoQueue', LifoQueue)


def rec():

    chunk = 1024

    FORMAT = pyaudio.paInt16

    channels = 1

    sample_rate = 44100
    record_seconds = 5

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT, channels=channels, rate=sample_rate, input=True, output=True, frames_per_buffer=chunk)

    frames = []

    print("Recording...") 

    for i in range(int(44100 / chunk * record_seconds)):
        data = stream.read(chunk)

    frames.append(data)
    print("Finished recording.")

    stream.stop_stream()
    stream.close()

    p.terminate()

    wf = wave.open(file, "wb")

    wf.setnchannels(channels)

    wf.setsampwidth(p.get_sample_size(FORMAT))

    wf.setframerate(sample_rate)

    wf.writeframes(b"".join(frames))

    wf.close()

def calc_distances(file):

    rec()

    min_val = 5000
    
    fs, data = read(file)
    data_size = len(data)
    
    focus_size = int(0.15 * fs)
    
    focuses = []
    distances = []
    idx = 0
    
    while idx < len(data):
        if data[idx] > min_val:
            mean_idx = idx + focus_size // 2
            focuses.append(float(mean_idx) / data_size)
            if len(focuses) > 1:
                last_focus = focuses[-2]
                actual_focus = focuses[-1]
                distances.append(actual_focus - last_focus)
            idx += focus_size
        else:
            idx += 1
    return distances

def sound_type():
    calc_distances(file)
    print(calc_distances(file))

def launch_alert(compte, lifo):

    while True:

        ready()

        if GPIO.input(soundpin) == 0:

            compte += 1

            lifo.put(compte)

            Led()

            results()
            
            Print(GPIO.input(soundpin))

        else:
                
            Print(GPIO.input(soundpin))
                
            time.sleep(0.1)


if __name__ == "__main__":

    manager = MyManager()

    manager.start()
    
    compte = int(compte)

    lifo = manager.LifoQueue()

    launch_alert(compte, lifo)





    

    

