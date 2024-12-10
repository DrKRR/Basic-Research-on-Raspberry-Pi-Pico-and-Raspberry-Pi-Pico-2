# Basic-Research-on-Raspberry-Pi-Pico-Raspberry-Pi-Pico-W-and-Raspberry-Pi-Pico-2
<b>Experimental Measurement of Certain Raspberry Pi Pico Parameters</b> <br>
As a beginning of the research done on variants of Raspberry Pi Pico models, I am explaining certain parameter measurements. Codes are developed both in MicroPython and Arduino, wherever is necessary. I am sure that I am not describing the parameters in systematic way (Randomly).<br>
## Unveiling the On-chip Temperature Sensor of Raspberry Pi Pico ##
<b>Raspberry Pi Pico W:</b><br>
I have already explained the On-chip temperature sensor in the following YouTube Short:<br>
**Unveiling the On chip Temperature Sensor of Raspberry Pi Pico**  (https://youtube.com/shorts/_W1XJNeHqDk)<br>
The MicroPython code for the above is given in this repository<br>
**Raspberry Pi Pico 2**<br>
The Raspberry Pi Pico 2 was introduced on 8th August 2024, costing 5$. It's a 2X dual core (dual-ARM Cortex M33 and dual-RISC V Hazard3) microcontroller (RP2350) with advanced features.
It has an integrated on-chip temperature sensor in the form of a biased NPN-diode connected in the configuration shown below, and the chip has greatly improved power efficiency.</br>
![image](https://github.com/user-attachments/assets/c80c05c4-9675-4558-9ab6-7fae2fbe310e) ![image](https://github.com/user-attachments/assets/84edc946-6a16-4ce9-885d-f1ca040028a8)<br>
The ADC used in RP2350 as compared to RP2040, has improved precision. Basic specification of the Temperature Sensor ADC from Data sheet is given below (Courtesy: Raspberry Pi RP2350 Manual):
![image](https://github.com/user-attachments/assets/fc6e8e90-f7d5-49eb-a59d-271f9850077c)
MicroPython program is developed using the above specifications and sensor temperature is displayed on the Thonny shell. The measured temperature will be almost constant at the beginning . But, as time progress, the power dissipation of the internal dye will change (increase) the measured temperature. On the other hand, when the plastic encapsulation of RP2350 is cooled, the sensor temperature reduces. The microcontroller board placed on the bread board is shown below. Don<sup>'</sup>t get puzzled by the extra components on the board. It is for other experiments. The temperature output is seen on the Thonny shell. Code is available in this repository.

<p align="center"><img src="https://github.com/user-attachments/assets/28edce4a-7c7c-4d8c-b722-7704b703e5c5"width="250"height="250">
     <img src="https://github.com/user-attachments/assets/8bc0a0ce-6aa2-4fd5-b226-42ee5900e1fd"width="200"height="250"></p>

<p align="center"><img src="https://github.com/user-attachments/assets/e0ed06d0-11f4-42b0-b3c0-96f9257fa9ae"width="720"height="500"></p>

<p align="center"><img src="https://github.com/user-attachments/assets/2ba50dcd-a691-4cd0-b5b3-942030526014"width="720"height="500"></p>










