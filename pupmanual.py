import RPi.GPIO as p

UPBUTTON = 23
DOWNBUTTON = 24

p.setup(UPBUTTON, p.IN, pull_up_down=p.PUD_UP)
p.setup(DOWNBUTTON, p.IN, pull_up_down=p.PUD_UP)


while True:

    if not p.input(UPBUTTON):
        pass
    elif not p.input(DOWNBUTTON):
        pass