<u>www.dragino.com</u>

# Dragino LoRa® AT Command Sets (For LSN50/LoRaST)

|Version|Describe|Time|
|---|---|---|
|V1.3|Add AT+CHS & AT+CHE command.|2018-10-26|
|V1.4|Add AT+CFG, AT+RX1WTO & AT+RX2WTO|2019-01-09|
|V1.5|Add AT+TXP with more option, Add AT+MOD|2019-04-18|
|V1.5.1|Add AT+INTMOD, AT+TXP|2019-05-27|
|V1.6.3|Sync with manual v1.6.3. Add AT +WEIGAP/ AT+WEIGRE|2019-Dec-31|

*Dragino LoRa® AT Command Sets* 1 / 24

1 Introduction...........................................................................................................4

1.1 How to connect device and send AT command?.........................................4
2 General Command.................................................................................................6

2.1 AT: Attention.................................................................................................6
2.2 AT?: Short Help.............................................................................................6
2.3 ATZ: MCU Reset............................................................................................6
2.4 AT+FDR: Factory Data Reset.........................................................................6
2.5 AT+VER: Image Version and Frequency Band...............................................7
2.6 AT+CFG: Print all configurations...................................................................7
2.7 AT+TDC: Application Data Transmission Interval..........................................8
3 Keys, IDs and EUIs management............................................................................8

3.1 AT+APPEUI: Application EUI.........................................................................8
3.2 AT+APPKEY: Application Key.........................................................................8
3.3 AT+APPSKEY: Application Session Key..........................................................9
3.4 AT+DADDR: Device Address..........................................................................9
3.5 AT+DEUI: Device EUI...................................................................................10
3.6 AT+NWKID: Network ID(You can enter this command change only after
successful network connection)..........................................................................10

3.7 AT+NWKSKEY: Network Session Key...........................................................10
4 Joining and sending date on LoRa® network.......................................................11

4.1 AT+CFM: Confirm Mode.............................................................................11
4.2 AT+CFS: Confirm Status..............................................................................11
4.3 AT+JOIN: Join LoRa® Network....................................................................12
4.4 AT+NJM: LoRa® Network Join Mode..........................................................12
4.5 AT+NJS: LoRa® Network Join Status...........................................................12
4.6 AT+RECV: Print Last Received Data in Raw Format....................................13
4.7 AT+RECVB: Print Last Received Data in Binary Format...............................13
4.8 AT+SEND: Send Text Data...........................................................................13
4.9 AT+SENB: Send Hexadecimal Data.............................................................14
5 LoRa® network management...............................................................................14

5.1 AT+ADR: Adaptive Rate..............................................................................14
5.2 AT+CLASS: LoRa® Class(Currently only support class A, class C)................14
5.3 AT+DCS: Duty Cycle Setting........................................................................15
5.4 AT+DR: Data Rate (Can Only be Modified after ADR=0).............................15
5.5 AT+FCD: Frame Counter Downlink.............................................................16
5.6 AT+FCU: Frame Counter Uplink..................................................................16
5.7 AT+JN1DL: Join Accept Delay1....................................................................17
5.8 AT+JN2DL: Join Accept Delay2....................................................................17
5.9 AT+PNM: Public Network Mode.................................................................17
5.10 AT+RX1DL: Receive Delay1.........................................................................18
*Dragino LoRa® AT Command Sets* 2 / 24

5.11 AT+RX2DL: Receive Delay2.........................................................................18
5.12 AT+RX2DR: Rx2 Window Data Rate............................................................19
5.13 AT+RX2FQ: Rx2 Window Frequency...........................................................19
5.14 AT+TXP: Transmit Power.............................................................................20
5.15 AT+RSSI: RSSI of the Last Received Packet..................................................20
5.16 AT+SNR: SNR of the Last Received Packet..................................................20
5.17 AT+PORT: Application Port.........................................................................21
5.18 AT+ CHS: Single Channel Mode..................................................................21
5.19 AT+ CHE: Eight Channel Mode....................................................................21
5.20 AT+MOD: Set work mode...........................................................................23
5.21 AT+INTMOD: Set the trigger interrupt mode.............................................23
5.22 AT+WEIGAP: Get or Set the GAP Value (calibrate factor) of measurement 24
5.23 AT+WEIGRE: Set the weight to 0g (Zero Calibration).................................24
*Dragino LoRa® AT Command Sets* 3 / 24

