# First Look Raspberry Pi Pico

## What is the Raspberry Pi Pico?

The Pico is a brand new microcontroller from the Raspberry Pi Foundation.  It is based on the RP2040 chip developed by the Raspberry Pi Foundation here within the UK.

## Specs

* Dual cores Arm cortex M0+ running at 133MHz
* 264kB RAM (Random Access Memory)
* 26 GPIO (Genral Purpose Input Output) pins
    * 2 x I2C (Inter- Integrated Circuit)
    * 2 x SPI (Serial Peripheral Interface)
    * 2 x UART (Universal Asynchronous Receiver/Transmitter)
    * 3 x Analogue
* 2Mb flash storage for your programs and data

## What can it do?

The Raspberry PI Pico can become the brains of your next project whether it be a robot, DIY home automation gadget or an electronic musical instrument like a theremin and much more.

## How to Program the Pico?

The Pico can be programmed using MicroPython, C and C++ from launch. We will look at MicroPython to program the Pico later within this guide.

## Soldering the Pins

To solder the pins onto the Pico you will need:

* Soldering iron
* Solder
* Header Pins
* The Pico board
* Breadboard

Breadboard may sound a little strange, but it helps keep your Pico board and pins steady while you solder them.

## Installing MicroPython

1. Plug the Pico into your computer while holding down the BOOTSEL button on the front of the board
2. Let go of the BOOTSEL button and you should see the Pico pop-up as a removable drive like you have plugged in a pen drive named RPI-RP2
3. Open up the Pico drive and click on INDEX.HTM. This will open up a web page telling you all about the Pico
4. Scroll down the page and click on the Getting Started with MicroPython tab
5. Click on Download UF2 file button and save it to your RPI-RP2 drive. The Pico will reboot and you are now running MicroPython on your Pico.

## Installing Thonny

Thonny is the recommended MicroPython editor for the Pico.

1. Go to your browser and type [thonny.org](https://thonny.org/)
2. Click on either Windows, Mac or Linux depending on what operating system you are running. As I am using Windows I will click on Windows
3. This will download the Thonny application to the downloads folder on your computer
4. Open your downloads folder and double click on thonny-3.xx to run the install process
5. Follow the instructions on the screen. Once Thonny has installed click on finish.

## Setting up Thonny

1. Click on Thonny to open the editor
2. Make sure your Pico is plugged into your computer
3. Click on Python 3.xx down in the bottom right corner. This is where we can change the version of Python that we are programming in. From the menu that appears click on MicroPython(Raspberry Pi Pico).

We are now ready to program our Pico.

## Coding the LED

The Pico has a built-in LED that we can program Let's see how to do this.

Type the following code:

```
import machine

led_onboard = machine.Pin(25, machine.Pin.OUT)
led_onboard.value(1)
```

## Wrapping Up

That is us completed the first steps to getting started with the Raspberry Pi Pico.

Follow me on Twitter and Instagram as @RaspiKidd to see more of my discoveries with the Pico over the coming weeks.