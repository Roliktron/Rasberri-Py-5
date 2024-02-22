from gpiozero import PWMLED
from time import sleep

led = PWMLED(5)

try:
    while True: 
        led.value = 0    # off 
        sleep(.1) 
        led.value = 0.1  # 10% brightness 
        sleep(.1) 
        led.value = 0.2  # 20% brightness 
        sleep(.1) 
        led.value = 0.3  # 30% brightness 
        sleep(.1)
        led.value = 0.4  # 40% brightness 
        sleep(.1)
        led.value = 0.5  # 50% brightness 
        sleep(.1)
        led.value = 0.6  # 60% brightness 
        sleep(.1)
        led.value = 0.7  # 70% brightness 
        sleep(.1)
        led.value = 0.8  # 80% brightness 
        sleep(.1)
        led.value = 0.9  # 90% brightness 
        sleep(.1)
        
        led.value = 1    # full brightness 
        sleep(.1) 
    
except KeyboardInterrupt:
    print("Program leallitva")
    print("Led ki")
    led.off()

finally:
    # GPIO eroforrasok felszabaditasa
    led.close()
