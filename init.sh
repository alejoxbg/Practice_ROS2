#!/bin/bash
. /opt/ros/$ROS_DISTRO/setup.sh

#colcon build --packages-select custom_msg_srv

#. install/setup.sh

#colcon build

. install/setup.sh

exec "$@"
#ros2 launch python_pkg all_launch.launch.py
