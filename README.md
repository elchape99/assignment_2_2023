# Project Overview

This project is based on the use of ROS and Python. The main task involves writing a node and two service nodes that interact with a system provided by the professor. The system consists of a robot with some sensors and an arena. The robot is simulated using Gazebo and RViz for motion simulation. The robot is a non-holonomic robot, capable of moving along its x-axis and rotating around its z-axis.

## Implementation Details

### Node Descriptions

1. **First Node**:
    - The user can send a goal to the robot, and the robot starts moving towards it, providing information about the state and notifying when the goal is reached.
    - Subscribes to the topic `/odom` to capture the robot's position and velocity (x, y, x_vel, z_vel) using a custom message called `RobotInfo`.
    - Publishes this custom message on a topic called `/robot_info`.

2. **Service Node: `LastTrgPos_server`**:
    - Returns the coordinates of the last target sent by the user when called.

3. **Service Node: `InfoRobot_server`**:
    - Returns the distance of the robot relative to the goal and the average robot speed considering a certain window of values when called.

## Installation

### Using Docker

1. Pull the Docker image:
    ```bash
    docker pull carms84/noetic_ros2
    ```

2. Run the Docker image:
    ```bash
    docker run -it --name my_ros -p 6080:80 -p 5900:5900 carms84/noetic_ros2
    ```

3. To start a brand new container, also forwarding port 8888:
    ```bash
    docker run -it --name my_jupyter -p 6080:80 -p 5900:5900 -p 8888:8888 carms84/noetic_ros2
    ```

4. Add the following line to the end of your `.bashrc` file:
    ```bash
    source /opt/ros/noetic/setup.bash
    ```

### Cloning the Repository

1. Clone this git repository inside the `src` folder of the ROS workspace:
    ```bash
    git clone https://github.com/elchape99/rt1_assignment_2.git
    ```

2. Change the name of the cloned folder from `rt1_assignment_2` to `assignment_2_2023`.

3. If using the Docker image, add this line to your `.bashrc` file:
    ```bash
    source ~/my_ros/devel/setup.bash
    ```

4. Update all packages and install the `xterm` package:
    ```bash
    sudo apt update
    sudo apt install xterm
    ```

5. Build the executable files in the repository:
    ```bash
    catkin_make
    ```

6. Launch the program:
    ```bash
    roslaunch assignment_2_2023 assignment1.launch
    ```

## Usage

Once the program is running, Gazebo and RViz will open, allowing you to see the arena with the robot and the data coming from sensors in RViz. Another terminal, `xterm`, will also open, where you can follow the instructions to add a goal. After adding the goal for the first time, you can either delete it or change it.

### Services

- To get information about the last inserted goal, call the `/LastTrgPos` service:
    ```bash
    rosservice call /LastTrgPos
    ```

- To get information about the distance between the robot and the goal, and the average speed over a window of 10 measurements, call the `/InfoRobot` service. You can change the window size in the `assignment1.launch` file inside the `launch` folder:
    ```bash
    rosservice call /InfoRobot
    ```

## Flowchart

For detailed information on the first node (`target_client.py`), refer to the following flowchart:

![Flowchart](path_to_flowchart_image)

Feel free to reach out if you have any questions or need further assistance!


