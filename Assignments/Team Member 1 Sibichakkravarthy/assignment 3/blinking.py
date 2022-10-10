from gpiozero import LED
from time import sleep

led=LED(23)

while true :
    led.on()
    sleep(1)
    led.off()
    sleep(1)
