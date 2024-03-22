import pupbeams
import RPi.GPIO as GPIO
from time import sleep

PIN_MOTOR_PWM = 12

def InitMotors():
    while pupbeams.IsBottomBeamBroken() or pupbeams.IsTopBeamBroken():
        pass

    LowerLift()

def LowerLift():
    print("Lowering lift")
    GPIO.setup(PIN_MOTOR_PWM, GPIO.OUT)
    p = GPIO.PWM(PIN_MOTOR_PWM, 50)
    p.start(2)
    sleep(1)
    GPIO.setup(PIN_MOTOR_PWM, GPIO.IN)

def RaiseLift():
    print("Raising lift")
    GPIO.setup(PIN_MOTOR_PWM, GPIO.OUT)
    p = GPIO.PWM(PIN_MOTOR_PWM, 50)
    p.start(12.5)
    sleep(1)
    GPIO.setup(PIN_MOTOR_PWM, GPIO.IN)

def TestMotors():
    while True:
        GPIO.setup(PIN_MOTOR_PWM, GPIO.OUT)
        p = GPIO.PWM(PIN_MOTOR_PWM, 50)
        p.start(12)
        sleep(0.5)
        GPIO.setup(PIN_MOTOR_PWM, GPIO.IN)
        # while True:
        #     servo.min()
        #     sleep(3)
        #     servo.max()
        #     sleep(3)