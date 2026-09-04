
# Import servo libraries
from scservo_sdk import * 

old_id = 1
new_id = 2



# Setup communication settings
SCS_ID = 1  # which servo 
BAUDRATE = 1000000
DEVICENAME = '/dev/cu.usbmodem5B790156211'

# Set up servo setting
SCS_MOVING_SPEED0 = 2400
SCS_MOVING_SPEED1 = -2400
SCS_MOVING_ACC = 50


# Create communivation objects
portHandler = PortHandler(DEVICENAME)
packetHandler = sms_sts(portHandler)

# Open and configure the serial connection
portHandler.openPort()
portHandler.setBaudRate(BAUDRATE)

# Unlock servo EPROM
packetHandler.unLockEprom(old_id)

packetHandler.write1ByteTxRx(
    old_id,
    SMS_STS_ID, # 5 - command to change address
    new_id
)

packetHandler.LockEprom(new_id)