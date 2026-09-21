*www.dragino.com*

### LSN50 LoRaWAN Sensor Node User Manual

## Document Version: 1.7.4 Image Version: v1.7.0

|Version|Description|Date|
|---|---|---|
|1.0|Release|2018-Dec-4|
|1.1|Add steps of install STM320x; Add ST-Link Upload firmware method|2018-Dec-27|
|1.2|Add trouble shooting for UART upload, Add change log for firmware v1.4|2019-Jan-23|
|1.2.1|More detail description for 8 channel mode and trouble shooting for using in US915/AU915|2019-Feb-21|
|1.2.2|Modify trouble shooting for upload via Flashloader|2019-Mar-13|
|1.2.3|Add ISP Mode / Flash mode different/ Add working flow diagram (Chapter 2.1 how it works) Add FAQ for how to configure the Keys|2019-Apr-1|
|1.5.0 1.5.1|Upgrade to v1.5 version firmware Add ultrasonic sensor support and description. Add downlink description Change decoder for v1.5 Add working flow chart Add Datacake support Improve Interrupt feature, change interrupt example to use door sensor|2019-Apr-19|
|1.5.2|Various minor text and format edits.|2019-Jun-10|
|1.6.0|Update to firmware v1.6 version, add 3ADC mode|2019-Aug-7|
|1.6.1|Trouble shooting for AT Command input Add support for 3 * DS18B20 (MOD4)|2019-Sep-18|
|1.6.2|Add door sensor detail/ power, Add battery connector info|2019-Dec-13|
|1.6.3|Add firmware version 1.6.2 change log, Add support for HX711 Weight Sensor|2019-Dec-31|
|1.6.4|Add New AT Command for 1.6.3. Add LSN50 v2.0 Hardware info|2020-Jan-13|
|1.6.5|Add battery measure suggestion, Add ADC range, Add change log for v1.6.4|2020-May-19|
|1.6.6|Add MOD=6 (counting) for firmware version v1.6.5, Update description for interrupt and 5v out, correction of digital input payload, change description for MOD=2 and MOD=5.|2020-Jul-15|
|1.7.0|Upgrade manual for v1.7.0. See change log.|2020-Nov-6|
|1.7.1|Add working mode payload, Add illumination sensor|2020-Dec-5|
|1.7.2|Correct ADC payload position error for MOD1 and MOD2, Add boot mode description, add VDD, +5v Out description.|2021-Jan-23|

*LSN50 LoRaWAN Sensor Node User Manual* /

|1.7.3|Add Power on photo for LSN50v2, add jumper info. Add New order option for Battery LSn50 v2.1 hardware change log|2021-Mar-17|
|---|---|---|
|1.7.4|Change to TTN v3 Add note for 3 x DS18B20 mode|2021-Sep-1|

1. Introduction
1.1 What is LSN50 LoRa Sensor Node
1.2 Specifications
1.3 Features
1.4 Applications
1.5 Pin Definitions and Switch
1.5.1 Jumper JP2
1.5.2 BOOT MODE / SW1
1.5.3 Reset Button
1.5.4 LED
1.6 Hardware Change log
1.7 Hole Option
2. Use LSN50 with LoRaWAN firmware
2.1 How it works
2.2 Quick guide to connect to LoRaWAN server (OTAA)
2.3 Working Mode & Uplink Payload
2.3.1 MOD=1 (Default Mode)
2.3.2 MOD=2 (Distance Mode)
2.3.3 MOD=3 (3 ADC + I2C)
2.3.4 MOD=4 (3 x DS18B20)
2.3.5 MOD=5(Weight Measurement by HX711)
2.3.6 MOD=6(Counting Mode, Since firmware v1.6.5)
2.3.7 Decode payload in The Things Network
2.4 Payload Explanation and Sensor Interface
2.4.1 Battery Info
2.4.2 Temperature (DS18B20)
2.4.3 Digital Input
2.4.4 Analogue Digital Converter (ADC)
2.4.5 Digital Interrupt
2.4.6 I2C Interface (SHT20)
2.4.7 Distance Reading
2.4.8 Ultrasonic Sensor
2.4.9 +5V Output
2.4.10 Weigh Sensor HX711
2.4.11 BH1750 Illumination Sensor
2.4.12 Working MOD
2.5 Configure LSN50 via AT or Downlink
2.5.1 Common Commands:
2.5.2 Sensor related commands:
2.6 Show Data in Datacake IoT Server
2.7 Firmware Change Log
2.8 Use VDD or +5V to Power External Sensor
2.9 Battery Analysis
2.9.1 Battery Type
2.9.2 Power consumption Analyze
2.9.3 Battery Note
#### LSN50 LoRaWAN Sensor Node User Manual

6 7 7 8 9 9 10 10 10 11 12 12 14 20 20 20 25 25 26 29 30 31 31 31 31 32 34 37 38 38 40 40 40 41 43 43 43 45 48 48 49 49

/

2.9.4 Replace the battery
3. Using the AT Commands
3.1 Access AT Commands
3.2 Common AT Command Sequence
3.2.1 Multi-channel ABP mode (Use with SX1301/LG308)
3.2.2 Single-channel ABP mode (Use with LG01/LG02)
4. Upload Firmware
4.1 Upload Firmware via Serial Port
4.2 Upload Firmware via ST-Link V2
5. Developer Guide
6. FAQ
6.1 Why there is 433/868/915 version?
6.2 What is the frequency range of LT LoRa part?
6.3 How to change the LoRa Frequency Bands/Region?
6.4 Can I use Private LoRa protocol?
6.5 How to set up LSN50 to work in 8 channel mode
6.6 LG01/LG02?
6.7 How to configure the EUI keys in LSN50?
7. Trouble Shooting
7.1 Connection problem when uploading firmware.
7.2 Why I can’t join TTN V3 in US915 / AU915 bands?
7.3 AT Command input doesn’t work
8. Order Info
9. Packing Info
10. Support
11. References
53 53 53 54 54 57 59 61 61 61 61 61 62

64 65 66 66 66 67 68 68 69 69

*LSN50 LoRaWAN Sensor Node User Manual* /

How to set up LSN50 to work with Single Channel Gateway such as

# 1. Introduction

### 1.1 What is LSN50 LoRa Sensor Node

LSN50 is a Long Range LoRaWAN Sensor Node. It is designed for **outdoor data logging** and powered by **Li/SOCl2 battery** for long term use and secure data transmission. It is designed to facilitate developers to quickly deploy industrial level LoRa and IoT solutions. It helps users to turn the idea into a practical application and make the Internet of Things a reality. It is easy to program, create and connect your things everywhere.

It is based on SX1276/SX1278 allows the user to send data and reach extremely long ranges at low data-rates. It provides ultra-long range spread spectrum communication and high interference immunity whilst minimizing current consumption. It targets professional wireless sensor network applications such as irrigation systems, smart metering, smart cities, smartphone detection, building automation, and so on.

