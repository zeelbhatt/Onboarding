#!/usr/bin/env python

from cropimg_msgs.srv import (CropImg, CropImgResponse)
import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge
import numpy as np


a = False
x = y = h = w = cropimg = 0

def handle_crop(req):

    print "In callback"
    global a, x, y, h, w, cropimg
    a = True
    x = req.x_pix
    y = req.y_pix
    h = req.y_width
    w = req.x_width
    cropimg = cv_image[y:y+h, x:x+w]
    crop_image_message = bridge.cv2_to_imgmsg(cropimg, encoding="passthrough")

    response = CropImgResponse()
    response.cropimg = crop_image_message
    pub.publish(crop_image_message)
    
    return response



cv_image = None
rospy.init_node('crop_images')
loop_rate = rospy.Rate(1)
pub = rospy.Publisher('images', Image)

bridge = CvBridge()
cv_image = cv2.imread('/home/zeel/Pictures/sample.jpg')

s = rospy.Service('crop_image', CropImg, handle_crop)


while not rospy.is_shutdown():
    if cv_image is not None:
        if a:
            pub.publish(bridge.cv2_to_imgmsg(cropimg))
            print "Server Called"
        else:
            print "In else"
            pub.publish(bridge.cv2_to_imgmsg(cv_image))            
    loop_rate.sleep()






ctrl = False

while not ctrl:
    connections = pub.get_num_connections()
    if connections > 0 and a == True:
        pub.publish(image_message)
        ctrl = True
        print "Message Published, Closing program..."
    else:
        rospy.spin()
