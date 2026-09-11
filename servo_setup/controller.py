import serial

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


ser = serial.Serial("/dev/cu.usbmodem21101", 115200)

# Set up servo setting
SCS_MOVING_SPEED = 2400
SCS_MOVING_ACC = 50


while True:
    line = ser.readline().decode().strip()
    
    
    x, y, button = line.split(",")

    x = float(x)
    y = float(y)
    button = int(button)

    print(x, y, button)
    target_pos_x = int(x * 2000) + 2000
    target_pos_y = int(y * 2000) + 2000
    packetHandler.WritePosEx(1,target_pos_x,SCS_MOVING_SPEED,SCS_MOVING_ACC)
    packetHandler.WritePosEx(2,target_pos_y,SCS_MOVING_SPEED,SCS_MOVING_ACC)