# 1 Introduction

This article describes the AT Commands Set used in Dragino LoRa® products, it cover below products: Ø LSN50 Ø LoRa ST Module Ø <u>Serial_Port_Tool</u>

## 1.1 How to connect device and send AT command?

<u>Software Setting:</u> An USB-TTL can be used with standard windows software such as Serial Port Utility. The chosen software should be configured with the following parameters:

- Baud rate: 9600
- Data: 8 bit
- Parity: none
- Stop: 1 bit
- Flow type: none
Figure 1 show the standard configuration for Serial Port Utility to use USB-TTL.

All the AT commands have a standard format as “AT+XXX”, with XXX denoting the command. There are four available command behaviors:

- **AT+XXX?** provides a short help of the given command, for example **AT?**
- **AT+XXX** is used to run a command, such as **AT+JOIN**
- **AT+XXX=?** is used to get the value of a given command, for example **AT+TDC=?**
- **AT+XXX=<value>** is used to provide a value to a command, for example **AT+SENDB=12:12a0ff** The output of the commands is provided on the UART. The output format is as below: *Dragino LoRa® AT Command Sets* 4 / 24

<value><CR><LF> <CR><LF><Status>

**Note**: <CR> stands for “carriage return” and <LF> stands for “line feed”

The <value><CR><LF> output is returned whenever the “help AT+XXX?” or the “get AT+XXX=?” commands are run. When no value is returned, the <value><CR><LF> output is not returned at all. Every command (except for ATZ used for MCU reset) returns a status string, which is preceded and followed by <CR><LF> in a “<CR><LF><Status>” format. The possible status are:

- OK: command run correctly without error.
- AT_ERROR: generic error
- AT_PARAM_ERROR: a parameter of the command is wrong
- AT_BUSY_ERROR: the LoRa® network is busy, so the command could not completed
- AT_TEST_PARAM_OVERFLOW: the parameter is too long
- AT_NO_NETWORK_JOINED: the LoRa® network has not been joined yet
- AT_RX_ERROR: error detection during the reception of the command More details on each command description and examples are described in the next part of this section. Note that each command preceded by # is the one provided by the host to the module. Then the return of the module is printed.
*Dragino LoRa® AT Command Sets* 5 / 24

