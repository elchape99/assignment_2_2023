# Assignment 2 Research Track

This project is based on the use of ros and python. The main task is about writing a node and two service node that interact with a system provided by prfessor.
The system provided is a roboth with some sensors, and an arena.
The robot is also simulate with gazebo and rvitz, for simulate the motion. The robot consins on a non holonomic robot, so it can move long his x-axe and rotate around its z-axe. My ilmpelemtantion was about:
- in the first node the user could send a goal to robot, and the robot start going to it ad give back some information about the state, and know when the goal is reached. Also this node subscribe to a certain topic /odom. This topic is about the motion, catch the robot position and velocity (x, y, x_vel, z_vel) using a custome message called in my case RobotInfo. This node also publish this custom message on a topic called /robot_info
- service node, LastTrgPos_server, when it is called it returnsthe coordinate of the last target sent by user
- the last service node InfoRobot_server thaht return when called a distance of robot respect to goal and a robot speed average considering a certain windows of value.

## Installation

For the isntallation, clone this git repository inside the src folder of the ros workspace. afer clone change to branch master


git checkout master

before running the code is importanto to install using apt the pakage xterm
 sudo apt update
 sudo apt instll xterm

After the isntallations of xterm, in the srv folder of ros workspace run the command catkin_make. This command will built all the exeguibile files in the repository.
At this point the gazebo and rvitz will open and yuo can see the arena with the robot, and the data coming from sensors looking in rvitz.

In the window will be open also another terminal, xterm, in wicht folowing the instruction you will add a goal. After add the gol the first time you will delete it or change it. 

Also when the simulator is running is possible to run the two service.
For know the information about the last insereted goal you can use the service /LastTrgPos usig in terminal the line
rosservice call InfoRObot

For know the information about the distance from robot to goal and the average speed of the robot you can use the service /InfoRobot calling in the terminal
rosservice call InfoRobot


# Assignment 2 Research Track

This project is based on the use of ROS and Python. The main task involves writing a node and two service nodes that interact with a system provided by the professor. The system consists of a robot with some sensors and an arena. The robot is simulated using Gazebo and RViz for motion simulation. The robot is a non-holonomic robot, capable of moving along its x-axis and rotating around its z-axis.

My implementation includes:

- In the first node, the user can send a goal to the robot, and the robot starts moving towards it, providing information about the state. It notifies when the goal is reached. This node subscribes to the topic `/odom` to capture the robot's position and velocity (x, y, x_vel, z_vel) using a custom message called `RobotInfo`. This node also publishes this custom message on a topic called `/robot_info`.

- The service node `LastTrgPos_server`, when called, returns the coordinates of the last target sent by the user.

- The service node `InfoRobot_server` returns, upon calling, the distance of the robot relative to the goal and the average robot speed considering a certain window of values.

## Installation

For installation, clone this git repository inside the `src` folder of the ROS workspace.
Before running the code, it's important to install the xterm package using the following commands:

```bash
sudo apt update
sudo apt install xterm
```
After installing xterm, in the srv folder of the ROS workspace, run the command catkin_make. This command will build all the executable files in the repository.

Now for running the program need to launch the launch file:

```bash
roslaunch assignment_2_2323.launch assignment1.launch
```


At this point, Gazebo and RViz will open, allowing you to see the arena with the robot and the data coming from sensors in RViz.

Another terminal, xterm, will also open, in which you can follow the instructions to add a goal. After adding the goal for the first time, you can either delete it or change it.

While the simulator is running, you can use the two services. To get information about the last inserted goal, you can use the service /LastTrgPos by calling:

```bash
rosservice call LastTrgPos
```

For knowin information about the distanche between the robot and goal, and the average speed in window of 10 mesurement is possible to call the service /InfoRobot. Is possible to change the size of the windows in the launch file assignemnt1.launch inside the launch folder.

```bash
rosservice call InfoRobot
```

For entering in the detail of the first node create `target_client.py` here there is a flowchart about the working of this node:

![target_client.py workflow ](Untitled_Diagram_drawio.png)


