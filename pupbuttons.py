import RPi.GPIO as GPIO

PIN_BUTTON_UP = 3
PIN_BUTTON_DOWN = 5

def InitButtons():
    GPIO.setup(PIN_BUTTON_UP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PIN_BUTTON_DOWN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def IsUpButtonPressed():
    return GPIO.input(PIN_BUTTON_UP) == GPIO.HIGH

def IsDownButtonPressed():
    return GPIO.input(PIN_BUTTON_DOWN) == GPIO.HIGH