|||www.dragino.com|
|---|---|---|
|2 2.1|General Command AT: Attention AT: Attention||
|AT|Test Command:|Response: OK|
|2.2|AT ?: Short Help AT ?: Short Help Test Command:|Response:|
|AT?||AT+<CMD>?:help on <CMD> AT+<CMD>:run <CMD> AT+<CMD>=<value>:set the value AT+<CMD>=?:get the value <followed by the help of all commands> OK|
|2.3|AT Z: MCU Reset AT Z: MCU Reset||
|AT Z?|Test Command: Test Command:|Response: ATZ: Trig a reset of the MCU OK Response:|
|AT Z||LSN50 Device/LoRa ST Module Image Version: XX Frequency Band: XX DevEui= XX XX XX XX XX XX XX XX <followed by the Tx and Rx information>|
|2.4|AT+FDR: Factory Data Reset Test Command: Dragino LoRa® AT Command Sets|AT+FDR: Factory Data Reset Response: 6 / 24|
||AT+FDR|LSN50 Device/LoRa ST Module Image Version: XX Frequency Band: XX DevEui= XX XX XX XX XX XX XX XX Please set the parameters or reset Device to apply change|
||Test Command: AT+FDR?|Response: AT+FDR: Reset Parameters to Factory Default, Keys Reserve OK|
|2.5|Test Command:|AT+VER: Image Version and Frequency Band AT+VER: Image Version and Frequency Band Response:|
||AT+VER=? Test Command:|1.3 EU868 OK Response:|
||AT+VER?|AT+VER: Get current image version and Frequency Band OK|
|2.6|AT+CFG: Print all configurations Test Command:|AT+CFG: Print all configurations Response:|
||AT+CFG Dragino LoRa® AT Command Sets|AT+DEUI = XX XX XX XX XX XX XX XX AT+DADDR=XXXXXXXX ………. AT+RX2WTO=X AT+CHS=868100000 OK 7 / 24|
|2.7|Test Command:|AT+TDC: Application Data Transmission Interval AT +TDC: Application Data Transmission Interval< The default TDC is 30000 ms> Response:|
||AT+TDC?|AT+TDC: Get or set the application data transmission interval in ms OK|
||AT +TDC=?|Response: 30000 OK|
||AT+TDC=60000|Response: OK|
|3 3.1||Keys, IDs and EUIs management AT+APPEUI: Application EUI AT+APPEUI: Application EUI <8 hex separated by >|
||Test Command: AT+APPEUI? Test Command: AT+APPEUI=?|Response: AT+APPEUI: Get or Set the Application EUI OK Response: 00 b3 d5 7e f0 00 4d 34 OK|
|CD|Test Command: AT+APPEUI=01 30 48 23 54 76 53|Response: OK|
|3.2|Test Command:|AT+APPKEY: Application Key AT+APPKEY: Application Key <16 hex separated by > Response:|
||AT+APPKEY?|AT+APPKEY: Get or Set the Application Key OK|
||Test Command: AT+APPKEY=? Dragino LoRa® AT Command Sets|Response: 00 35 55 55 22 23 55 53 43 24 23 42 34 35 35 35 8 / 24|
||Test Command:|Response:|
|35 35|AT+APPKEY=00 35 55 55 22 23 55 53 43 24 23 42 34 35|OK|
|3.3||AT+APPSKEY: Application Session Key|
||AT+APPSKEY: Application Session Test Command:|Key <16 hex separated by > Response:|
||AT+APPSKEY?|AT+APPSKEY: Get or Set the Application Session Key OK|
||Test Command: AT+APPSKEY=?|Response: 00 7d dc 73 33 d3 eb 9e 14 38 d5 a4 3e 62 5b e2|
||Test Command:|OK Response:(While Error in format, return|
|5b e2|AT+APPSKEY=00 7d dc 73 33 d3 eb 9e 14 38 d5 a4 3e 62|AT_PARAM_ERROR) OK|
|3.4|Test Command:|AT+DADDR: Device Address AT+DADDR: Device Address <4 hex digit separate by > Response:|
||AT+DADDR? Test Command:|AT+DADDR: Get or Set the Device Address OK Response: (While Error in format, return|
||AT+DADDR=?|AT_PARAM_ERROR) A8 40 41 FF OK|
||Test Command: AT+DADDR=A8 40 41 FF Dragino LoRa® AT Command Sets|Response: OK 9 / 24|

## 3.5 AT+DEUI: Device EUI

<u>AT+DEUI: Device EUI<8 hex separated by:></u> Test Command: Response: **AT+DEUI? AT+DEUI: Get or Set the Device EUI**

