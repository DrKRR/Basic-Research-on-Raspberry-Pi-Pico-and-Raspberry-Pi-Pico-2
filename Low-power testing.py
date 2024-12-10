from machine import Pin
from time import sleep

import lowpower

DORMANT_wfi_PIN = 15
ONBOARD_GREEN_LED = 25
OUT_FROM_DORMANT_YELLOW_LED = 22

# btn = Pin(DORMANT_PIN, Pin.IN, Pin.PULL_UP)
# btn.irq(lambda e: print("button event!"),
#      Pin.IRQ_FALLING)

green_led=Pin(ONBOARD_GREEN_LED, Pin.OUT)
yellow_led=Pin(OUT_FROM_DORMANT_YELLOW_LED, Pin.OUT)
yellow_led.value(1)

push_button=Pin(DORMANT_wfi_PIN, Pin.IN, Pin.PULL_UP)
push_button.irq(lambda e:none, Pin.IRQ_FALLING)

def blink_n_times(n):
    for _ in range(n):
        green_led.value(1)
        sleep(0.5)
        green_led.value(0)
        sleep(0.5)

while True:
    blink_n_times(1)
    for _ in range(10**6):
        pass
  
    blink_n_times(2)
    sleep(10)
    
    blink_n_times(3)
    lowpower.lightsleep()
    
    blink_n_times(4)
    lowpower.dormant_until_pin(DORMANT_wfi_PIN)
    
    blink_n_times(5)
    yellow_led.value(0)
    sleep(0.5)
    yellow_led,value(1)
    sleep(0.5)
