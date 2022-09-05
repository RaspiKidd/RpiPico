# Blinking LED Program

# By RaspiKidd 05.09.2022

# Simple program blinking the internal pico LED on and off


from machine import Pin
from utime import sleep

led = Pin(25, Pin.OUT)

while True:
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.5)
