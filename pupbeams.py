import RPi.GPIO as GPIO

PIN_BEAM_TOP = 16
PIN_BEAM_BOTTOM = 18

def InitBeams():
    GPIO.setup(PIN_BEAM_TOP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(PIN_BEAM_BOTTOM, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def IsTopBeamBroken():
    return GPIO.input(PIN_BEAM_TOP == GPIO.LOW)

def IsBottomBeamBroken():
    return GPIO.input(PIN_BEAM_BOTTOM == GPIO.LOW)

def TestBeams():
    
    tempTop = False
    tempBottom = False
    currentTop = False
    currentBottom = False

    while True:

        tempTop = IsTopBeamBroken()
        tempBottom = IsBottomBeamBroken()

        if tempTop != currentTop:
            currentTop = tempTop
            print(f'Top Beam: {currentTop}')

        if tempBottom != currentBottom:
            currentBottom = tempBottom
            print(f'Bottom Beam: {currentBottom}')