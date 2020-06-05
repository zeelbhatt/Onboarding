#! /usr/bin/env python

import rospy
import actionlib
from crop_action_server.msg import CropTheImageAction, CropTheImageFeedback, CropTheImageResult
from cv_bridge import CvBridge
import cv2

class ActionServer():

    def __init__(self):
        self.a_server = actionlib.SimpleActionServer("crop_images_as", CropTheImageAction, execute_cb=self.execute_cb, auto_start=False)
        self.a_server.start()
        print "In init"


    def execute_cb(self,  goal):
        bridge = CvBridge()
        input_img = cv2.imread('/home/zeel/Pictures/sample.png')
        
        print "In Execute Callback "
        success = True
        feedback = CropTheImageFeedback()
        result = CropTheImageResult()
        rate = rospy.Rate(0.2)
        # x = goal.x_pix
        # y = goal.y_pix
        width = input_img.shape[1]
        hieght = input_img.shape[0]
        x = 50
        y = 50
        
        while input_img.shape[1] > goal.x_width:
            if self.a_server.is_preempt_requested():
                success = False
                print "Server failed"
                break
            
            print "Server called"
            
            hieght = hieght - 100  #The Hieght of croped image
            width = width - 100   #The Width of croped image

            input_img = input_img[y:y+hieght, x:x+width]
            image_message = bridge.cv2_to_imgmsg(input_img, encoding="passthrough")

            


            feedback.feedback_img = image_message
            
            self.a_server.publish_feedback(feedback)
            rate.sleep()

        result.result_img = image_message
        if success:
            self.a_server.set_succeeded(result)



rospy.init_node("action_server")
s = ActionServer()
rospy.spin()