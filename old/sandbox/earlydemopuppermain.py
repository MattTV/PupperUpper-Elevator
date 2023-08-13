import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
servo = 11

def main():
    
    isup = False
    
    while True:
        if GPIO.input(10) == GPIO.HIGH:
            if (isup == True):
                isup = False
                GoDown()
        elif GPIO.input(12) == GPIO.HIGH:
            if (isup == False):
                isup = True
                GoUp()
                
def GoDown():
    GPIO.setup(servo, GPIO.OUT)
    p = GPIO.PWM(servo, 50)
    p.start(2)
    time.sleep(0.5)
    GPIO.setup(servo, GPIO.IN)
            
def GoUp():
    GPIO.setup(servo, GPIO.OUT)
    p = GPIO.PWM(servo, 50)
    p.start(12.5)
    time.sleep(0.5)
    GPIO.setup(servo, GPIO.IN)

if __name__ == "__main__":
    main()