||OK|
|---|---|
|Test Command:|Response:|
|AT+DEUI=?|00 44 34 22 33 45 55 55|
||OK|
|Test Command:|Response:(System will write new value to Device EUI,While|
|AT+DEUI=A8 40 41 FF FF 12 34 56|Error in format, return AT_PARAM_ERROR)|
||OK|
|AT+NWKID: Network ID<4 hex separated by:>||
|Test Command:|Response:|
|AT+NWKID?|AT+NWKID: Get or Set the Network ID|
||OK|
|Test Command:|Response:|
|AT+NWKID=?|a8 40 41 ff|
||OK|
|Test Command:|Response:|
|AT+NWKID=A8 40 41 FF||
||OK|
|AT+NWKSKEY: Network Session Key<16 hex separated by:>||
|Test Command:|Response:|
|AT+NWKSKEY?|AT+NWKSKEY: Get or Set the Network Session Key|
||OK|
|Test Command:|Response:|
|AT+NWKSKEY=?|00 4f 19 25 52 ce 97 09 d7 fa 84 71 db 51 02 92|

## 3.6 AT+NWKID: Network ID(You can enter this command change only after

## successful network connection)

## 3.7 AT+NWKSKEY: Network Session Key

*Dragino LoRa® AT Command Sets* 10 / 24

