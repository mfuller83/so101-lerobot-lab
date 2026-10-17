# Python library for the control of robot arm

# Import servo libraries
from servo_setup.scservo_sdk import * 

class Robot:

    def __init__(self):
        """Iinitiate robot object"""
        self.SCS_MOVING_SPEED = 2400
        self.SCS_MOVING_ACC = 50


    def connect(self,DEVICENAME = '/dev/cu.usbmodem5B790156211',BAUDRATE = 1000000):
        # Setup communication settings
        # TODO: add in try for connection      

        # Create communivation objects
        self.portHandler = PortHandler(DEVICENAME)
        self.packetHandler = sms_sts(self.portHandler)

        # Open and configure the serial connection
        self.portHandler.openPort()
        self.portHandler.setBaudRate(BAUDRATE)


    def set_joint_limits(self, limits_max, limits_min):
        pass

    def set_home_position(self, home_position):
        pass

    def joint_move(self, joints):
        for id in range(1,7):
            self.packetHandler.SyncWritePosEx(id, joints[id-1],self.SCS_MOVING_SPEED, self.SCS_MOVING_ACC)
        
        

    def jog_joint(self, joint, dist):
        """Jog joint by set value"""
        # get joint positions 
        # add value to joint list
        joint[i] += dist
        # joint move

    def linear_move(self):
        pass

    def get_position(self):
        """Return position for each joint"""
        joints = []
        for sms_id in range(1,7):
            model_number, result, error = self.packetHandler.ping(sms_id)
            if result == 0:
                position, result, error = self.packetHandler.ReadPos(sms_id)
                joints.append(position)

        return joints
    
    