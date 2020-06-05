#!/usr/bin/env python

import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


def callback(data):
    bridge = CvBridge()

    print "In callback"
    
    try:
        cv_image = bridge.imgmsg_to_cv2(data, "passthrough")
    except CvBridgeError as e:
        print(e)

    cv2.imshow("Image window", cv_image)
    cv2.waitKey(3)

    
rospy.init_node('image_publisher_1591091460178623889', anonymous=True)

# rospy.init_node('image_converter2', anonymous=True)

print "Node initialised"

rospy.Subscriber("images", Image, callback)

print "Subscribed"

try:
    rospy.spin()
except KeyboardInterrupt:
    print("Shutting down")

cv2.destroyAllWindows()