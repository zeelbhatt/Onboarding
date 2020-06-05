#!/usr/bin/env python

from cropimg_msgs.srv import (CropImg, CropImgResponse, CropImgRequest)
import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge
import numpy as np

rospy.init_node('crop_client')

pub_img = rospy.ServiceProxy('crop_image', CropImg )


req = CropImgRequest()
req.x_pix = 5
req.y_pix = 5
req.x_width = rospy.get_param("~x_width")
req.y_width = rospy.get_param("~y_width")
resp = pub_img(req)

image_message = resp.cropimg

# bridge = CvBridge()

# crop_cv_image = bridge.imgmsg_to_cv2(image_message)

# cv2.imshow('image', crop_cv_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()