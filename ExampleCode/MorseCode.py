# SOS Morse Code Program

# By RaspiKidd 05.09.2022

# Using the built in LED of the pico to sned the SOS morse code message


from machine import Pin
from utime import sleep

led = Pin(25, Pin.OUT)

while True:
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

