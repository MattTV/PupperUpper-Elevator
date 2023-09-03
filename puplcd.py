from RPi import GPIO as gpio
from RPLCD.gpio import CharLCD

PIN_LCD_RS = 21
PIN_LCD_EN = 23
PIN_LCD_D4 = 37
PIN_LCD_D5 = 35
PIN_LCD_D6 = 33
PIN_LCD_D7 = 31

lcd = None

def InitLCD():
    lcd = CharLCD(
        pin_rs=PIN_LCD_RS,
        pin_e=PIN_LCD_EN,
        pins_data=[PIN_LCD_D4, PIN_LCD_D5, PIN_LCD_D6, PIN_LCD_D7],
        numbering_mode=gpio.BOARD,
    )

def WriteLCD(text, x, y):
    lcd.cursor_pos = (y, x)
    lcd._write_string(text)

def TestLCD():
    for y in range(2):
        for x in range(16):
            lcd.cursor_pos = (y, x)
            lcd.write_string('{x}')