**LSN50** uses STM32l0x chip from ST, STML0x is the **ultra-low-power** STM32L072xx microcontrollers incorporate the connectivity power of the universal serial bus (USB 2.0 crystal-less) with the high-performance ARM® Cortex®-M0+ 32-bit RISC core operating at a 32 MHz frequency, a memory protection unit (MPU), high-speed embedded memories (192 Kbytes of Flash program memory, 6 Kbytes of data EEPROM and 20 Kbytes of RAM) plus an extensive range of enhanced I/Os and peripherals.

LSN50 is an **open source product**, it is based on the STM32Cube HAL drivers and lots of libraries can be found in ST site for rapid development.

### 1.2 Specifications

#### Micro Controller:

- STM32L072CZT6 MCU
- MCU: STM32L072CZT6
- Flash: 192KB
- RAM: 20KB
- EEPROM: 6KB
- Clock Speed: 32Mhz
#### Common DC Characteristics:

- Supply Voltage: 2.1v ~ 3.6v
- Operating Temperature: -40 ~ 85°C
- I/O pins: Refer to STM32L072 datasheet
#### LoRa Spec:

- Frequency Range,
- Band 1 (HF): 862 ~ 1020 Mhz or
- Band 2 (LF): 410 ~ 528 Mhz
- 168 dB maximum link budget.
- +20 dBm - 100 mW constant RF output vs.
- +14 dBm high efficiency PA.
- Programmable bit rate up to 300 kbps.
- High sensitivity: down to -148 dBm.
- Bullet-proof front end: IIP3 = -12.5 dBm.
- Excellent blocking immunity.
- Low RX current of 10.3 mA, 200 nA register retention.
- Fully integrated synthesizer with a resolution of 61 Hz.
- FSK, GFSK, MSK, GMSK, LoRaTM and OOK modulation.
- Built-in bit synchronizer for clock recovery.
- Preamble detection.
- 127 dB Dynamic Range RSSI.
- Automatic RF Sense and CAD with ultra-fast AFC.
- Packet engine up to 256 bytes with CRC.
- LoRaWAN 1.0.2 Specification
#### Battery:

- Li/SOCI2 un-chargeable battery
- Capacity: 4000mAh
- Self Discharge: <1% / Year @ 25°C
- Max continuously current: 130mA
- Max boost current: 2A, 1 second
#### Power Consumption

- STOP Mode: 2.7uA @ 3.3v
- LoRa Transmit Mode: 125mA @ 20dBm 44mA @ 14dBm

### 1.3 Features

- LoRaWAN 1.0.3 Class A, Class C
- STM32L072CZT6 MCU
- SX1276/78 Wireless Chip
- Pre-load bootloader on USART1/USART2
- MDK-ARM Version 5.24a IDE
- I2C, LPUSART1, USB, SPI2
- 3x12bit ADC, 1x12bit DAC
- 20xDigital I/Os
- LoRa™ Modem
- Preamble detection
- Baud rate configurable
- CN470/EU433/KR920/US915/IN865
- EU868/AS923/AU915
- Open-source hardware / software
- Available Band:433/868/915/920 Mhz
- IP66 Waterproof Enclosure
- Ultra-Low Power consumption
- AT Commands to change parameters
- 4000mAh or 8500mAh Battery for long term use。
### 1.4 Applications

- Smart Buildings & Home Automation
- Logistics and Supply Chain Management
- Smart Metering
- Smart Agriculture
- Smart Cities
- Smart Factory

### 1.5 Pin Definitions and Switch

|No.|Signal|Direction|Function|Remark|
|---|---|---|---|---|
|1|VDD (3v)|OUTPUT|VCC|Directly connect to main power for board|
|2|PA0|In/Out|Directly from STM32 chip|Used as ADC in LSN50 image|
|3|PA1|In/Out|Directly from STM32 chip||
|4|PA2|In/Out|Directly from STM32 chip, 10k pull up to VCC|Used as UART_TXD in LSN50 image|
|5|PA3|In/Out|Directly from STM32 chip, 10k pull up to VCC|Used as UART_RXD in LSN50 image|

|6|PB6|In/Out|Directly from STM32 chip, 10k pull up to VCC||
|---|---|---|---|---|
|7|PB7|In/Out|Directly from STM32 chip, 10k pull up to VCC||
|8|PB3|In/Out|Directly from STM32 chip, 10k pull up to VCC||
|9|PB4|In/Out|Directly from STM32 chip||
|10|PA9|In/Out|Directly from STM32 chip, 10k pull up to VCC||
|11 12|PA10 GND|In/Out|Directly from STM32 chip, 10k pull up to VCC Ground||
|13 14|VCC(2.9V) Jumper|OUTPUT|VCC Power on/off jumper|Directly connect to main power for board|
|15|PA4|In/Out|Directly from STM32 chip||
|16|NRST|In|Reset MCU||
|17|PA12|In/Out|Directly from STM32 chip||
|18|PA11|In/Out|Directly from STM32 chip||
|19|PA14|In/Out|Directly from STM32 chip||
|20|PB13|In/Out|Directly from STM32 chip||
|21|PB12|In/Out|Directly from STM32 chip||
|22|PB15|In/Out|Directly from STM32 chip||
|23|PB14|In/Out|Directly from STM32 chip||
|24|PA13|In/Out|Directly from STM32 chip||
|25 26|PA8 GND|In/Out|Directly from STM32 chip Ground|Default use to turn on/off LED1 in LSN50 image|
|27|+5V|Out|5v output power|Controlled by PB5(Low to Enable, High to Disable) Continuous output : max 600mA Pulse output : max 1A|
|28|LED1||Controlled by PA8|Blink on transmit|
|29|BOOT MODE/ SW1||Configure device in working mode or ISP program mode|Flash: Normal Working mode and send AT Commands ISP: UART Program Mode|
|30|NRST|In|Reset MCU||

#### 1.5.1 Jumper JP2

Power on Device when put this jumper.

#### 1.5.2 BOOT MODE / SW1

1) ISP: upgrade mode, device won't have any signal in this mode. but ready for upgrade firmware. LED won't work. Firmware won’t run.
2) Flash: work mode, device starts to work and send out console output for further debug

#### 1.5.3 Reset Button

Press to reboot the device.

#### 1.5.4 LED

It will flash:

1) When boot the device in flash mode
2) Send an uplink packet
### 1.6 Hardware Change log

Note: Hardware version is marked in the PCB.

#### <u>LSN50 v2.1:</u>

1. Change R14 to 1M ohm
2. Change R3, R4 to 4.7Kohm. So no need to modify them for 3 DS18B20 connection.
3. Add ESD to each I/O
#### <u>LSN50 v2.0:</u>

Ø Change to a new enclosure. Improve with external antenna, IP68, ear hook.

**LSN50 v1.3**: Ø Add P-MOS to control 5V output

<u>LSN50 v1.2</u>: Ø Add LED. Turn on for every LoRa transmit Ø Add pin PA4, PB13, NRST Ø Add 5V Output, on/off control by PB5(Low to Enable, High to Disable)

### 1.7 Hole Option

