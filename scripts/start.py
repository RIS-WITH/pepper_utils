#! /usr/bin/env python

import rospy
import qi
import sys
import os
import time

def main(session):
    # Setting the services
    motion_service = session.service("ALMotion")
    face_detection_service = session.service("ALFaceDetection")

    # Example showing how to activate "Move", "LArm" and "RArm" external anti collision
    motion_service.setExternalCollisionProtectionEnabled("All", False)
    print("Safety Lock Disabled")

    face_detection_service.pause(1)
    print("Auto Face detection Disabled")

    # Wake up call and get to localisation pose
    motion_service.wakeUp()
    print("Robot is awake")
    
    # Disable the artificial breath
    motion_service.setBreathEnabled("Body",False)
    print("Artificial Breath Disabled")

    # Set the robot to standard posture
    names = "Body"
    angles = [0.0193678308,-0.204438269,1.24219799,0.0365650989,-1.11843324,-0.526670039,-1.03511024,0.61011523,-2.51969592e-08,-0.0573792122,-0.0442125686,1.31760716,-0.0351500735,1.37310743,0.613771081,0.806987405,0.688877523,0,0,0]
    fractionMaxSpeed  = 0.1
    motion_service.setAngles(names, angles, fractionMaxSpeed)
    print("Set to standard posture")


    while(1):
        time.sleep(10)

        if not motion_service.robotIsWakeUp():
            print("Robot rested for 10 minutes")
            time.sleep(600)
            motion_service.wakeUp()
            print("Robot is awake after rest")

            # Set the robot to standard posture
            names  = "Body"
            angles  = [0.0193678308,-0.204438269,1.24219799,0.0365650989,-1.11843324,-0.526670039,-1.03511024,0.61011523,-2.51969592e-08,-0.0573792122,-0.0442125686,1.31760716,-0.0351500735,1.37310743,0.613771081,0.806987405,0.688877523,0,0,0]
            fractionMaxSpeed  = 0.1
            motion_service.setAngles(names, angles, fractionMaxSpeed)
            print("Set to standard posture")

if __name__ == "__main__":
    ip = os.environ['NAO_IP']
    port = 9559
    session = qi.Session()
    try:
        session.connect("tcp://" + ip + ":" + str(port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)
