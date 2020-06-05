#! /usr/bin/env python

import rospy
import actionlib
from crop_action_server.msg import CropTheImageAction, CropTheImageGoal
import cv2
from cv_bridge import CvBridge
import matplotlib.pyplot as plt
import matplotlib.image as mpimg



def feedback_cb(img):
    
    print "Feedback received"
    fb_img = img.feedback_img
    bridge = CvBridge()
    
    crop_cv_image = bridge.imgmsg_to_cv2(fb_img)
    
    cv2.imshow('image', crop_cv_image)
    cv2.waitKey(300)
    # cv2.destroyAllWindows()
    


def call_server():
    client = actionlib.SimpleActionClient('crop_images_as', CropTheImageAction)
    client.wait_for_server()

    print "Wait completed"

    goal = CropTheImageGoal()
    goal.x_pix = 100
    goal.y_pix = 100
    goal.x_width = 100
    goal.y_width = 100

    print "Calling server"

    client.send_goal(goal, feedback_cb = feedback_cb)

    client.wait_for_result()

    result = client.get_result()

    return result


    
    
    
rospy.init_node('action_client')
print "Node init"
result = call_server()
print "Result generated"

image_msg = result.result_img

bridge = CvBridge()

crop_cv_image = bridge.imgmsg_to_cv2(image_msg)

cv2.imshow('image', crop_cv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()