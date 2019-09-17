#!/usr/bin/env python 

import rospy
import serial
from geometry_msgs.msg import PointStamped

class UltrasonicCostmap():
    def __init__(self):
        print('start node')
        rospy.init_node('ultrasonic_costmap')
        self.u_data_pub = rospy.Publisher('u_data', PointStamped, queue_size=1)
        self.rate = 20

        self.ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)


    def handleScanner(self):
        self.ser.write('1')
        line = self.ser.readline()
        data = ""
        
        for i in range(len(line)-2):
            data += line[i]

        print(data)

        p = PointStamped()
        p.point.y = int(data)/100.0
        p.header.frame_id = "hokuyo"
        self.u_data_pub.publish(p)


    def spin(self):
        r = rospy.Rate(self.rate)
        while not rospy.is_shutdown():
            self.handleScanner()


if __name__ == '__main__':
    print('start')
    uc = UltrasonicCostmap()
    uc.spin()

        
