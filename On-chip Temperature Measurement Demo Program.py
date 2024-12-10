#  On-chip Temperature Measurement Demo Program
import machine
import time
import rp2

sensor_temp = machine.ADC(4) #Connect to the internal temperature sensor
conversion_factor = 3.3/(65535)
while True:
    temp_adc = sensor_temp.read_u16()*conversion_factor
    # The temperature sensor measures the Vbe voltage of a biased bipolar diode, connected to
    # the fifth ADC channel
    # Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree.
    temp_c   = 27-(temp_adc-0.706)/0.001721
    print(f"Temperature:{temp_c:.2f}{chr(176)}C")
    time.sleep(1)
