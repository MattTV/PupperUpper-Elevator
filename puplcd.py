import time
from RPi import GPIO as gpio
from RPLCD.gpio import CharLCD

PIN_LCD_RS = 22
PIN_LCD_EN = 27
PIN_LCD_D4 = 26
PIN_LCD_D5 = 16
PIN_LCD_D6 = 5
PIN_LCD_D7 = 6

# PIN_LCD_RS = 15
# PIN_LCD_EN = 13
# PIN_LCD_D4 = 37
# PIN_LCD_D5 = 36
# PIN_LCD_D6 = 29
# PIN_LCD_D7 = 31

lcd: CharLCD

def InitLCD():
    global lcd
    lcd = CharLCD(
        pin_rs=PIN_LCD_RS,
        pin_e=PIN_LCD_EN,
        pins_data=[PIN_LCD_D4, PIN_LCD_D5, PIN_LCD_D6, PIN_LCD_D7],
        numbering_mode=gpio.BCM,
        cols=16,
        rows=2,
    )

def WriteLCD(text, x, y):
    lcd.cursor_pos = (y, x)
    lcd.write_string(text)

def TestLCD():
    for y in range(2):
        for x in range(16):
            lcd.cursor_pos = (y, x)
            lcd.write_string('{x}')
    
    while True:
        pass