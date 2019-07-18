from gpiozero import LED
from gpiozero import Buzzer
from time import sleep
from gpiozero import Button
import random
led = LED(17)
buzzer = Buzzer(22)
button1 = Button(21)
button2 = Button(26)
while True:
    if button1.is_pressed:
        buzzer.on()
    else:
        buzzer.off()
    
    if button2.is_pressed:
        led.on()
    else:
        led.off()





