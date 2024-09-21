from machine import Pin #只使用Pin Class不需import整個machine
import time

led = Pin("LED", mode=Pin.OUT)
status = False
while True:
    if status == False:
        led.on()
        status = True
    else:
        led.off()
        status = False
    
    time.sleep(1)