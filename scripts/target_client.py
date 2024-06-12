#! /usr/bin/env python

## @package assignment_2_2023
#
# \file target_client.py
# \brief This node is the client of the action server, it sends the goal to the server and it can delete the goal or set a new one
# \author Andrea Chiappe
# \version 0.1
# \date 2024-05-29
# \details 
#
# Subscribes to: <BR>
#    /odom <BR>
#
# Publishes to: <BR>
#   /robot_info <BR>
#
# Clients: <BR>
#  /reaching_goal <BR>
#
# Description: <BR>
# This node is the client of the action server, it sends the goal to the server and it can delete the goal or set a new one. 
# The user can decide to delete the actual goal or set a new one. 
# The user can also decide to set a new goal or not. 
# The user can insert the coordinates of the target to reach. 
# The node sends the goal to the action server and prints the coordinates of the target to reach. 
# The node prints if the goal is reached or not. The node also prints if the goal is deleted or not
#


import rospy
import actionlib
import assignment_2_2023
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
from assignment_2_2023.msg import PlanningAction, RobotInfo, DistObj
from assignment_2_2023.srv import LastTrgPos, InfoRobot

# creates a goal to send to the action server
goal = assignment_2_2023.msg.PlanningGoal()
    
client = None ## \var client is the client of the action server
odom_sub = None ## \var sub is the subscriber of the topic /odom
info_pub = None ## \var pub is the publisher on topic /robot_info
dist_pub = None ## \var pub is the publisher on topic /dist
pose = None 


def odomCallback(msg):
    ##
    # \brief This function is the callback of the subscriber /odom
    # \param msg is the message of the subscriber
    
    global info_pub
    # declare the mesage i want to publish
    msg_robot = RobotInfo()
    # assign the value msg_robot
    msg_robot.x = msg.pose.pose.position.x 
    msg_robot.y = msg.pose.pose.position.y
    msg_robot.x_vel = msg.twist.twist.linear.x
    msg_robot.z_vel = msg.twist.twist.angular.z
    # publish the message
    info_pub.publish(msg_robot)
    

def laserCallback(msg):
    ##
    # \brief This function is the callback of the subscriber /scan
    # \param msg is the message of the subscriber
    
    global dist_pub
    dist = 1 # (msg.x2 + msg.y**2 + msg.z**2)**0.5
    result = DistObj()
    result.distance = dist
    dist_pub.publish(result)    
 

def targetPosition():
    ##
    # \brief This function is used to get the last target position
    # \return the last target position
    
    global pose
    rospy.wait_for_service("last_trg_pose")
    pos_proxy = rospy.ServiceProxy('last_trg_pose', LastTrgPos)
    try:
        pose = pos_proxy() 
        print (f'the last target ppsition was X: ', pose.x, 'Y: ', pose.y)
    except rospy.ServiceException as e:
        print(f"Service call failed: {e}")


def input_cord():
    ##
    # \brief This function is used to input the coordinates of the target to reach
    while True:
        try:
            x = float(input("Insert x coordinate (float): "))
            y = float(input("Insert y coordinate (float): "))
            print(f"You entered coordinates: x = {x}, y = {y}")
            return x, y
        except ValueError:
            print("Error: Please enter valid floating-point numbers.")
            
            
def send_goal_and_log(coords):
    ##
    # \brief This function is used to send the goal to the action server and print the coordinates of the target to reach
    
    global goal
    goal.target_pose.pose.position.x = coords[0]
    goal.target_pose.pose.position.y = coords[1]
    # Send goal to the action server
    client.send_goal(goal)
    #print to screen the coordinate of the target to reach
    rospy.loginfo("You sent the goal with: X = %f, Y = %f", goal.target_pose.pose.position.x, goal.target_pose.pose.position.y)


def get_user_deleteGoal():
    ##
    # \brief This function is used to get the user input to delete the actual goal or set a new one
    # \return True if the user wants to delete the actual goal
    # \return False if the user wants to insert a new target
   
    while True:
        user_input = input("Do you want to delete the actual goal (press 1) or insert a new target (press 2)")
        if user_input == "1":
            return True
        elif user_input == "2":
            return False
        else:
            print("Insert a correct key, press 1 or 2")


def set_user_newGoal():
    ##
    # \brief This function is used to get the user input to set a new goal or not
    # \return True if the user wants to set a new goal
    # \return False if the user doesn't want to set a new goal
    
    while True:
        user_input = input("Do you want to set a new Goal [y/n] ")
        if user_input == "y":
            return True
        elif user_input == "n":
            return False
        else:
            print("Insert a correct character, retry")


def target_client():
    ##
    # \brief This function is the main function of the node
    # \details
    # wait until the server process has started
    # if the user insert a new goal it send to the server
    # if the user wants to delete the actual goal it cancels the goal
    # if the user wants to insert a new target to reach it sends the new goal to the server
    # if the goal is reached it prints the message
    # if the goal is not reached it prints the message
    # if the goal is deleted it prints the message

    global client, goal
    coords_old = [None, None]
    # wait until the server process has started
    client.wait_for_server()
  
    while not rospy.is_shutdown():
        # first round there is no goal, the user could decide to set a new goal
        if coords_old[0] is None or coords_old[1] is None:
            # first round there is no goal, the user could decide to set a new goal
            if set_user_newGoal(): #is true if user decide to set a new goal
                #this function retur the coordinate setted by user
                coords = input_cord()
                send_goal_and_log(coords)
                # update the variable for the control of next loop
                coords_old = coords
            else:
                print("no goal is added, the robot has no goal to reach")
        else: # case when one goal is setted before
            if get_user_deleteGoal(): #returns true whn the user wants to delete the goal
                #cancel the goal
                if (client.get_state() == actionlib.GoalStatus.ACTIVE):
                    print("You canceled the goal with: X = ", goal.target_pose.pose.position.x," Y = ", goal.target_pose.pose.position.y)
                    client.cancel_goal() 
                else:
                    print("the goal is already deleted, press y and add a new goal")
                if set_user_newGoal(): #true if the user want to set a new goal after delete the last one
                    targetPosition()
                    coords = input_cord()
                    send_goal_and_log(coords)
                    # update the variable for the control of next loop
                    coords_old = coords  
            else :#user wants to insert a new target to reach   
                targetPosition()      
                coords = input_cord()
                goal.target_pose.pose.position.x = coords[0]
                goal.target_pose.pose.position.y = coords[1]
                # Send goal to the action server
                client.send_goal(goal)
                #prin to screen the new coordinate of the target
                rospy.loginfo("You sent the goal with: X = %f, Y = %f", goal.target_pose.pose.position.x, goal.target_pose.pose.position.y)
                coords_old = coords    
            
                             
        if client.get_state() == actionlib.GoalStatus.SUCCEEDED:
            rospy.loginfo("Goal reached successfully!")
        else:
            rospy.loginfo("Goal not reached.")
     
def main():
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node("trg_client")

        # create the SimpleActionClient, passing the type of action
        global client, odom_sub, info_pub, dist_pub
        client = actionlib.SimpleActionClient("/reaching_goal", assignment_2_2023.msg.PlanningAction)
        odom_sub = rospy.Subscriber("/odom", Odometry, odomCallback)
        info_pub = rospy.Publisher("/robot_info", RobotInfo, queue_size = 1)
        laser_sub = rospy.Subscriber("/scan", LaserScan, laserCallback)
        dist_pub = rospy.Publisher("/dist", DistObj, queue_size = 1)
        target_client()

    except Exception as e:
        rospy.logerr(f"ERROR trg_client: {e}")


main()


