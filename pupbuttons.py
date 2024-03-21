import RPi.GPIO as GPIO

PIN_BUTTON_UP = 24
PIN_BUTTON_DOWN = 23

def InitButtons():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_BUTTON_UP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PIN_BUTTON_DOWN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def IsUpButtonPressed():
    return GPIO.input(PIN_BUTTON_UP) == GPIO.HIGH

def IsDownButtonPressed():
    return GPIO.input(PIN_BUTTON_DOWN) == GPIO.HIGH

def TestButtons():

    tempUp = False
    tempDown = False
    currentUp = False
    currentDown = False

    while True:

        tempUp = IsUpButtonPressed()
        tempDown = IsDownButtonPressed()
        
        if tempUp != currentUp:
            currentUp = tempUp
            print(f'Up Button: {currentUp}')

        if tempDown != currentDown:
            currentDown = tempDown
            print(f'Down Button: {currentDown}')