The LSN50 provides different hole size options for different size sensor cable. The options provided are M12, M16 and M20. The definition is as below:

# 2. Use LSN50 with LoRaWAN firmware

### 2.1 How it works

The LSN50 is pre-loaded with a firmware and is configured as LoRaWAN OTAA Class A mode by default. It has OTAA keys to join LoRaWAN network. To connect a local LoRaWAN network, you just need to input the OTAA keys in the LoRaWAN IoT server and power on the LSN50. It will automatically join the network via OTAA.

The diagram below shows the working flow in default firmware (ver 1.7.0):

In case you can’t set the OTAA keys in the LoRaWAN OTAA server, and you have to use the keys from the server, you can <u>use AT Commands</u> to set the keys in the LSN50.

|||www.dragino.com||
|---|---|---|---|
|2.2 network structure; we use the|Quick guide to connect to LoRaWAN server (OTAA) Following is an example for how to join the TTN V3 LoRaWAN Network LG308|. Below is the as a LoRaWAN gateway in this example.||
|configure the TTN V3 server. Step 1|The LG308 is already set to connected to TTN V3 network : Create a device in TTN V3 with the OTAA keys from LSN50. Each LSN50 is shipped with a sticker with the default device EUI as below: LSN50 LoRaWAN Sensor Node User Manual|, so what we need to now is|14 / 69|

You can enter this key in the LoRaWAN Server portal. Below is TTN V3 screen shot:

#### Add APP EUI in the application

||www.dragino.com|
|---|---|
|You can also choose to create the device manually.||
|Add APP KEY and DEV EUI LSN50 LoRaWAN Sensor Node User Manual|17 / 69|

#### Step 2: Power on LSN50

Put a Jumper on JP2 to power on the device.

#### For LSn50v2:

**Step 3:** The LSN50 will auto join to the TTN V3 network. After join success, it will start to upload messages to TTN V3 and you can see the messages in the panel.

### 2.3 Working Mode & Uplink Payload

LSN50 has different working mode for the connections of different type of sensors. This section describes these modes. Use can use the AT Command AT+MOD to set LSN50 to different working modes.

For example: **AT+MOD=2 //** will set the LSN50 to work in <u>MOD=2 distance mode</u> which target to measure distance via Ultrasonic Sensor.

#### NOTE:

1. Some working modes has payload more than 12 bytes, The US915/AU915/AS923 frequency bands’ definition has maximum 11 bytes in **DR0**. Server sides will see NULL payload while LSn50 transmit in DR0 with 12 bytes payload.
2. All modes share the same Payload Explanation from <u>HERE</u>.
3. By default, the device will send an uplink message every 5 minutes.
#### 2.3.1 MOD=1 (Default Mode)

In this mode, uplink payload includes in total 11 bytes. Uplink packets use FPORT=2.

#### Size(bytes 2 2 2 1 2 2

**)** **Value** BAT Temperature ADC Digital in & Temperature Humidity (DS18B20) Digital (SHT20 or SHT31 or (SHT20)

|(DS18B20)|Digital|(SHT20 or SHT31 or|(SHT20)|
|---|---|---|---|
||Interrupt|Ultrasonic Sensor)||

#### 2.3.2 MOD=2 (Distance Mode)

This mode is target to measure the distance. The payload of this mode is totally 11 th th bytes. The 8 and 9 bytes is for the distance.

|Size(bytes)|2|2|2|1|2|2|
|---|---|---|---|---|---|---|
|Value|BA T|Temperature (DS18B20)|ADC|Digital in & Digital Interrupt|Distance measure by: 1) LIDAR-Lite V3HP Or 2) Ultrasonic Sensor|Reserved|

#### Connection of LIDAR-Lite V3HP:

#### Connection to Ultrasonic Sensor:

For the connection to TF-Mini or TF-Luna, MOD2 payload is as below:

|Size(bytes)|2|2|1|2|2|2|
|---|---|---|---|---|---|---|
|Value|BA T|Temperature (DS18B20)|Digital in & Digital Interrupt|ADC|Distance measure by: 1) TF-Mini plus LiDAR Or 2) TF-Luna LiDAR|Distance signal strength|

Connection to <u>TF-Mini plus</u> LiDAR(UART version): Need to remove R3 and R4 resistors to get low power. Since firmware v1.7.0

|||www.dragino.com|
|---|---|---|
|Connection to|TF-Luna LiDAR (UART version): Need to remove R3 and R4 resistors to get low power. Since firmware v1.7.0||
|consumption.|Please use firmware version > 1.6.5 when use MOD=2, in this firmware version, user can use LSn50 v1 to power the ultrasonic sensor directly and with low power LSN50 LoRaWAN Sensor Node User Manual|24 / 69|

#### 2.3.3 MOD=3 (3 ADC + I2C)

This mode has total 12 bytes. Include 3 x ADC + 1x I2C

|Size(bytes)|2|2|2|1|2|2|1|
|---|---|---|---|---|---|---|---|
|Value|ADC1 (Pin PA0)|ADC2 (PA1)|ADC3 (PA4)|Digital in & Digital Interrupt|Temperature (SHT20 or SHT31)|Humidity (SHT20 or SHT31)|BAT|

#### 2.3.4 MOD=4 (3 x DS18B20)

This mode is supported in firmware version since v1.6.1. Software set to AT+MOD=4 Hardware connection is as below, (Note: Ø In hardware version v1.x and v2.0, R3 & R4 should change from 10k to 4.7k ohm to support the other 2 x DS18B20 probes. Ø In hardware version v2.1 no need to change R3, R4, by default, they are 4.7k ohm already. See <u>here</u> for hardware changelog. )

This mode has total 11 bytes. As shown below:

|Size(bytes)|2|2|2|1|2|2|
|---|---|---|---|---|---|---|
|Value|BAT|Temperature1 (DS18B20) (PB3)|ADC|Digital in & Digital Interrupt|Temperature2 (DS18B20) (PA9)|Temperature3 (DS18B20) (PA10)|

#### 2.3.5 MOD=5(Weight Measurement by HX711)

This mode is supported in firmware version since v1.6.2. Please use v1.6.5 firmware version so user no need to use extra LDO for connection.

Each HX711 need to be calibrated before used. User need to do below two steps:

a) Zero calibration. Don’t put anything on load cell and run **AT+WEIGRE** to calibrate to Zero gram.
b) Adjust calibration factor (default value 400): Put a known weight thing on load cell and run **AT+WEIGAP** to adjust the Calibration Factor. For example:
#### AT+WEIGAP =403.0

Response: Weight is 401 g

Check the response of this command and adjust the value to match the real value for thing.

#### Size(bytes) 2 2

|2 2|2 1|
|---|---|
|BAT Temperature|ADC Digital in & Digital|
|(DS18B20)|Interrupt|

**Value** Weight Reserved

#### 2.3.6 MOD=6(Counting Mode, Since firmware v1.6.5)

In this mode, the device will work in counting mode. It counts the interrupt on the interrupt pins and sends the count on TDC time.