|||www.dragino.com OK|
|---|---|---|
||Test Command: AT+NWKSKEY=A8 40 41 FF FF 12 34 56 00 01 02 04 05 06 06 07|Response: OK|
|4 4.1|AT+CFM: Confirm Mode AT+CFM: Confirm Mode|Joining and sending date on LoRa® network|
||Test Command: AT+CFM? Test Command:|Response: AT+CFM: Get or Set the confirmation mode (0-1) OK Response:|
||AT+CFM=?|0 OK|
||Test Command: AT+CFM=1|Response: OK|
||Test Command: AT+CFM=2|While Error in format, return AT_PARAM_ERROR|
|4.2|AT+CFS: Confirm Status AT+ CFS: Confirm Status Test Command:|Response:|
||AT+CFS?|AT+CFS: Get confirmation status of the last AT+SEND (0-1) OK|
||Test Command: AT+CFS=? Dragino LoRa® AT Command Sets|Response: 0 OK 11 / 24|
|4.3|AT+ JOIN: Join LoRa® Network|AT+JOIN: Join LoRa® Network|
||Test Command: AT+JOIN Test Command:|Response: OK Response:|
||AT+ JOIN?|AT+JOIN: Join network OK While Error in format, return AT_BUSY_ERROR|
|4.4|AT+ NJM: LoRa® Network Join Mode|AT+NJM: LoRa® Network Join Mode|
||Test Command: AT+NJM=? Test Command:|Response: 1 OK Response:|
||AT+NJM?|AT+NJM: Get or Set the Network Join Mode. (0: ABP, 1: OTAA) OK|
||Test Command: AT+NJM=0|Response: OK|
||Test Command: AT+NJM=2|While Error in format, return AT_PARAM_ERROR|
|4.5|AT+ NJS: LoRa® Network Join Status|AT+NJS: LoRa® Network Join Status|
||Test Command: AT+NJS=? Test Command:|Response: 0 OK Response:|
||AT+NJS? Dragino LoRa® AT Command Sets|AT+NJS: Get the join status OK 12 / 24|
|4.6|Test Command:|AT+RECV: Print Last Received Data in Raw Format AT+ RECV: Print Last Received Data in Raw Format<port:data> Response:|
||AT+RECV=?|0: OK|
||Test Command: AT+RECV?|Response: AT+RECV: print last received data in raw format OK|
|4.7|Test Command:|AT+RECVB: Print Last Received Data in Binary Format AT+ RECVB: Print Last Received Data in Binary Format<port:data> Response:|
||AT+RECVB=? Test Command:|2: 0010 OK Response:|
||AT+RECVB?|AT+RECVB: print last received data in binary format (with hexadecimal values) OK|
|4.8|AT+SEND: Send Text Data AT+ SEND: Send Text Data<port:data>||
||Test Command: AT+SEND?|Response: AT+SEND: Send text data along with the application port OK|
||Test Command: AT+SEND=12:hello world Dragino LoRa® AT Command Sets|Response: OK While Error in format, return AT_BUSY_ERROR/AT_BUSY_ERROR/AT_NO_NETWORK_JOI NED 13 / 24|
|4.9|AT+SENDB: Send Hexadecimal Dat Test Command:|AT+SENB: Send Hexadecimal Data a<port:data> Response:|
||AT+SENDB?|AT+SENDB: Send hexadecimal data along with the application port OK|
|9|Test Command: AT+SENDB=12:abcdef012345678|Response: OK|
||Test Command: AT+SENDB=abcdef0123456789|While Error in format, return AT_PARAM_ERROR AT_BUSY_ERROR/AT_NO_NETWORK_JOINED|
|5 5.1|AT+ADR: Adaptive Rate AT+ ADR: Adaptive Rate Test Command:|LoRa® network management Response:|
||AT+ADR=? Test Command:|1 OK Response:|
||AT+ADR?|AT+ADR: Get or Set the Adaptive Data Rate setting. (0: off, 1: on) OK|
||Test Command: AT+ADR=0|Response: OK While Error in format, return AT_PARAM_ERROR|
|5.2|AT+ CLASS: LoRa® Class Test Command:|AT+CLASS: LoRa® Class(Currently only support class A, class C) Response:|
||AT+CLASS=? Dragino LoRa® AT Command Sets|A OK 14 / 24|
||Test Command:|Response:|
||AT+CLASS?|AT+CLASS: Get or Set the Device Class OK|
||Test Command: AT+CLASS=C|Response: OK While Error in format, return AT_PARAM_ERROR|
|5.3|AT+ DCS: Duty Cycle Setting Test Command:|AT+DCS: Duty Cycle Setting Response:|
||AT+DCS? Test Command:|AT+DCS: Get or Set the ETSI Duty Cycle setting - 0=disable, 1=enable-Only for testing OK Response:|
||AT+DCS=?|1 OK|
||Test Command: AT+DCS=1|Response: OK While Error in format, return AT_PARAM_ERROR|
|5.4|AT+DR: Data Rate|AT+DR: Data Rate (Can Only be Modified after ADR=0)|
||Test Command: AT+DR=? Test Command:|Response: 5 OK Response:|
||AT+DR?|Get or Set the Data Rate. (0-7 corresponding to DR_X) OK|
||Test Command: AT+DR=2 Dragino LoRa® AT Command Sets|Response: 15 / 24|
|5.5|AT+ FCD: Frame Counter Downlink Test Command:|AT+FCD: Frame Counter Downlink Response:|
||AT+FCD=? Test Command:|0 OK Response:|
||AT+FCD?|AT+FCD: Get or Set the Frame Counter Downlink OK|
||Test Command: AT+FCD=10|Response: (System will write new value to FCD) OK While Error in format, return AT_PARAM_ERROR|
|5.6|AT+ FCU: Frame Counter Uplink|AT+FCU: Frame Counter Uplink|
||Test Command: AT+FCU=? Test Command:|Response: 0 OK Response:|
||AT+FCU?|AT+FCU: Get or Set the Frame Counter Uplink OK|
||Test Command: AT+FCU=10|Response: OK|
||Test Command: AT+ FCU=10.1 Dragino LoRa® AT Command Sets|Response: While Error in format, return AT_PARAM_ERROR 16 / 24|

