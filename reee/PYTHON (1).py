from gpiozero import LED
from time import sleep
from gpiozero import Button

led1 = LED(4)
led2 = LED(26)
led3 = LED(21)
button = Button(26)

while True:
    led1.on()
    sleep(0.5)
    led1.off()
    led2.on()
    sleep(0.5)
    led2.off()
    led3.on()
    sleep(0.5)
    led3.off()