Connection is as below. The PIR sensor is a count sensor, it will generate interrupt when people come close or go away. User can replace the PIR sensor with other counting sensors.

Note: LoRaWAN wireless transmission will infect the PIR sensor. Which cause the counting value

increase +1 for every uplink. User can change PIR sensor or put sensor away of the LSN50 to avoid this happen.

#### Size(bytes) 2 2 2 1 4

**Value** BAT Temperature ADC Digital in Count <u>(DS18B20)</u>

||www.dragino.com|
|---|---|
|2.3.7 Decode payload in The Things Network While using TTN V3 network, you can add the payload format to decode the payload.||
|The payload decoder function for TTN V3 are here: LSN50 TTN V3 Payload Decoder: [http://www.dragino.com/downloads/downloads/LSN50-LoRaST/Payload_decoder/](http://www.dragino.com/downloads/downloads/LSN50-LoRaST/Payload_decoder/) LSN50 LoRaWAN Sensor Node User Manual|30 / 69|

|||www.dragino.com|
|---|---|---|
|2.4 2.4.1 2.4.2|Payload Explanation and Sensor Interface Battery Info Check the battery voltage for LSN50. Ex1: 0x0B45 = 2885mV Ex2: 0x0B49 = 2889mV Temperature (DS18B20) If there is a DS18B20 connected to PB3 pin. The temperature will be uploaded in the payload. More DS18B20 can check the 3 DS18B20 mode Connection||
|2.4.3 ● ●|Example : If payload is: 0105H: (0105 & FC00 == 0), temp = 0105H /10 = 26.1 degree If payload is: FF3FH : (FF3F & FC00 == 1), temp = (FF3FH - 65536)/10 = -19.3 degrees. Digital Input The digital input for pin PA12, When PA12 is high, the bit 1 of payload byte 6 is 1. When PA12 is low, the bit 1 of payload byte 6 is 0. LSN50 LoRaWAN Sensor Node User Manual|31 / 69|

#### 2.4.4 Analogue Digital Converter (ADC)

The ADC pins in LSN50 can measure range from 0~3.3v, it use reference voltage from STM32. If user need to measure a voltage >3.3v, please use resistors to divide this voltage to lower than

3.3v, otherwise, it may destroy the ADC pin. The ADC monitors the voltage on the PA0 line, in mV. Ex: 0x021F = 543mv, **Example1:** Reading an Oil Sensor (Read a resistance value):
* Bouy on top, the oil sensor act as a 10K resistor.
* Bouy on bottom, it act as a 0ohm resistor, To get the deep for the liquid, we can measure the output resistance for oil sensor and calculate where the bouy is so to calculate the height of oil.
10 ~ 70cm

In the LSN50, we can use PB4 and PA0 pin to calculate the resistance for the oil sensor.

Steps:

1. Solder a 10K resistor between PA0 and VCC.
2. Screw oil sensor’s two pins to PA0 and PB4.
#### The equipment circuit is as below:

**ADC Pin**

**Solder a 10K Resistor between** **PA0 and VCC**

**Connect oil sensor to PA0 and** **PB4PB4 will be set to low(0v) at every sampling**

|||||www.dragino.com|
|---|---|---|---|---|
|So 𝑉𝑃𝐴₀ The 𝑅 2.4.5|According to above diagram: (𝑉𝐶𝐶 − 𝑉𝑃𝐴₀ 𝑜𝑖𝑙𝑠𝑒𝑛𝑠𝑜𝑟 The position of Bouy is|𝑘 = 10 10𝐾 = 0.9 × 2.9−0.9 Since the Bouy is linear resistance from 10 ~ 70cm. 4.5𝐾 10𝐾 Digital Interrupt trigger, the LSN50 will send a packet to the server. Interrupt connection method:|𝑉 𝑃𝐴0 𝑅𝑜𝑖𝑙𝑠𝑒𝑛𝑠𝑜𝑟 𝐾 𝑅 = 𝑉𝑃𝐴₀ × 10 𝑜𝑖𝑙𝑠𝑒𝑛𝑠𝑜𝑟 (𝑉𝐶𝐶 − 𝑉𝑃𝐴₀ is the reading of ADC. So if ADC=0x05DC=0.9 v and VCC (BAT) is 2.9v = 4.5K ohm × (70𝑐𝑚 − 10𝑐𝑚) + 10𝑐𝑚 = 37𝑐𝑚, from the bottom of Bouy Digital Interrupt refers to pin PB14, and there are different trigger methods. When there is a|)|
||(Requires firmware > 1.5.1) window.|Example to use with door sensor The door sensor is shown at right. It is a two wire magnetic contact switch used for detecting the open/close status of doors or windows. When the two pieces are close to each other, the 2 wire output will be short or open (depending on the type), while if the two pieces are away from each other, the 2 wire output will be the opposite status. So we can use LSN50 interrupt interface to detect the status for the door or|||
|● ●|follows:|Below is the installation example: One pin to LSN50’s PB14 pin The other pin to LSN50’s VCC pin LSN50 LoRaWAN Sensor Node User Manual|Fix one piece of the magnetic sensor to the door and connect the two pins to LSN50 as Install the other piece to the door. Find a place where the two pieces will be close to each other when the door is closed. For this particular magnetic sensor, when the door is closed, the output will be short, and PB14 will be at the VCC voltage.|34 / 69|

Door sensors have two types: NC (Normal close) and NO (normal open). The connection for both type sensors are the same. But the decoding for payload are reverse, user need to modify this in the IoT Server decoder.

When door sensor is shorted, there will extra power consumption in the circuit, the extra current is 3v3/R14 = 3v2/1Mohm = 0.3uA which can be ignored.

The above photos shows the two parts of the magnetic switch fitted to a door.

The software by default uses the falling edge on the signal line as an interrupt. We need to modify it to accept both the rising edge (0v --> VCC, door close) and the falling edge (VCC --> 0v, door open) as the interrupt.

The command is: **AT+INTMOD=1 //(more info about INMOD please refer** <u>AT Command Manual</u>**. )**

Below shows some screen captures in TTN V3:

||www.dragino.com|
|---|---|
|In MOD=1, user can use byte 6 to see the status for door open or close. TTN V3 decoder is as below:||
|door= (bytes[6] & 0x80)? "CLOSE":"OPEN";||
|Notice for hardware version LSN50 v1 < v1.3 In this hardware version, there is no R14 resistance solder. When use the latest firmware, it should set AT+INTMOD=0 to close the interrupt. If user need to use Interrupt in this hardware version, user need to solder R14 with 10M resistor and C1 (0.1uF) on board.|(produced before 2018-Nov).|
|LSN50 LoRaWAN Sensor Node User Manual|36 / 69|

#### 2.4.6 I2C Interface (SHT20)

The PB6(SDA) and PB7(SCK) are I2C interface lines. You can use these to connect to an I2C device and get the sensor data.

We have made an example to show how to use the I2C interface to connect to the SHT20 Temperature and Humidity Sensor. This is supported in the stock firmware since v1.5 with **AT+MOD=1 (default value).**

#### Below is the connection to SHT20.

The device will be able to get the I2C sensor data now and upload to IoT Server.

Convert the read byte to decimal and divide it by ten.

#### Example:

Temperature: Read:0116(H) = 278(D) Value: 278 /10=27.8℃; Humidity: Read:0248(H)=584(D) Value: 584 / 10=58.4, So 58.4%

If you want to use other I2C device, please refer the SHT20 part source code as reference.

#### 2.4.7 Distance Reading

Refer <u>Ultrasonic Sensor section</u>.

#### 2.4.8 Ultrasonic Sensor

The LSN50 v1.5 firmware supports ultrasonic sensor (with AT+MOD=2) such as SEN0208 from DF-Robot. This Fundamental Principles of this sensor can be found at this link: <u>[https://wiki.dfrobot.com/Weather_-](https://wiki.dfrobot.com/Weather_-)</u> <u>_proof_Ultrasonic_Sensor_with_Separate_Probe_SKU___SEN0208</u>

The LSN50 detects the pulse width of the sensor and converts it to mm output. The accuracy will be within 1 centimeter. The usable range (the distance between the ultrasonic probe and the measured object) is between 24cm and 600cm.

#### The picture below shows the connection:

Connect to the LSN50 and run <u>AT+MOD=2</u> to switch to ultrasonic mode (ULT). The ultrasonic sensor uses the 8 th and 9 th byte for the measurement value.

#### Example:

Distance: Read:0C2D(Hex) = 3117(D) Value: 3117 mm=311.7 cm

You can see the serial output in ULT mode as below:

#### In TTN V3 server:

#### 2.4.9 +5V Output

Since v1.2 hardware version, a +5v output is added in the hardware. The +5V output will be valid for every sampling. LSN50 will enable +5V output before all sampling and disable the +5v after all sampling.

Since firmware <u>v1.6.3</u>, The 5V output time can be controlled by AT Command.

### AT+5VT=1000

Means set 5V valid time to have 1000ms. So the real 5V output will actually have 1000ms + sampling time for other sensors.

By default the AT+5VT=500. If the external sensor which require 5v and require more time to get stable state, user can use this command to increase the power ON duration for this sensor.

#### 2.4.10 Weigh Sensor HX711

Since v1.6.2 firmware, LSN50 support Weigh Sensor HX711.

#### 2.4.11 BH1750 Illumination Sensor

th Since v1.7.0 firmware, MOD=1 support this sensor. The sensor value is in the 8 and th 9 bytes.

#### 2.4.12 Working MOD

th The working MOD info is contained in the Digital in & Digital Interrupt byte (7 Byte).

rd th User can use the 3 ~ 7 bit of this byte to see the working mod:

th Case 7 Byte >> 2 & 0x1f: Ø 0: MOD1 Ø 1: MOD2

||www.dragino.com|
|---|---|
|Ø 2: MOD3 Ø 3: MOD4 Ø 4:MOD5 Ø 5:MOD6 LSN50 LoRaWAN Sensor Node User Manual|42 / 69|

### 2.5 Configure LSN50 via AT or Downlink

User can configure LSN50 via AT Commands or LoRaWAN Downlink Commands There are two kinds of Commands: ✓ **Common Commands**: They should be available for each sensor, such as: change uplink interval, reset device. For firmware v1.7.0, user can find what common commands it supports: [http://wiki.dragino.com/index.php?title=End_Device_AT_Commands_and_Downlink_Com](http://wiki.dragino.com/index.php?title=End_Device_AT_Commands_and_Downlink_Com) mands ✓ **Sensor Related Commands**: These commands are special designed for LSN50. User can see these commands below:

#### 2.5.1 Common Commands:

They should be available for each of Dragino Sensors, such as: change uplink interval, reset device. For firmware v1.7.0, user can find what common commands it supports: [http://wiki.dragino.com/index.php?title=End_Device_AT_Commands_and_Downlink_Command](http://wiki.dragino.com/index.php?title=End_Device_AT_Commands_and_Downlink_Command) s

#### 2.5.2 Sensor related commands:

#### <u>Set work mode</u>:

Ø AT Command: AT+MOD=2 // Set work MOD =2. (1:IIC mode,2:Distance mode,3:3ADC mode, 4:3DS18B20 mode,5:weight mode) AT+MOD=? // Get current work MOD

Ø Downlink Payload: 0x0A aa // Same as AT+MOD=aa

#### <u>Set the trigger interrupt mode</u>:

Ø AT Command: AT+INTMOD=2 // Set INTMOD =2. (0:Disable,1:falling or rising,2:falling,3:rising) AT+INTMOD=? // Get current INTMOD

Ø Downlink Payload: 0x06 000003 // Set AT+INTMOD=3

#### <u>Set the 5V power open time during sampling</u>:

Ø AT Command: AT+5VT=1000 // Set 5v open time to 1000ms AT+5VT=? // Check current 5v open duration

Ø Downlink Payload: 0x07 aa bb // Equal AT+5VT=0x(aa bb)

||||www.dragino.com|
|---|---|---|---|
|Ø AT Command: AT+WEIGRE Ø 0x08 01 Ø AT Command: AT+WEIGAP=? Ø 0x08 02 aa bb|Set the weight to 0g (Zero Calibration) Downlink Payload: AT+WEIGAP=403.0 Downlink Payload:|// Set the weight to 0g // Set the weight to 0g Get or Set the GAP Value (calibrate factor) of measurement // Set GAP Value =403.0 (response: Weight: xx g) // Get current GAP Value // Equal to AT+WEIGAP=0x(aa bb)/10 LSN50 LoRaWAN Sensor Node User Manual|44 / 69|

### 2.6 Show Data in Datacake IoT Server

Datacake provides a human friendly interface to show the sensor data, once we have data in TTN V3, we can use Datacake to connect to TTN V3 and see the data in Datacake. Below are the steps:

Step 1: Be sure that your device is programmed and properly connected to the network at this time. Step 2: To configure the Application to forward data to Datacake you will need to add integration. To add the Datacake integration, perform the following steps:

Step 3: Create an account or log in Datacake. Step 4: Search the LSN50 and add DevEUI.

### 2.7 Firmware Change Log

* <u>Firmware download link</u> <u>[http://www.dragino.com/downloads/index.php?dir=LSN50-LoRaST/Firmware/LSN50.hex/](http://www.dragino.com/downloads/index.php?dir=LSN50-LoRaST/Firmware/LSN50.hex/)</u>
*** Firmware Change Log:** <u>[http://www.dragino.com/downloads/index.php?dir=LSN50-LoRaST/Firmware/LSN50.hex/](http://www.dragino.com/downloads/index.php?dir=LSN50-LoRaST/Firmware/LSN50.hex/)</u>
### 2.8 Use VDD or +5V to Power External Sensor

User can use VDD or +5V to power external sensor. Note:

1) VDD is 2.5~3.3v from the battery + diode, the VDD is always on, so when use VDD to power external sensor, make sure the sensor has a low power consumption in sleep mode ( less 50 uA) to get a long battery life.
2) +5V output is only ON when sampling. And MCU will turn off it after sampling. So if sensor can support 5v, +5V out is the best choice. <u>See here for more info</u>.
Note: Always test the actually current pass by the JP2 jumper when connect to a new type of
 sensor.

||||www.dragino.com|
|---|---|---|---|
|2.9 2.9.1 ●|Battery Analysis Battery Type The battery is designed to last for more than 5 years for the LSN50. The battery related documents as below: Battery Dimension,|The LSN50 battery is a combination of a 4000mAh or 8500mAh Li/SOCI2 Battery and a Super Capacitor. The battery is non-rechargeable battery type with a low discharge rate (<2% per year). This type of battery is commonly used in IoT devices such as water meter.||
|●|Lithium-Thionyl Chloride Battery|datasheet, Tech Spec||
|●|Lithium-ion Battery-Capacitor datasheet|, Tech Spec JST-XH-2P connector||
|2.9.2|Power consumption Analyze multimeter is required to measure this level of current. A victor VC86E is recommended.|When connect to different sensors, it is good to test the power consumption with the sensor working. User can remove the ON/OFF Jumper of LSN50, and connect a multimeter between the two pins of this header and measure the current to know the whole system power consumption. Because the sleep mode will have as low as 10uA, at least 4.5 digit||
|1.|consumption includes: Deep Sleep (Stop mode) for STM32. ~ 5uA LSN50 LoRaWAN Sensor Node User Manual|In a minimum system with DS18B20 and Oil Sensor and default firmware, the power|49 / 69|

2. Sampling current while reading DS18B20 and Oil Sensor
- Oil Sensor sampling time: 200us, current: 0.3mA
- DS18B20 sampling time: 750ms, current: 0.64mA
- Above power should add 8mA CPU power in working mode.
3. LoRaWAN transmit and receive time consumption. The LoRa TX / RX time and power can be found in the <u>LoRa calculator tool</u>. In a typical LoRaWAN data transmit. The energy profile is as below:
In the LoRaWAN protocol, the device will transfer in different LoRa Radio, and have different energy profile in LoRa part. We can calculate the battery life in two cases:

1) Lower power LoRa radio. Device has a good signal to gateway
2) Higher power LoRa radio. Device has a poor signal to gateway **Low Power Case**:
- Radio Parameter: SF7, 125kHz, 20dbm
- Transmit interval: 15 minutes.
- Payload: 8 Bytes. **High Power Case**:
- Radio Parameter: SF10, 125kHz, 20dbm
- Transmit interval: 15 minutes.
- Payload: 8 Bytes. To simplify the calculation, we can:
- Combine oil sensor and DS18B20 sampling energy together to **751ms@8.64ma**
- Combine the two RX windows together. There is a <u>power consumption tool</u> for easy analysis. Below is the analysis result.

Note: Ignore the 18 year result, because the battery has a max 2% discharge per year.

#### 2.9.3 Battery Note

The Li-SICO battery is designed for small current / long period application. It is not good to use a high current, short period transmit method. The recommended minimum period for use of this battery is 5 minutes. If you use a shorter period time to transmit LoRa, then the battery life may be decreased.

#### 2.9.4 Replace the battery

You can change the battery in the LSN50.The type of battery is not limited as long as the output is between 3v to 3.6v. On the main board, there is a diode (D1) between the battery and the main circuit. If you need to use a battery with less than 3.3v, please remove the D1 and shortcut the two pads of it so there won’t be voltage drop between battery and main board.

The default battery pack of LSN50 includes a ER18505 plus super capacitor. If user can’t find this pack locally, they can find ER18505 or equivalence, which will also work in most case. The SPC can enlarge the battery life for high frequency use (update period below 5 minutes)

# 3. Using the AT Commands

### 3.1 Access AT Commands

LSN50 supports AT Command set in the stock firmware. You can use a USB to TTL adapter to connect to LSN50 for using AT command, as below.

#### LSN50 v1 UART connection photo

#### LSN50 v2 UART connection photo

In the PC, you need to set the serial baud rate to **9600** to access the serial console for LSN50. LSN50 will output system info once power on as below:

### 3.2 Common AT Command Sequence

#### 3.2.1 Multi-channel ABP mode (Use with SX1301/LG308)

If device has not joined network via OTAA: AT+FDR AT+NJM=0 ATZ

If device already joined network: AT+NJM=0 ATZ

#### 3.2.2 Single-channel ABP mode (Use with LG01/LG02)

#### See <u>Sect 6.7</u>

||||www.dragino.com|
|---|---|---|---|
|- -|4. Upload Firmware Notes : be kept after running AT+FDR. 4.1 for upgrade firmware is as below: Step1: Download Step2 : Download the Step3:|Since image v1.3, the firmware will show version info during boot. If your device doesn’t show version info, you may have a very old image version. Always run AT+FDR to reset parameters to factory default after an update image. If the update is from image >= v1.3 to another image version >=v1.3, then the keys will Otherwise (e.g. from v1.2 to v1.3), AT+FDR may erase the keys. Upload Firmware via Serial Port The LSN50’s AT Command port can be used for firmware upgrade. The hardware connection flash loader. LSN50 Image files. Open flashloader; choose the correct COM port to update LSN50 LoRaWAN Sensor Node User Manual|54 / 69|

Board detected

**Step4:** Switch SW1 back to flash state and push the RESET button. The LSN50 will then run the new firmware.

### 4.2 Upload Firmware via ST-Link V2

You can use ST-LINK to upgrade firmware into LSN50. The hardware connection for upgrade firmware is as below:

Connection:

- ST-LINK v2 GND <--> LSN50 GND
- ST-LINK v2 SWCLK <--> LSN50 PA14
- ST-LINK v2 SWDIO <--> LSN50 PA13
- ST-LINK v2 RST <-->LSN50 NRST. **Step1:** Install <u>ST-LINK driver</u> first and then install <u>ST-LINK Utility</u>
#### Step2: Download the <u>LSN50 Image files</u>.

**Step3:** Open ST-LINK utility, **file --> open file** to select the image to be upgraded.

**Step4:** Click the “**Program Verify**” button on ST-LINK.

**Step5:** The led on the ST-LINK adapter will now blinking, and the ST-Link utility will pop up a download window. Click the start button to download the image to LSN50.

||www.dragino.com|
|---|---|
|LSN50 LoRaWAN Sensor Node User Manual|58 / 69|

NOTE: If this step fails, ST-LINK can’t establish connection to LSN50, please try to swap SWDIO & SWCLK pin. Some ST-LINK v2 devices are incorrectly marked.

# 5. Developer Guide

<u>Software Source Code Download Link</u>. ([https://github.com/dragino/LoRa_STM32/tree/master/STM32CubeExpansion_LRWAN](https://github.com/dragino/LoRa_STM32/tree/master/STM32CubeExpansion_LRWAN))

<u>Hardware Source Code Download Link</u> ([https://github.com/dragino/Lora/tree/master/LSN50](https://github.com/dragino/Lora/tree/master/LSN50))

LSN50 is an open source project, developer can use compile their firmware for customized applications. User can get the source code from: Ø Software Source Code: <u>[https://github.com/dragino/LoRa_STM32/tree/master/STM32CubeExpansion_LRWAN](https://github.com/dragino/LoRa_STM32/tree/master/STM32CubeExpansion_LRWAN)</u> Ø Hardware Design files: <u>[https://github.com/dragino/Lora/tree/master/LSN50](https://github.com/dragino/Lora/tree/master/LSN50)</u> Ø Compile instruction: <u>[http://wiki.dragino.com/index.php?title=Firmware_Compile_Instruction_--_STM32](http://wiki.dragino.com/index.php?title=Firmware_Compile_Instruction_--_STM32)</u>

Use Keil to open project file: STM32CubeExpansion_LRWAN/Projects/Multi/Applications/LoRa/DRAGINO-LRWAN(AT)/MDK- ARM/STM32L072CZ-Nucleo/Lora.uvprojx

In Keil, you can see what frequency band the code support.

1. If you want to change frequency, modify the Preprocessor Symbols. For example, change EU868 to US915

2. Compile and build

# 6. FAQ

### 6.1 Why there is 433/868/915 version?

Different countries have different rules for the ISM band for LoRa. Although the LoRa chip can support a wide range of Frequencies, we provide different versions of the hardware for best tune of the LoRa hardware part.

### 6.2 What is the frequency range of LT LoRa part?

Different LT version supports different frequency range, below is the table for the working frequency and recommend bands for each model.

|Version|LoRa IC|Working Frequency|Best Tune Frequency|Recommend Bands|
|---|---|---|---|---|
|433|SX1278|Band2(LF): 410 ~525 Mhz|433Mhz|CN470/EU433|
|868|SX1276|Band1(HF):862~1020 Mhz|868Mhz|EU868|
|915|SX1276|Band1(HF):862 ~1020 Mhz|915Mhz|AS923/AU915/ KR920/US915|

### 6.3 How to change the LoRa Frequency Bands/Region?

You can follow the instructions for <u>how to upgrade image</u>. When downloading the images, choose the required image file for download.

### 6.4 Can I use Private LoRa protocol?

The stock firmware is based on LoRaWAN protocol. You can use a private LoRa protocol in LSN50. This section describes an example for base LoRa transfer. It is a reference/demo and we do not provide further software development support on this topic.

In this demo, we will show the communication between LoRa Shield and LSN50, both of them using the basic LoRa library. LSN50 will send a message to a LoRa Shield and the LoRa Shield will print it to the console.

<u>LoRa Shield + UNO</u>: Use the <u>LoRa Library</u> and upload the <u>LoRa_Receive</u> Sketch to Arduino.

Refs: [http://www.dragino.com/downloads/index.php?dir=LSN50-LoRaST/LoRa_Raw_Example/Arduino/&file=LoRa.zip](http://www.dragino.com/downloads/index.php?dir=LSN50-LoRaST/LoRa_Raw_Example/Arduino/&file=LoRa.zip) [http://www.dragino.com/downloads/downloads/LSN50-LoRaST/LoRa_Raw_Example/Arduino/LoRaReceiver.ino](http://www.dragino.com/downloads/downloads/LSN50-LoRaST/LoRa_Raw_Example/Arduino/LoRaReceiver.ino)

Open the serial monitor to Arduino. The device acts as a LoRa Receiver and listen on the frequency 868.3Mhz by default.

**LSN50**: Use the <<u>LoRa RAW code</u>>. The project file is in: MDK-ARM\STM32L072CZ-Nucleo\ Lora.uvprojx <u>Compile</u> it and <u>Upload</u> it to LSN50, the LSN50 will transfer on the frequency 868.3Mhz. In the Arduino Console, it will see the received packets as below.

### 6.5 How to set up LSN50 to work in 8 channel mode

By default, the frequency bands US915, AU915, CN470 work in 72 frequencies. Many gateways are 8 channel gateways, and in this case, the OTAA join time and uplink schedule is long and unpredictable while the end node is hopping in 72 frequencies.

You can configure the end node to work in 8 channel mode by using the AT+CHE command. The 500kHz channels are always included for OTAA.

For example, in **US915** band, the frequency table is as below. By default, the end node will use all channels (0~71) for OTAA Join process. After the OTAA Join, the end node will use these all channels (0~71) to send uplink packets.

|CHE||||||US915 Uplink Channels(125KHz,4/5,Unit:MHz,CHS=0)||||
|---|---|---|---|---|---|---|---|---|---|
|0||||||ENABLE Channel 0-63||||
|1|902.3|902.5|902.7|902.9|903.1|903.3|903.5|903.7|Channel 0-7|
|2|903.9|904.1|904.3|904.5|904.7|904.9|905.1|905.3|Channel 8-15|
|3|905.5|905.7|905.9|906.1|906.3|906.5|906.7|906.9|Channel 16-23|
|4|907.1|907.3|907.5|907.7|907.9|908.1|908.3|908.5|Channel 24-31|
|5|908.7|908.9|909.1|909.3|909.5|909.7|909.9|910.1|Channel 32-39|
|6|910.3|910.5|910.7|910.9|911.1|911.3|911.5|911.7|Channel 40-47|
|7|911.9|912.1|912.3|912.5|912.7|912.9|913.1|913.3|Channel 48-55|
|8|913.5|913.7|913.9|914.1|914.3|914.5|914.7|914.9|Channel 56-63|

Channels(500KHz,4/5,Unit:MHz,CHS=0) 903 904.6 906.2 907.8 909.4 911 912.6 914.2 Channel 64-71

When you use the TTN V3 network, the US915 frequency bands use are:

- 903.9 - SF7BW125 to SF10BW125
- 904.1 - SF7BW125 to SF10BW125
- 904.3 - SF7BW125 to SF10BW125
- 904.5 - SF7BW125 to SF10BW125
- 904.7 - SF7BW125 to SF10BW125
- 904.9 - SF7BW125 to SF10BW125
- 905.1 - SF7BW125 to SF10BW125
- 905.3 - SF7BW125 to SF10BW125
- 904.6 - SF8BW500 Because the end node is now hopping in 72 frequency, it makes it difficult for the devices to Join the TTN V3 network and uplink data. To solve this issue, you can access the device via the AT commands and run: **AT+CHE=2** **ATZ** to set the end node to work in 8 channel mode. The device will work in Channel 8-15 & 64- 71 for OTAA, and channel 8-15 for Uplink. The **AU915** band is similar. Below are the AU915 Uplink Channels.

|CHE||||||AU915 Uplink Channels(125KHz,4/5,Unit:MHz,CHS=0)||||
|---|---|---|---|---|---|---|---|---|---|
|0||||||ENABLE Channel 0-63||||
|1|915.2|915.4|915.6|915.8|916|916.2|916.4|916.6|Channel 0-7|
|2|916.8|917|917.2|917.4|917.6|917.8|918|918.2|Channel 8-15|
|3|918.4|918.6|918.8|919|919.2|919.4|919.6|919.8|Channel 16-23|
|4|920|920.2|920.4|920.6|920.8|921|921.2|921.4|Channel 24-31|
|5|921.6|921.8|922|922.2|922.4|922.6|922.8|923|Channel 32-39|
|6|923.2|923.4|923.6|923.8|924|924.2|924.4|924.6|Channel 40-47|
|7|924.8|925|925.2|925.4|925.6|925.8|926|926.2|Channel 48-55|
|8|926.4|926.6|926.8|927|927.2|927.4|927.6|927.8|Channel 56-63|

Channels(500KHz,4/5,Unit:MHz,CHS=0)

915.9 917.5 919.1 920.7 922.3 923.9 925.5 927.1 Channel 64-71

|||www.dragino.com|
|---|---|---|
|6.6 Step1|How to set up LSN50 to work with Single Channel Gateway such as LG01/LG02? In this case, users need to set LSN50 to work in ABP mode and transmit in only one frequency. Assume we have a LG02 working in the frequency 868400000 now, below is the steps. : Log in TTN V3, Create an ABP device in the application and input the network session key (NETSKEY), app session key (APPSKEY) from the device.||
|V3.|Note: You need to make sure the above three keys match in the device and in TTN V3. You can change them either in TTN V3 or in the Device to make them match. In TTN V3, NETSKEY and APPSKEY can be configured in the setting page, but the Device Addr is generated by TTN You can also change the Device ADDR in TTN V3 by using the LSN50 LoRaWAN Sensor Node User Manual|The Things Network CLI. 64 / 69|

||||www.dragino.com||
|---|---|---|---|---|
|Step2:||Below are the AT commands:|Run AT commands to make the LSN50 work in Single frequency and ABP mode.||
||AT+FDR|Reset Parameters to Factory Default, Keys Reserve AT+NJM=0 Set to ABP mode AT+ADR=0 Set the Adaptive Data Rate Off AT+DR=5 Set Data Rate (Set AT+DR=3 for 915 band) AT+TDC=300000 Set transmit interval to 5 minutes AT+CHS=868400000 Set transmit frequency to 868.4Mhz AT+DADDR=26 01 1A F1 Set Device Address to 26 01 1A F1|||
||ATZ As shown below:|Reset MCU|||
|6.7 Refer||How to configure the EUI keys in LSN50? The early version of LSN50 firmware doesn’t have pre-configured keys. upgrade_image to update the firmware to the latest version. Run AT commands to set the keys to desired keys; refer LSN50 LoRaWAN Sensor Node User Manual|It is recommended that you update the image to the latest version before configure the keys. AT Command manual.|65 / 69|

# 7. Trouble Shooting

### 7.1 Connection problem when uploading firmware.

<u>Issue</u>: While using USB to TTL to upload firmware via UART interface. It works for several times but most of times it fails.

<u>Checklist</u>:

1. Double check if follow up exactly the steps as manual.
2. Check if hardware works fine: a) check if AT command works, b) check if ISP / flash switch works: PA12 will have different output level while set the ISP/Flash Switch in different position. c) check if reset button works.
3. If you use Windows10 system. Please change the flash loader to run in Windows7 compatibility mode.
4. We have seen cases where the FT232 USB TTL adapter has a reliability issue with the PC USB chipset (Intel). In this case, even though points 1 and 2 above work, it still has a reliability issue for uploading. If this happens, change to a different PC or change the USB to TTL adapter to solve the issue.
### 7.2 Why I can’t join TTN V3 in US915 / AU915 bands?

It is due to channel mapping. Please see the <u>Eight Channel Mode</u> section above for details.

||||www.dragino.com|
|---|---|---|---|
|7.3 send|if you already include the ENTER|AT Command input doesn’t work In the case if user can see the console output but can’t type input to the device. Please check ENTER while sending out the command. Some serial tool doesn’t while press the send key, user need to add ENTER in their string. LSN50 LoRaWAN Sensor Node User Manual|67 / 69|

# 8. Order Info

#### Part Number: LSN50-XX-YY or LSN50-v2-XX-YY-ZZ

**XX**: The default frequency band

- **AS923**: LoRaWAN AS923 band
- **AU915**: LoRaWAN AU915 band
- **EU433**: LoRaWAN EU433 band
- **EU868**: LoRaWAN EU868 band
- **KR920**: LoRaWAN KR920 band
- **US915**: LoRaWAN US915 band
- **IN865**: LoRaWAN IN865 band
- **CN470**: LoRaWAN CN470 band **YY:** Hole Option
- **12**: With M12 waterproof cable hole
- **16**: With M16 waterproof cable hole
- **20**: With M20 waterproof cable hole (LSN50 v2 doesn’t have this version)
- **NH**: No Hole **ZZ:** Battery Option ( Only valid for v2 model)
- **4**: with 4000mAh battery
- **8**: with 8500mAg battery
# 9. Packing Info

#### For LSN50:

<u>Package Includes</u>: Ø LSN50 LoRa Sensor Node x 1

<u>Dimension and weight</u>: Ø Device Size: 8 x 6.5 x 5 cm Ø Device Weight: 137g Ø Package Size / pcs : 9 x 7 x 6cm Ø Weight / pcs : 160g

#### For LSN50 v2:

<u>Package Includes</u>: Ø LSN50 v2 LoRa Sensor Node x 1 Ø External antenna x 1 Ø Spring Antenna (evaluate purpose)

<u>Dimension and weight</u>: Ø Device Size: 9.7 x 6.5 x 4.7 cm Ø Device Weight: 150g Ø Package Size / pcs : 14.0 x 8x 5 cm Ø Weight / pcs : 180g

# 10. Support

- Support is provided Monday to Friday, from 09:00 to 18:00 GMT+8. Due to different time zones we cannot offer live support. However, your questions will be answered as soon as possible in the before-mentioned schedule.
- Provide as much information as possible regarding your enquiry (product models, accurately describe your problem and steps to replicate it etc) and send a mail to
<u>support@dragino.com</u>

# 11. References

² <u>Product Page</u> ([http://www.dragino.com/products/lora/item/128-lsn50.html](http://www.dragino.com/products/lora/item/128-lsn50.html))

² <u>Data Sheet</u> ([http://www.dragino.com/downloads/index.php?dir=datasheet/EN/&file=Datasheet_LoRaS](http://www.dragino.com/downloads/index.php?dir=datasheet/EN/&file=Datasheet_LoRaS) ensorNode.pdf)

² <u>Image Download</u> ([https://github.com/dragino/LoRa_STM32/tree/master/LSN50.hex](https://github.com/dragino/LoRa_STM32/tree/master/LSN50.hex))

² Mechanical Drawing: <u>[http://www.dragino.com/downloads/index.php?dir=LSN50-LoRaST/Mechanical_Drawing/](http://www.dragino.com/downloads/index.php?dir=LSN50-LoRaST/Mechanical_Drawing/)</u>
