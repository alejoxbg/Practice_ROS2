FROM ros:foxy

RUN mkdir -p /dev_ws/src/cpp_pkg/ && mkdir -p /dev_ws/src/python_pkg/

COPY ["python_pkg/", "/dev_ws/src/python_pkg/"]

COPY ["cpp_pkg/", "/dev_ws/src/cpp_pkg/"]

WORKDIR /dev_ws

RUN . /opt/ros/$ROS_DISTRO/setup.sh && colcon build && echo "source /dev_ws/install/setup.bash" >> /etc/bash.bashrc

#CMD ["ros2" ,"run","python_pkg","python_node_pub"]
#CMD ["ros2" ,"launch","test.launch.py"]
