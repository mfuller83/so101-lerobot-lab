
# Import servo libraries
from scservo_sdk import * 

from time import sleep

# Setup communication settings
SCS_ID = 1  # which servo 
BAUDRATE = 1000000
DEVICENAME = '/dev/cu.usbmodem5B790156211'

# Set up servo setting
SCS_MOVING_SPEED0 = 2400
SCS_MOVING_SPEED1 = -2400
SCS_MOVING_ACC = 50


# Create communivation objects
"""
Python program
     ↓
packetHandler      ← understands ST servo commands
     ↓
portHandler        ← handles the USB/serial connection
     ↓
USB Servo Adaptor
     ↓
ST3215
"""
portHandler = PortHandler(DEVICENAME)
packetHandler = sms_sts(portHandler)

# Open and configure the serial connection
portHandler.openPort()
portHandler.setBaudRate(BAUDRATE)

"""# Put the servo in the wheel mode
packetHandler.WheelMode(SCS_ID)


# Command the servo
packetHandler.WriteSpec(
    SCS_ID,
    SCS_MOVING_SPEED0,
    SCS_MOVING_ACC
)"""



packetHandler.WritePosEx(1, , 2400, 50)




#packetHandler.DisableTorque(6)


