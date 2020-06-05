#!/usr/bin/env python

import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np

cv_image = None
rospy.init_node('image_converter', anonymous=True)
loop_rate = rospy.Rate(1)
image_pub = rospy.Publisher("image_topic",Image)
bridge = CvBridge()
cv_image = cv2.imread('/home/zeel/Pictures/sample.jpg')

print "Message Converted"

while not rospy.is_shutdown():
    if cv_image is not None:
        image_pub.publish(bridge.cv2_to_imgmsg(cv_image))
    loop_rate.sleep()


# try:
#     rospy.spin()
# except KeyboardInterrupt:
#     print("Shutting down")
# cv2.destroyAllWindows()