# Assignment 2 Research Track

This project is based on the use of ROS and Python. The main task involves writing a node and two service nodes that interact with a system provided by the professor. The system consists of a robot with some sensors and an arena. The robot is simulated using Gazebo and RViz for motion simulation. The robot is a non-holonomic robot, capable of moving along its x-axis and rotating around its z-axis.

My implementation includes:

- In the first node, the user can send a goal to the robot, and the robot starts moving towards it, providing information about the state. It notifies when the goal is reached. This node subscribes to the topic `/odom` to capture the robot's position and velocity (x, y, x_vel, z_vel) using a custom message called `RobotInfo`. This node also publishes this custom message on a topic called `/robot_info`.

- The service node `LastTrgPos_server`, when called, returns the coordinates of the last target sent by the user.

- The service node `InfoRobot_server` returns, upon calling, the distance of the robot relative to the goal and the average robot speed considering a certain window of values.

## Installation

- In the case of my project I develop all the code using the docker image. If use the same docker immage follow these followiong passage, if not skip to the part of cloning repository
```bash
docker pull carms84/noetic_ros2
```

- For run the docker image I use the command line in the bash:
```bash
docker run -it --name my_ros -p 6080:80 -p 5900:5900 carms84/noetic_ros2
```

- After this passage, if use the docker image, have to write inside the `.bashrc` file the following line of code, at the end of file:
```bash
source /opt/ros/noetic/setup.bash
```

Now is possible to clone this git repository inside the `src` folder of the ROS workspace. (This passage for everyone, using or not the docker image)

- After clone the folder in the src folder, is importan to to change the name of the folder cloned. The name is to change with this:
```bash
assignment_2_2023
```

- Only for who use the docker image, write this row of code inide the `.bashrc` file
```bash
source ~/my_ros/devel/setup.bash
```
- Before running the code, it's important to update all the packages installed and install the xterm package using the following commands:

```bash
sudo apt update
sudo apt install xterm
```
After installing xterm, in the srv folder of the ROS workspace, run the command catkin_make. This command will build all the executable files in the repository.

- Now for running the program need to launch the launch file:

```bash
roslaunch assignment_2_2023 assignment1.launch
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

[target_client.py workflow ](https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Untitled%20Diagram.drawio#R5VrbcqM4EP0aV%2B0%2BOAXi6sdxbpPZ7FS2kt3sPE1pjAJsMPIIEdvz9SsZiZuA4MTYifOSoNaV7j6nW41Hxul8dUngIvgTeygaAc1bjYyzEQDA0U32j0vWmcS1jUzgk9DLRHohuA1%2FISHUhDQNPZRUBlKMIxouqsIZjmM0oxUZJAQvq8MecFTddQF9pAhuZzBSpfehRwPxFsAp5J9R6AdyZ92eZD1zKAeLN0kC6OFlSWScj4xTgjHNnuarUxRx5Um93F%2Bt76PrR%2Fvyy1%2FJT%2Fj39I%2B7r%2F%2BMs8UutpmSvwJBMX3x0jffo%2FMxuHl8%2BHLthf718vEKncqln2CUCn2NgB2xTaYPmO3FXpquhSbtnymWHeNkY%2BdPbIBuLpivTIt%2B9uTz%2F3eELSkWY6fK1su6hD7zpQHymM1EExMaYB%2FHMDovpFOC09hD%2FFU01irGXGO8YEKdCf9DlK6FA8KUYiYK6DwSvdmefKOaXzyjVDEuwSmZoY5xtvBtSHxEOzReeA6DHMJzRMmazSMogjR8qh4OCt%2F383GFfdmDMPEW5nYUc1%2FAKEGHsAf3B9HJKObt2Mfek326Dlmyz9UDazPO%2Bz7DmHjsmYt5j%2FYVx6rhSIDnP1J2rOkyCCm6XcCNUpaM26vqz8lME7a4gPMw4hz%2FGUVPiIYzWDMS08oURqEfs8aM2QQRvgwl%2BDEn1s3CbMsw9lnLLlp3G6cYF3bua9YnRChalZSuWkb0GpqgaRGndEnby4L1dUfIghLjW9pAYLMauPVd8147n%2FXAlXlI3tMUUySIR7cYLdnfSwzZahc7AtNLIaG4el8jtULCAlVI5DlZGRLWPiEB%2Bsaf2PvEcz%2FWijnNVbRdhQRahfRf%2Fnxiida3Us%2FZqtxYl%2FiuHHuYksm6tAhvfhO7bRrFMpuWXOetxKyWnKJk5i4r94ag2OEGh5vUUBLvpOplBqh5T%2FaaYlY5Qa0tZNcYHExqC2V6UBZingLXpWELPiDpOLBrVfZxtc5jObb2muFSHX3fetvxUksFLDN9FCDNPeLluNXVxPEYY5nZE2%2F6vpLErlOWbFHODdnkeJHSLF%2F87Xd5A%2FtB5OWrnkzyq%2FemVbPn%2B4x5hluDh9sQ8wxLZUN7qJinq0Evuxof1Z2r%2FS7VB08tNt0PnsDHILe%2BxgAHJTf1BrwgKEl4oWnEq3%2BMxjQPRYgyAGk%2BT9wVgpMTQD5hFsDY5xNogAoVHE2635HeA6eB6pzB0nuV6o4RSbqsYz8LpYPymjxmyRpnEjmbK%2B9xRPwxMGohv6nyozVcgMzBQv7kY%2BCgd3x3D4oDNaYkaO7l8eMoUGC4zkn1Wms2wQDstdqjKcrdg9c3F4RkT3NBaHCkvBYALbUGq7E0seuCiWm6lW1scaVpK1G4mt41fqAShaug%2FClMUhhxP%2BE%2BCGmaHC3YLdPqB3Y5bvdgV2Peoa65kgH0Ev4LNuhXEh6aEV6dGjZDTzdr1USrZu8WStgVCmUqNsQPCsSngjfzi4I80GzhZu%2FUreo1%2FoECzRhYze7bFmmUCUCEntYJ%2BmTSNWGY2ATUm5jy%2FfFoqhFt1zKj77VsuPKE%2ByHy0Z2j36yBzNb7wV%2BNToZ14tRvKbUA1fK1cFsq0Q37BNRyJN145nSTZ6YMxA5N99OCHWS1sl7mVHz5ffKEU09lDbtnKvuCLzasWfxeM7Nf8atX4%2Fx%2F)


