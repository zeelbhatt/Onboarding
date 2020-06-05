#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String
import cv2
from cv_bridge import CvBridge


class ImageSubscriber:
    def __init__(self):

        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("images",Image,self.callback)



    def callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)
        
        cv2.imshow("Image window", cv_image)
        cv2.waitKey(3)


ic = ImageSubscriber()
rospy.init_node('crop_subscriber')
try:
    rospy.spin()
except KeyboardInterrupt:
    print "Shutting down"
cv2.destroyAllWindows() 