|||www.dragino.com|
|---|---|---|
|5.7|AT+ JN1DL: Join Accept Delay1 Test Command:|AT+JN1DL: Join Accept Delay1 Response:|
||AT+JN1DL=? Test Command:|5000 OK Response:|
||AT+JN1DL?|AT+JN1DL: Get or Set the Join Accept Delay between the end of the Tx and the Join Rx Window 1 in ms OK|
||Test Command: AT+JN1DL=10000|Response: OK While Error in format, return AT_PARAM_ERROR/AT_BUSY_ERROR|
|5.8|AT+ JN2DL: Join Accept Delay2 Test Command:|AT+JN2DL: Join Accept Delay2 Response:|
||AT+JN2DL=? Test Command:|6000 OK Response:|
||AT+JN2DL?|AT+JN2DL: Get or Set the Join Accept Delay between the end of the Tx and the Join Rx Window 2 in ms OK|
||Test Command: AT+JN2DL=20000|Response: OK While Error in format, return AT_PARAM_ERROR/AT_BUSY_ERROR|
|5.9|AT+ PNM: Public Network Mode|AT+PNM: Public Network Mode|
||Test Command: AT+PNM=? Dragino LoRa® AT Command Sets|Response: 1 17 / 24|

|||www.dragino.com OK|
|---|---|---|
||Test Command:|Response:|
||AT+PNM?|AT+PNM: Get or Set the public network mode. (0: off, 1: on) OK|
||Test Command: AT+PNM=1|Response:(System will write new value to PNM) OK While Error in format, return AT_PARAM_ERROR/AT_BUSY_ERROR|
|5.10|AT+ RX1DL: Receive Delay1|AT+RX1DL: Receive Delay1|
||Test Command: AT+RX1DL=? Test Command:|Response: 1000 OK Response:|
||AT+RX1DL?|AT+RX1DL: Get or Set the delay between the end of the Tx and the Rx Window 1 in ms OK|
||Test Command: AT+RX1DL=1500|Response: OK While Error in format, return AT_BUSY_ERROR/AT_PARAM_ERROR|
|5.11|AT+ RX2DL: Receive Delay2|AT+RX2DL: Receive Delay2|
||Test Command: AT+RX2DL=? Test Command:|Response: 2000 OK Response:|
||AT+RX2DL? Dragino LoRa® AT Command Sets|AT+RX2DL: Get or Set the delay between the end of the Tx and the Rx Window 2 in ms 18 / 24|
||Test Command: AT+RX2DL=2500|Response: OK While Error in format, return AT_BUSY_ERROR/AT_PARAM_ERROR|
|5.12|AT+ RX2DR: Rx2 Window Data Rate|AT+RX2DR: Rx2 Window Data Rate|
||Test Command: AT+RX2DR=? Test Command:|Response: OK Response:|
||AT+RX2DR?|AT+RX2DR: Get or Set the Rx2 window data rate (0-7 corresponding to DR_X) OK|
||Test Command: AT+RX2DR=6|Response: OK Response: While Error in format, return AT_PARAM_ERROR|
|5.13|AT+ RX2FQ: Rx2 Window Frequency Test Command:|AT+RX2FQ: Rx2 Window Frequency Response:|
||AT+RX2FQ=?|434665000 OK|
||Test Command: AT+RX2FQ?|Response: AT+RX2FQ: Get or Set the Rx2 window frequency OK|
||Test Command: AT+RX2FQ=434665000 Dragino LoRa® AT Command Sets|Response: OK While Error in format, return A T_BUSY_ERROR / AT_BUSY_ERROR 19 / 24|
|5.14|AT+TXP: Transmit Power AT+ TXP: Transmit Power Test Command:|Response:|
||AT+TXP=? Test Command:|0 OK Response:|
||AT+TXP?|AT+TXP: Get or Set the Transmit Power (0-5, MAX:0, MIN:5, according to LoRaWAN Spec, or 40=10dB, 41 = 11dB, …, 50 = 20dB which is out of LoRaWAN spec.) OK|
||Test Command: AT+ TXP=1|Response: OK While Error in format, return AT_PARAM_ERROR|
|5.15|AT+ RSSI: RSSI of the Last Received Packet Test Command:|AT+RSSI: RSSI of the Last Received Packet Response:|
||AT+RSSI=?|0 OK|
||Test Command: AT+RSSI?|Response: AT+RSSI: Get the RSSI of the last received packet OK|
|5.16|AT+ SNR: SNR of the Last Received Packet Test Command:|AT+SNR: SNR of the Last Received Packet Response:|
||AT+SNR=? Test Command:|0 OK Response:|
||AT+SNR? Dragino LoRa® AT Command Sets|AT+SNR: Get the SNR of the last received packet OK 20 / 24|

