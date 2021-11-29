import RPi.GPIO as GPIO
import time

# GPIO port number, modified according to actual
servo = 8
a = 4
b = 6


def setup():
    global pwm
    # Remove warning message
    GPIO.setwarnings(False)
# Set the pin mode to BOARD mode
    GPIO.setmode(GPIO.BOARD)
#servo for output mode
    GPIO.setup(servo, GPIO.OUT)
# Create a PWM instance
    pwm = GPIO.PWM(servo, 50)
# Enable PWM
    pwm.start(0)


# Set angle
def setDirection(direction):
    duty = a / 180 * direction + b
# Change the frequency to change the angle
    pwm.ChangeDutyCycle(duty)
    print("direction =", direction, "-> duty =", duty)
    time.sleep(1)


print('start testing')
# initialization
setup()
while True:
    for direction in range(0, 181, 20):
        setDirection(direction)
        time.sleep(0.001)
    for direction in range(180, 0, -20):
        setDirection(direction)
        time.sleep(0.001)
    print('Repeat the test')