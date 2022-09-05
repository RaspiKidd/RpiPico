# SOS Morse Code Program

# By RaspiKidd 05.09.2022

# Using the built in LED of the pico to send the SOS morse code message using functions


from machine import Pin
from utime import sleep

led = Pin(25, Pin.OUT)

def blink(times, delay):
    for x in range(1, times+1):
        led.on()
        sleep(delay)
        led.off()
        sleep(delay)

while True:
    blink(3, 0.2)
    sleep(0.4)
    blink(3, 0.6)
    # This loop does 3 dots for "S"
   # for x in range(1, 4):
   #     led.on()
   #     sleep(0.2)
   #     led.off()
    #    sleep(0.2)
    #sleep(0.4)

    # this loop does 3 dashes for "O"
    # for i in range(1, 4):
    #    led.on()
    #    sleep(0.6)
    #    led.off()
    #    sleep(0.6)
    #sleep(0.4)
    # Write your code here :-)
