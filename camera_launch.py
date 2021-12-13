from tkinter import Variable
from flask import Flask, render_template, Response, request
from camera import VideoCamera
import time
import threading
import os
import pyaudio
import struct
import RPi.GPIO as GPIO
import time

servo = 8

GPIO.setmode(GPIO.BOARD)

GPIO.setup(servo, GPIO.OUT)

pwm=GPIO.PWM(servo, 50)

pwm.start(0)


pi_camera = VideoCamera(flip=False) # flip pi camera if upside down.

# App Globals (do not edit)
app = Flask(__name__)

def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(servo, True)
	pwm.ChangeDutyCycle(duty)
	time.sleep(1)
	GPIO.output(servo, False)
	pwm.ChangeDutyCycle(0)

print('start testing')

def run():
    
    SetAngle(180) 

    SetAngle(90) 

    pwm.stop()

    GPIO.cleanup()

def comptage():
    with open("comptage") as file:
        
        for last_line in file:

            pass

    print(last_line)

    compte = last_line

    print(compte)

    return compte

def statement():
    with open('resume') as file:

        for last_line in file:

            pass
    
    print(last_line)

    state = last_line

    return state

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 262144
RECORD_SECONDS = 5

audio1 = pyaudio.PyAudio()

def genHeader(sampleRate, bitsPerSample, channels):
    datasize = 2000*10**6
    o = bytes("RIFF",'ascii')                                               # (4byte) Marks file as RIFF
    o += (datasize + 36).to_bytes(4,'little')                               # (4byte) File size in bytes excluding this and RIFF marker
    o += bytes("WAVE",'ascii')                                              # (4byte) File type
    o += bytes("fmt ",'ascii')                                              # (4byte) Format Chunk Marker
    o += (16).to_bytes(4,'little')                                          # (4byte) Length of above format data
    o += (1).to_bytes(2,'little')                                           # (2byte) Format type (1 - PCM)
    o += (channels).to_bytes(2,'little')                                    # (2byte)
    o += (sampleRate).to_bytes(4,'little')                                  # (4byte)
    o += (sampleRate * channels * bitsPerSample // 8).to_bytes(4,'little')  # (4byte)
    o += (channels * bitsPerSample // 8).to_bytes(2,'little')               # (2byte)
    o += (bitsPerSample).to_bytes(2,'little')                               # (2byte)
    o += bytes("data",'ascii')                                              # (4byte) Data Chunk Marker
    o += (datasize).to_bytes(4,'little')                                    # (4byte) Data size in bytes
    return o

@app.route('/audio')
def audio():
    def sound():
        CHUNK = 262144
        sampleRate = 44100
        bitsPerSample = 16
        channels = 2
        wav_header = genHeader(sampleRate, bitsPerSample, channels)

        stream = audio1.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True,input_device_index=11, frames_per_buffer=CHUNK)
        
        print("recording...")

        while True:
            data = wav_header + stream.read(CHUNK)
            yield(data)
    
    return Response(sound())

@app.route('/')
def index():
    return render_template('index.html', Compte=comptage(), State=statement()) 

def gen(camera):
    #get camera frame
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/SomeFunction')
def SomeFunction():
    run()
    return "Nothing"

if __name__ == '__main__':

    comptage()

    app.run(host='0.0.0.0', threaded=True, port=5000)

    