||||www.dragino.com|
|---|---|---|---|
|5.17|AT+PORT: Application Port|AT+PORT: Application Port||
||Test Command: AT+PORT=21 Test Command:|Response: OK Response:||
||AT+PORT?||AT+PORT: Get or set the application port|
|||OK||
||Test Command: AT+PORT=?|Response: 21 OK||
|5.18|AT+ CHS: Single Channel Mode Test Command:|AT+ CHS: Single Channel Mode Response:||
||AT+ CHS =? Test Command:|0 OK Response:||
||AT+ CHS?|AT+CHS: Mode OK|Get or Set Frequency (Unit: Hz) for Single Channel|
||Test Command: AT+ CHS =868100000|Response: OK||
|5.19|AT+ CHE: Eight Channel Mode Test Command: AT+ CHE =?|AT+ CHE: Eight Channel Mode Response: 1 OK|902.3 902.5 902.7 902.9 903.1 903.3 903.5 903.7|
||Test Command: AT+ CHE? Dragino LoRa® AT Command Sets|Response: AT+CHE:|Get or Set eight channels mode,Only for US915,AU915,CN470 21 / 24|

**OK** Test Command: Response: **AT+ CHE =1** **OK**

|CHE||||||CN470 Uplink Channels(125KHz,4/5,Unit:MHz,CHS=0)||||
|---|---|---|---|---|---|---|---|---|---|
|0||||||ENABLE Channel 80-95||||
|1|486.3|486.5|486.7|486.9|487.1|487.3|487.5|487.7|Channel 80-87|
|2|487.9|488.1|488.3|488.5|488.7|488.9|489.1|489.3|Channel 88-95|

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

|CHE||||||AU915 Uplink Channels(125KHz,4/5,Unit:MHz, CHS=0)||||
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

*Dragino LoRa® AT Command Sets* 22 / 24

|||www.dragino.com|
|---|---|---|
|5.20|AT+MOD: Set work mode AT+MOD: Get or Set the work mode Test Command:|Response:|
||AT+ MOD =? Test Command:|1 OK Response:|
||AT+ MOD?|Get or Set the work mode(1:IIC mode,2:Distance mode,3:3ADC mode,4:3DS18B20 mode,5:weight mode) OK|
||Test Command: AT+ MOD =2|Response: OK|
|5.21|Test Command:|AT+INTMOD: Set the trigger interrupt mode AT+MOD: Get or Set the trigger interrupt mode Response:|
||AT+ INTMOD =? Test Command:|1 OK Response:|
||AT+ INTMOD?|Get or Set the trigger interrupt mode (0:Disable,1:falling or rising,2:falling,3:rising) OK|
||Test Command: AT+ INTMOD =2 Dragino LoRa® AT Command Sets|Response: OK 23 / 24|
|5.22||AT +WEIGAP: Get or Set the GAP Value (calibrate factor) of measurement|
||AT+WEIGAP: Get or Set the GAP Test Command:|Value of weight Response:|
||AT+ WEIGAP =?|400.0 OK|
||Test Command: AT+ WEIGAP? Test Command:|Response: Get or Set the GAP Value of weight OK Response:|
|Or|AT+ WEIGAP =403.0|Weight: xx g|
||AT+ WEIGAP =400.5|OK|
|5.23|AT+WEIGRE: Set the weight to 0g|AT +WEIGRE: Set the weight to 0g (Zero Calibration)|
||Test Command: AT+ WEIGRE|Response: OK|
||Test Command: AT+ WEIGRE? Dragino LoRa® AT Command Sets|Response: Set the weight to 0g OK 24 / 24|
