#!/usr/bin/env python 

import rospy
import serial
from geometry_msgs.msg import Point

class UltrasonicCostmap():
    def __init__(self):
        print('start node')
        rospy.init_node('ultrasonic_costmap')
        self.u_data_pub = rospy.Publisher('u_data', Point, queue_size=1)
        self.rate = 20

        self.ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)


    def handleScanner(self):
        self.ser.write('1')
        line = self.ser.readline()
        data = ""
        
        for i in range(len(line)-2):
            data += line[i]

        print(data)

        p = Point()
        p.x = int(data)
        self.u_data_pub.publish(p)


    def spin(self):
        r = rospy.Rate(self.rate)
        while not rospy.is_shutdown():
            self.handleScanner()


if __name__ == '__main__':
    print('start')
    uc = UltrasonicCostmap()
    uc.spin()

        