[target_client.py workflow ](https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Untitled%20Diagram.drawio#R5VrbcqM4EP0aV%2B0%2BOAXi6sdxbpPZ7FS2kt3sPE1pjAJsMPIIEdvz9SsZiZuA4MTYifOSoNaV7j6nW41Hxul8dUngIvgTeygaAc1bjYyzEQDA0U32j0vWmcS1jUzgk9DLRHohuA1%2FISHUhDQNPZRUBlKMIxouqsIZjmM0oxUZJAQvq8MecFTddQF9pAhuZzBSpfehRwPxFsAp5J9R6AdyZ92eZD1zKAeLN0kC6OFlSWScj4xTgjHNnuarUxRx5Um93F%2Bt76PrR%2Fvyy1%2FJT%2Fj39I%2B7r%2F%2BMs8UutpmSvwJBMX3x0jffo%2FMxuHl8%2BHLthf718vEKncqln2CUCn2NgB2xTaYPmO3FXpquhSbtnymWHeNkY%2BdPbIBuLpivTIt%2B9uTz%2F3eELSkWY6fK1su6hD7zpQHymM1EExMaYB%2FHMDovpFOC09hD%2FFU01irGXGO8YEKdCf9DlK6FA8KUYiYK6DwSvdmefKOaXzyjVDEuwSmZoY5xtvBtSHxEOzReeA6DHMJzRMmazSMogjR8qh4OCt%2F383GFfdmDMPEW5nYUc1%2FAKEGHsAf3B9HJKObt2Mfek326Dlmyz9UDazPO%2Bz7DmHjsmYt5j%2FYVx6rhSIDnP1J2rOkyCCm6XcCNUpaM26vqz8lME7a4gPMw4hz%2FGUVPiIYzWDMS08oURqEfs8aM2QQRvgwl%2BDEn1s3CbMsw9lnLLlp3G6cYF3bua9YnRChalZSuWkb0GpqgaRGndEnby4L1dUfIghLjW9pAYLMauPVd8147n%2FXAlXlI3tMUUySIR7cYLdnfSwzZahc7AtNLIaG4el8jtULCAlVI5DlZGRLWPiEB%2Bsaf2PvEcz%2FWijnNVbRdhQRahfRf%2Fnxiida3Us%2FZqtxYl%2FiuHHuYksm6tAhvfhO7bRrFMpuWXOetxKyWnKJk5i4r94ag2OEGh5vUUBLvpOplBqh5T%2FaaYlY5Qa0tZNcYHExqC2V6UBZingLXpWELPiDpOLBrVfZxtc5jObb2muFSHX3fetvxUksFLDN9FCDNPeLluNXVxPEYY5nZE2%2F6vpLErlOWbFHODdnkeJHSLF%2F87Xd5A%2FtB5OWrnkzyq%2FemVbPn%2B4x5hluDh9sQ8wxLZUN7qJinq0Evuxof1Z2r%2FS7VB08tNt0PnsDHILe%2BxgAHJTf1BrwgKEl4oWnEq3%2BMxjQPRYgyAGk%2BT9wVgpMTQD5hFsDY5xNogAoVHE2635HeA6eB6pzB0nuV6o4RSbqsYz8LpYPymjxmyRpnEjmbK%2B9xRPwxMGohv6nyozVcgMzBQv7kY%2BCgd3x3D4oDNaYkaO7l8eMoUGC4zkn1Wms2wQDstdqjKcrdg9c3F4RkT3NBaHCkvBYALbUGq7E0seuCiWm6lW1scaVpK1G4mt41fqAShaug%2FClMUhhxP%2BE%2BCGmaHC3YLdPqB3Y5bvdgV2Peoa65kgH0Ev4LNuhXEh6aEV6dGjZDTzdr1USrZu8WStgVCmUqNsQPCsSngjfzi4I80GzhZu%2FUreo1%2FoECzRhYze7bFmmUCUCEntYJ%2BmTSNWGY2ATUm5jy%2FfFoqhFt1zKj77VsuPKE%2ByHy0Z2j36yBzNb7wV%2BNToZ14tRvKbUA1fK1cFsq0Q37BNRyJN145nSTZ6YMxA5N99OCHWS1sl7mVHz5ffKEU09lDbtnKvuCLzasWfxeM7Nf8atX4%2Fx%2F)


# Research Track II


## Documentation about rt1_assignemnt_1 (Assignment1_ RT2)
In this specific case the work is not related to the previous part but related to the part of research track 1. So this section will contain all the documentation about the python code od the assignemt 1. The documentation is seen in the following link:\
https://elchape99.github.io/rt1_assignment_2/


## User interface (Assignment2_RT2)
This project is based on the working done in the Last semester assignment, so based on all the topic seen in the upper part of the README.\\
Resoect the previous pare I have added:
- file `Assignment2.ipynb` that contain a jupyter node that implement a user inteface, allowing the user to send new goal, delete goal, and showing some details about the story of goal sended and deleted.\\

### How to run it
For running the node:
- First the environment on ros must to be run, see the isntruction on README upper part
- After the ros node is runnin is important to run the jupyter notebook with the command
```bash
jupyter notebook --allow-root --ip 0.0.0.0
```

Now open a browser on the host and go to:\\
http://localhost:8888

