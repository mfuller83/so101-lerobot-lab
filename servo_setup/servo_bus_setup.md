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


