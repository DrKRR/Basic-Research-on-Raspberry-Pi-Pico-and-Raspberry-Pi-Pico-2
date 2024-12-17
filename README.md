# Basic-Research-on-Raspberry-Pi-Pico-Raspberry-Pi-Pico-W-and-Raspberry-Pi-Pico-2
Among different types of microcontrollers available on the market, Raspberry Pi Pico series have decided advantages (Please refer to the hardware manual). I got attracted towards the on-chip thermal sensor and power down modes, specifically. Hence, I am focusing on these parameter measurements, experimentally.<br>
<b>Experimental Measurement of Certain Raspberry Pi Pico Parameters</b> <br>
As a beginning of the research done on variants of Raspberry Pi Pico models, I am explaining certain parameter measurements. Codes are developed both in MicroPython and Arduino, wherever is necessary. I am sure that I am not describing the parameters in systematic way (Randomly). A number of on-line web sites has motivated me to do this reearch.<br>
## Unveiling the On-chip Temperature Sensor of Raspberry Pi Pico ##
<b>Raspberry Pi Pico W:</b><br>
I have already explained the On-chip temperature sensor in the following YouTube Short:<br>
**Unveiling the On chip Temperature Sensor of Raspberry Pi Pico** [Please visit this YouTube Short](https://youtube.com/shorts/_W1XJNeHqDk)<br>
The MicroPython code for the above is given in this repository<br>
**Raspberry Pi Pico 2**<br>
The Raspberry Pi Pico 2 was introduced on 8th August 2024, costing 5$. It's a 2X dual core (dual-ARM Cortex M33 and dual-RISC V Hazard3) microcontroller (RP2350) with advanced features.
It has an integrated on-chip temperature sensor in the form of a biased NPN-diode connected in the configuration shown below, and the chip has greatly improved power efficiency.</br>
![image](https://github.com/user-attachments/assets/c80c05c4-9675-4558-9ab6-7fae2fbe310e) ![image](https://github.com/user-attachments/assets/84edc946-6a16-4ce9-885d-f1ca040028a8)<br>
The ADC used in RP2350 as compared to RP2040, has improved precision, and particularly removed spikes in the differential nonlinearity. Basic specification of the Temperature Sensor ADC from Data sheet is given below (Courtesy: Raspberry Pi RP2350 Manual):
![image](https://github.com/user-attachments/assets/fc6e8e90-f7d5-49eb-a59d-271f9850077c)
MicroPython program is developed using the above specifications and sensor temperature is displayed on the Thonny shell. The measured temperature will be almost constant at the beginning . But, as time progress, the power dissipation of the internal dye will change (increase) the measured temperature. On the other hand, when the plastic encapsulation of RP2350 is cooled, the sensor temperature reduces. The microcontroller board (Raspberry Pi Pico 2) placed on the bread board is shown below. A plastic bucket containing a small ice piece is placed on the chip:RP2350, that reduces the chip temperature from 27.51 degree celsius to 22.36 degrees. ***❗ Check the shell portion of Thonny editors below❗***. Don<sup>'</sup>t get puzzled by the extra components on the board. It is for other experiments. Code is available in this repository.

<p align="center"><img src="https://github.com/user-attachments/assets/b70d9323-9fe6-4b8b-8382-0d4b26cde543"width="200"height="360">
     <img src="https://github.com/user-attachments/assets/28edce4a-7c7c-4d8c-b722-7704b703e5c5"width="250"height="350">
        <img src="https://github.com/user-attachments/assets/58a17cb0-2721-47f7-8048-2c848cbfa70e"width="230"height="350"></p>
        
<p align="center"><img src="https://github.com/user-attachments/assets/e0ed06d0-11f4-42b0-b3c0-96f9257fa9ae"width="720"height="500"></p>

<p align="center"><img src="https://github.com/user-attachments/assets/2ba50dcd-a691-4cd0-b5b3-942030526014"width="720"height="500"></p>

## Study on Low Power Modes of RP2040 ##
In this exercise I have developed code in MicroPython to test and note the current drawn by the Raspberry Pi Pico board in the following modes:<br>
(a). Pass (Normal program with creation of delay) (b). sleep (c). lowpower.lightsleep() and (d). lowpower.dormant()<br>
Two files namely (i). lowpower.py (courtesy: https://github.com/tomjorquera/pico-micropython-lowpower-workaround/blob/master/lowpower.py) and (ii). Low-power testing.py (present work) are stored on the device  Both files are available in the repository.
The corresponding hardware diagram developed on a bread board is shown below, and the board is powered by an external USB power bank (https://github.com/DrKRR/Build-Your-own-Power-Bank-for-your-Travel-and-IoT-Projects) via 5V/3V selectable bread board power supply unit. Also shown below is the photograph of the experimental setup.

<p align="center"><img src="https://github.com/user-attachments/assets/cd4fb93f-164d-4055-977a-70f171ac2083"width="360"height="540"></p>
<p align="center"><img src="https://github.com/user-attachments/assets/aaf978c7-d79d-40c9-89de-4653d8f66f6d"width="360"height="540">
        <img src="https://github.com/user-attachments/assets/dc1a484c-636a-454e-83e5-0b6f56dc58cf"width="360"height="540"></p>
As the page has become larger in size, I am discussing the low power modes of Raspberry Pi Pico 2 (RP2350) in another repository.<br>
<p align="center"><img src="https://github.com/user-attachments/assets/ac1c769a-7d27-4df5-ab6f-8ea9eec081ba"></p>

> [!TIP]
> In order to use the same Raspberry Pi Pico board for different IDEs (say for example: MicroPython and Arduino), I erase the flash 
  memory of RP2040/RP2350 by using the file ***flash_nuke.uf2***.<br>
  
> [!CAUTION]
> Take care of Power Supply connections while carrying out the above exercise<br> 
> Advises about risks or negative outcomes of certain actions.





