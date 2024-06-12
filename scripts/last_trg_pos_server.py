#! /usr/bin/env python3

## @package assignment_2_2023
#
# \file LastTrgPos_server.py
# \brief This is a server that provides the last target position
# \author Andrea Chiappe
# \version 0.1
# \date 2024-05-29 
#
# Subscribes to: <BR>
#    /reaching_goal/goal <BR>
#
# Service to: <BR>
#    /LastTrgPos <BR>
#
# Description: <BR>
# The server provides the last target position. 
# The server subscribes to the topic /reaching_goal/goal to get the information about the goal. 
# The service /LastTrgPos provides the last target position. <BR>



import rospy
import assignment_2_2023.msg
import assignment_2_2023.srv
from assignment_2_2023.msg import PlanningActionGoal 
from assignment_2_2023.srv import LastTrgPos, LastTrgPosResponse

service = None

x_cord = None
y_cord = None


def srvCallback(req):

    global x_cord, y_cord    
    return LastTrgPosResponse(x_cord, y_cord)
    

def subCallback(msg):
    ##
    # \brief callback function for the subscriber at topic /reaching_goal/goal, the data are formatted in msg type PlanningGoal
    global x_cord, y_cord
    x_cord = msg.goal.target_pose.pose.position.x
    y_cord = msg.goal.target_pose.pose.position.y

def last_target_server():
    ## 
    # \brief function to initialize the node, the service and the subscriber

    global service
    #initialize the service 
    rospy.init_node("last_trg_pose_server")
    service = rospy.Service('/last_trg_pose', LastTrgPos, srvCallback )
    rospy.loginfo("Service LastTrgPos is ready")
    # nee to subscribe to reach_goal/goal for see the information about the goal
    sub = rospy.Subscriber("/reaching_goal/goal", PlanningActionGoal, subCallback)
    rospy.spin()
    
        
last_target_server()
