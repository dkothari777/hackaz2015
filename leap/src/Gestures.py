_author_ = 'Darshan Kothari'

#import os, sys, inspect to set Leap Library
import os, sys, inspect
#get the pwd (linux command) of the current directory and set it as the path
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
#get the src_dir set the lib_dir to the Leap Library and set it as part of the path
lib_dir = os.path.abspath(os.path.join(src_dir, '../lib'))
#set the sys.path to include both the src_dir and lib_dir
sys.path.insert(0, lib_dir)
#import the Leap library
import Leap
inFlight = False
change = False

#Callibration final var for hovering position.
callibration = True
pitch = 0
yaw = 0
roll = 0
wristPos_x = 0
wristPos_y = 0
wristPos_z = 0

#SubListener Class goes here
class HelpListener(Leap.Listener):

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

    def on_disconnect(self, controller):
        print "Disconnected"

    def on_exit(self, controller):
        print "Exit"

    def on_frame(self, controller):
        global inFlight
        frame = controller.frame()
        hands = frame.hands
        if len(hands) > 1:
            print "Please use one hand only"
        elif len(hands) == 0:
            if inFlight == True:
                print "Landing"
                inFlight = False
            else:
                print "No hands are detected"
        else:
            self.findCommand(self.parseHandData(hands[0]))

    def findCommand(self, handdata):
            #find the commmand to send to UV
            global change
            if (handdata['pitch'] < 30 and handdata['pitch'] > 10) and (handdata['roll'] > -10 and handdata['roll'] < 10) and (handdata['yaw'] > -10 and handdata['yaw'] < 10) and change == False:
                self.toggleInFlight()
                change = True
            else:
                if not ((handdata['pitch'] < 30 and handdata['pitch'] > 10) and (handdata['roll'] > -10 and handdata['roll'] < 10) and (handdata['yaw'] > -10 and handdata['yaw'] < 10)):
                    change = False
                    if( (handdata['pitch'] < 30 and handdata['pitch'] > 10) and (handdata['roll'] > -10 and handdata['roll'] < 10) and handdata['yaw'] < -10):
                        print "Moving Left"
                    elif ( (handdata['pitch'] < 30 and handdata['pitch'] > 10) and (handdata['roll'] > -10 and handdata['roll'] < 10) and handdata['yaw'] > 10):
                        print "Moving Right"
                    elif (handdata['pitch'] < 10 and (handdata['roll'] > -10 and handdata['roll'] < 10) and (handdata['yaw'] > -10 and handdata['yaw'] < 10)):
                        print "Diving"
                    elif (handdata['pitch'] > 30 and (handdata['roll'] > -10 and handdata['roll'] < 10) and (handdata['yaw'] > -10 and handdata['yaw'] < 10)):
                        print "Rising"
                    else:
                        print "Do not Understand"
                else:
                    print "Hovering"

    def checkPitchWithCallabration(self, data, bounds):
        bool_upper = data < bounds + 10
        bool_lower = data > bounds - 10
        return [bool_upper, bool_lower]

    def checkRollWithCallabration(self, data, bounds):
        bool_upper = data < bounds + 10
        bool_lower = data > bounds - 10
        return [bool_upper, bool_lower]

    def checkYawWithCallabration(self, data, bounds):
        bool_upper = data < bounds + 10
        bool_lower = data > bounds - 10
        return [bool_upper, bool_lower]

    def checkWristPosition_XYZ(self, data, bounds):
        bool_upper = data < bounds + 10
        bool_lower = data > bounds - 10
        return [bool_upper, bool_lower]

    def checkHovering(self, hdata, adata):
        global pitch, roll, yaw, wristPos_x, wristPos_y, wristPos_z
        pitch_bool = self.checkPitchWithCallabration(hdata['pitch'], pitch)
        roll_bool = self.checkRollWithCallabration(hdata['roll'], roll)
        yaw_bool = self.checkYawWithCallabration(hdata['yaw'], yaw)
        wristPos_boolx = self.checkWristPosition_XYZ(adata['x'], wristPos_x)
        wristPos_booly = self.checkWristPosition_XYZ(adata['y'], wristPos_y)
        wristPos_boolz = self.checkWristPosition_XYZ(adata['z'], wristPos_z)
        hand_bool = ((pitch_bool[0] == pitch_bool[1]) and (roll_bool[0] == roll_bool[1]) and (yaw_bool[0] == yaw_bool[1]))
        wristPos_bool = ((wristPos_boolx[0] == wristPos_boolx[1]) and (wristPos_booly[0] == wristPos_booly[1]) and (wristPos_boolz[0] == wristPos_boolz[1]))
        return (hand_bool and wristPos_bool)

    def checkTurningLeft(self, hdata, adata):
        global pitch, roll, yaw, wristPos_x, wristPos_y, wristPos_z
        pitch_bool = self.checkPitchWithCallabration(hdata['pitch'], pitch)
        roll_bool = self.checkRollWithCallabration(hdata['roll'], roll)
        yaw_bool = self.checkYawWithCallabration(hdata['yaw'], yaw)
        wristPos_boolx = self.checkWristPosition_XYZ(adata['x'], wristPos_x)
        wristPos_booly = self.checkWristPosition_XYZ(adata['y'], wristPos_y)
        wristPos_boolz = self.checkWristPosition_XYZ(adata['z'], wristPos_z)
        hand_bool = ((pitch_bool[0] == pitch_bool[1]) and ((roll_bool[0] == True) and  (roll_bool[1] == False)) and (yaw_bool[0] == yaw_bool[1]))
        wristPos_bool = ((wristPos_boolx[0] == wristPos_boolx[1]) and (wristPos_booly[0] == wristPos_booly[1]) and (wristPos_boolz[0] == wristPos_boolz[1]))
        return (hand_bool and wristPos_bool)

    def checkTurningRight(self, hdata, adata):
        global pitch, roll, yaw, wristPos_x, wristPos_y, wristPos_z
        pitch_bool = self.checkPitchWithCallabration(hdata['pitch'], pitch)
        roll_bool = self.checkRollWithCallabration(hdata['roll'], roll)
        yaw_bool = self.checkYawWithCallabration(hdata['yaw'], yaw)
        wristPos_boolx = self.checkWristPosition_XYZ(adata['x'], wristPos_x)
        wristPos_booly = self.checkWristPosition_XYZ(adata['y'], wristPos_y)
        wristPos_boolz = self.checkWristPosition_XYZ(adata['z'], wristPos_z)
        hand_bool = ((pitch_bool[0] == pitch_bool[1]) and ((roll_bool[0] == False) and  (roll_bool[1] == True)) and (yaw_bool[0] == yaw_bool[1]))
        wristPos_bool = ((wristPos_boolx[0] == wristPos_boolx[1]) and (wristPos_booly[0] == wristPos_booly[1]) and (wristPos_boolz[0] == wristPos_boolz[1]))
        return (hand_bool and wristPos_bool)

    def checkRotatingLeft(self, hdata, adata):
        global pitch, roll, yaw, wristPos_x, wristPos_y, wristPos_z
        pitch_bool = self.checkPitchWithCallabration(hdata['pitch'], pitch)
        roll_bool = self.checkRollWithCallabration(hdata['roll'], roll)
        yaw_bool = self.checkYawWithCallabration(hdata['yaw'], yaw)
        wristPos_boolx = self.checkWristPosition_XYZ(adata['x'], wristPos_x)
        wristPos_booly = self.checkWristPosition_XYZ(adata['y'], wristPos_y)
        wristPos_boolz = self.checkWristPosition_XYZ(adata['z'], wristPos_z)
        hand_bool = ((pitch_bool[0] == pitch_bool[1]) and (roll_bool[0] == roll_bool[1]) and ((yaw_bool[0] == False) and  (yaw_bool[1] == True)))
        wristPos_bool = ((wristPos_boolx[0] == wristPos_boolx[1]) and (wristPos_booly[0] == wristPos_booly[1]) and (wristPos_boolz[0] == wristPos_boolz[1]))
        return (hand_bool and wristPos_bool)

    def checkRotatingRight(self, hdata, adata):
        global pitch, roll, yaw, wristPos_x, wristPos_y, wristPos_z
        pitch_bool = self.checkPitchWithCallabration(hdata['pitch'], pitch)
        roll_bool = self.checkRollWithCallabration(hdata['roll'], roll)
        yaw_bool = self.checkYawWithCallabration(hdata['yaw'], yaw)
        wristPos_boolx = self.checkWristPosition_XYZ(adata['x'], wristPos_x)
        wristPos_booly = self.checkWristPosition_XYZ(adata['y'], wristPos_y)
        wristPos_boolz = self.checkWristPosition_XYZ(adata['z'], wristPos_z)
        hand_bool = ((pitch_bool[0] == pitch_bool[1]) and (roll_bool[0] == roll_bool[1]) and ((yaw_bool[0] == True) and  (yaw_bool[1] == False)))
        wristPos_bool = ((wristPos_boolx[0] == wristPos_boolx[1]) and (wristPos_booly[0] == wristPos_booly[1]) and (wristPos_boolz[0] == wristPos_boolz[1]))
        return (hand_bool and wristPos_bool)

    def checkRising(self, hdata, adata):
        global pitch, roll, yaw, wristPos_x, wristPos_y, wristPos_z
        pitch_bool = self.checkPitchWithCallabration(hdata['pitch'], pitch)
        roll_bool = self.checkRollWithCallabration(hdata['roll'], roll)
        yaw_bool = self.checkYawWithCallabration(hdata['yaw'], yaw)
        wristPos_boolx = self.checkWristPosition_XYZ(adata['x'], wristPos_x)
        wristPos_booly = self.checkWristPosition_XYZ(adata['y'], wristPos_y)
        wristPos_boolz = self.checkWristPosition_XYZ(adata['z'], wristPos_z)
        hand_bool = (((pitch_bool[0] == True) and  (pitch_bool[1]== False)) and (roll_bool[0] == roll_bool[1]) and (yaw_bool[0] == yaw_bool[1]))
        wristPos_bool = ((wristPos_boolx[0] == wristPos_boolx[1]) and (wristPos_booly[0] == wristPos_booly[1]) and (wristPos_boolz[0] == wristPos_boolz[1]))
        return (hand_bool and wristPos_bool)

    def checkFalling(self, hdata, adata):
        global pitch, roll, yaw, wristPos_x, wristPos_y, wristPos_z
        pitch_bool = self.checkPitchWithCallabration(hdata['pitch'], pitch)
        roll_bool = self.checkRollWithCallabration(hdata['roll'], roll)
        yaw_bool = self.checkYawWithCallabration(hdata['yaw'], yaw)
        wristPos_boolx = self.checkWristPosition_XYZ(adata['x'], wristPos_x)
        wristPos_booly = self.checkWristPosition_XYZ(adata['y'], wristPos_y)
        wristPos_boolz = self.checkWristPosition_XYZ(adata['z'], wristPos_z)
        hand_bool = (((pitch_bool[0] == False) and  (pitch_bool[1]== True)) and (roll_bool[0] == roll_bool[1]) and (yaw_bool[0] == yaw_bool[1]))
        wristPos_bool = ((wristPos_boolx[0] == wristPos_boolx[1]) and (wristPos_booly[0] == wristPos_booly[1]) and (wristPos_boolz[0] == wristPos_boolz[1]))
        return (hand_bool and wristPos_bool)

    def parseHandData(self, hand):
        rtodg = Leap.RAD_TO_DEG
        normal = hand.palm_normal
        direction = hand.direction
        pitch = direction.pitch * rtodg
        roll = normal.roll * rtodg
        yaw = direction.yaw * rtodg
        hand_data = {'pitch': pitch, 'roll': roll, 'yaw': yaw}
        return hand_data

    def parseArmData(self, arm):
        x = arm.wrist_position[0]
        y = arm.wrist_position[1]
        z = arm.wrist_position[2]
        return {'x': x, 'y': y, 'z': z}

    def toggleInFlight(self):
        global inFlight
        if inFlight == False:
            print "Starting to Fly"
            inFlight = True

def main():
    #initialize Listener Helper here before retrieving controller object
    listener = HelpListener()
    # get the Controller object of Leap
    controller = Leap.Controller()

    #add the listener to the controller object
    controller.add_listener(listener)

    #temporary exiting process
    print "Press any Key to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)

if __name__ == "__main__":
    main()
