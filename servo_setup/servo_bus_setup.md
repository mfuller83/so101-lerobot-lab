# Waveshare Serial Bus Servo Adaptor Setup


Product page
https://www.waveshare.com/bus-servo-adapter-a.htm

Wiki page
https://docs.waveshare.com/Bus_Servo_Adapter_A

FTServo Python GitHub
https://github.com/ftservo/FTServo_Python

install requirements 
```bash
python -m pip install -r requirements.txt
```

```
pyserial==3.5
```

to find the usb device address on the mac 
```
ls /dev/cu.*
```
for my computer this have given the address as ```/dev/cu.usbmodem5B790156211```

set this as the device name
```py
DEVICENAME              = '/dev/cu.usbmodem5B790156211'  
```

basic setup 

```py
# Import servo libraries
from scservo_sdk import * 

# Setup communication settings
SCS_ID = 1  # which servo 
BAUDRATE = 1000000
DEVICENAME = '/dev/cu.usbmodem5B790156211'

# Create communivation objects
portHandler = PortHandler(DEVICENAME)
packetHandler = sms_sts(portHandler)

# Open and configure the serial connection
portHandler.openPort()
portHandler.setBaudRate(BAUDRATE)

```

positioning move

```py
# Set up servo setting
SCS_MOVING_SPEED = 2400
SCS_MOVING_ACC = 50

target_pos = 2000

packetHandler.WritePosEx(SCS_ID,target_pos,SCS_MOVING_SPEED,SCS_MOVING_ACC)

```


