# ROS2 For ROS1 Users

## Environment Configuration
* For ROS Melodic: echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
* For ROS Dashing: echo "source /opt/ros/dashing/setup.bash" >> ~/.bashrc

## Installing packages
* For ROS Melodic: sudo apt install ros-melodic-std-msgs
* For ROS Dashing: sudo apt install ros-dashing-std-msgs

## ROS1 to ROS2 command line tools
* ROS Melodic: roslaunch <package name> <launch file>
* ROS Dashing: ros2 launch <package name> <launch file>
* ROS Melodic: rosrun <package name> <launch file>
* ROS Dashing: ros2 run <package name> <launch file>
* ROS Melodic: rostopic list
* ROS Dashing: ros2 topic list
* ROS Melodic: rostopic echo <topic name>
* ROS Dashing: ros2 topic echo <topic name>
* ROS Melodic: rosservice list
* ROS Dashing: ros2 service list
* ROS Melodic: rosbag play <bag file>
* ROS Dashing: ros2 bag <bag file>
* ... etc

## Creating and compiling packages
* ROS Melodic: catkin_create_package <package_name>
* ROS Dashing: ros2 pkg create <package_name>
* ROS Melodic: catin_make OR catkin build
* ROS Dashing: colcon build --symlink-install

