#! /usr/bin/env python3

## @package assignment_2_2023
#
# \file InfoRobot_server.py
# \brief This file contains the implementation of the server for the service InfoRobot
# \author Andrea Chiappe
# \version 0.1
# \date 2024-05-29
#
# Subscribes to: <BR>
#    /reaching_goal/goal <BR>
#    /robot_info <BR>
#
# Publishes to: <BR>
#    None <BR>
#
# Services: <BR>
#    /InfoRobot <BR>
#
# Description: <BR>
# This node contains the implementation of ascubscriber to the position and velocity of the robot. 
# and a subscriber to the position of the target.
# This node implements a server that to retreive the distance between the robot and the target and the average velocity of the robot. 
import rospy
import math
import assignment_2_2023.msg
import assignment_2_2023.srv
from assignment_2_2023.msg import PlanningActionGoal, RobotInfo 
from assignment_2_2023.srv import InfoRobot, InfoRobotResponse

goal_pose = [0, 0] # goal_pose[0] = x, goal_pose[1] = y
robot_pose = [0, 0] # robot_pose[0] = x, robot_pose[1] = y
robot_vel_x = [] # array with the linear velocity 
robot_vel_z = [] # array with the anguar velocity 
window = None # window size

def update_arr(array, window, element):
    ##
    # \brief Update the array with the new element
    # \param array list of element
    if(len(array) < window):
        array.append(element)
    else:
        array.append(element)
        array.pop(0)

def srvCallback(req):
    ## 
    # \brief Callback for the service InfoRobot
    # \param req request for the service 
    global goal_pose, robot_pose, robot_vel_x, robot_vel_z, window
    try:
        # compute the distance between the goal and robot
        distance = math.sqrt(((goal_pose[0] - robot_pose[0]) ** 2) + ((goal_pose[1] - robot_pose[1]) ** 2))

        # compute the average for the x_vel
        len_array_x = len(robot_vel_x)
        x_vel_avg = sum(robot_vel_x) / len_array_x if len_array_x > 0 else 0

        # compute the average for the z_vel
        len_array_z = len(robot_vel_z)
        z_vel_avg = sum(robot_vel_z) / len_array_z if len_array_z > 0 else 0

        # return all the elements computed
        return InfoRobotResponse(distance, x_vel_avg, z_vel_avg)
    except Exception as e:
        rospy.logerr(f"An error occurred in srvCallback: {str(e)}")
        return InfoRobotResponse(0, 0, 0)  # Return default values in case of an error


def sub_goalCallback(msg):
    ## 
    # \brief Callback for the subscriber to the goal
    # \param msg message from the topic
    
    global goal_pose
    try:
        # I subscribe to the publisher /reaching_goal/goal
        # The data are in format PlanningGoal
        goal_pose[0] = msg.goal.target_pose.pose.position.x
        goal_pose[1] = msg.goal.target_pose.pose.position.y
    except Exception as e:
        rospy.logerr(f"An error occurred in sub_goalCallback: {str(e)}")

def sub_robotCallback(msg):
    ## 
    # \brief Callback for the subscriber to the robot
    # \param msg message from the topic
    
    global robot_pose, robot_vel_x, robot_vel_z, window
    try:
        # update all the values inside the global variable
        robot_pose[0] = msg.x
        robot_pose[1] = msg.y
        update_arr(robot_vel_x, window, msg.x_vel)
        update_arr(robot_vel_z, window, msg.z_vel)
    except Exception as e:
        rospy.logerr(f"An error occurred in sub_robotCallback: {str(e)}")



def last_target_server():
    ## 
    # \brief Main function to initialize the server
    global service, window
    #initialize the service 
    rospy.init_node("InfoRobot_server")
    window= rospy.get_param("/ws_size")

    service = rospy.Service('/InfoRobot', InfoRobot, srvCallback)
    rospy.loginfo("Service InfoRobot is ready")
    # nee to subscribe to reach_goal/goal for see the information about the goal
    sub_goal = rospy.Subscriber("/reaching_goal/goal", PlanningActionGoal, sub_goalCallback)
    sub_robot = rospy.Subscriber("/robot_info", RobotInfo, sub_robotCallback)
    rospy.spin()
    
        
last_target_server()
