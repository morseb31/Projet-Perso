import RPi.GPIO as GPIO
import time

TRIG = 38
ECHO = 40

clockwise = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

IN1 = 37
IN2 = 35
IN3 = 33
IN4 = 31
speed = 0.0005

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    
    GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)
    
def MotorCW(time_s):
    counts = int(time_s /speed/16)
    for i in range(counts):
        for i in range(4):
            GPIO.output(IN1, clockwise[i][0])
            time.sleep(speed)
            GPIO.output(IN2, clockwise[i][1])
            time.sleep(speed) 
            GPIO.output(IN3, clockwise[i][2])
            time.sleep(speed) 
            GPIO.output(IN4, clockwise[i][3])
            time.sleep(speed)

def MotorCCW(time_s):
    counts = int(time_s /speed/16)
    for i in range(counts):
        for i in range(4):
            GPIO.output(IN4, clockwise[i][0])
            time.sleep(speed)
            GPIO.output(IN3, clockwise[i][1])
            time.sleep(speed) 
            GPIO.output(IN2, clockwise[i][2])
            time.sleep(speed) 
            GPIO.output(IN1, clockwise[i][3])
            time.sleep(speed)
            
def distance():
    GPIO.output(TRIG, 0)
    time.sleep(0.000002)

    GPIO.output(TRIG, 1)
    time.sleep(0.00001)

    GPIO.output(TRIG, 0)

    while GPIO.input(ECHO) == 0:
        a = 0
    time1 = time.time()
    while GPIO.input(ECHO) == 1:
        a = 1
    time2 = time.time()
    during = time2 - time1
    return round(during * 340 / 2 * 100, 2)


def loop():
    dis = distance()
    print(str(dis) + 'cm' + '\n')
    time.sleep(0.3)
    if 0 < int(dis) < 15:
        MotorCW(60)
        MotorCCW(60)
        time.sleep(0.005)
    else:
        time.sleep(0.005)

       
def launch_motor():
    while True:
        setup()
        loop()

if __name__ == "__main__": 
    launch_motor()