# Script for find the set ID of a servo

from scservo_sdk import * 

# Setup communication settings
BAUDRATE = 1000000
DEVICENAME = '/dev/cu.usbmodem5B790156211'

# Create communivation objects
portHandler = PortHandler(DEVICENAME)
packetHandler = sms_sts(portHandler)

# Open and configure the serial connection
portHandler.openPort()
portHandler.setBaudRate(BAUDRATE)

for sms_id in range(1,256):
    model_number, result, error = packetHandler.ping(sms_id)
    if result == 0:
        print(f"Servo found at ID:{sms_id}")