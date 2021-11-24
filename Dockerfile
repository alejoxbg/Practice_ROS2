FROM ros:foxy

RUN mkdir -p /dev_ws/src/cpp_pkg/ && mkdir -p /dev_ws/src/python_pkg/ && mkdir -p /dev_ws/src/custom_msg_srv/

WORKDIR /dev_ws/src

RUN git clone https://github.com/ros2/example_interfaces.git

WORKDIR /dev_ws



COPY ["python_pkg/", "/dev_ws/src/python_pkg/"]

COPY ["cpp_pkg/", "/dev_ws/src/cpp_pkg/"]

COPY ["custom_msg_srv/", "/dev_ws/src/custom_msg_srv/"] 

COPY ["init.sh","/"]

RUN chmod +x /init.sh

RUN . /opt/ros/$ROS_DISTRO/setup.sh && colcon build --packages-select custom_msg_srv example_interfaces  && echo "source /dev_ws/install/setup.bash" >> /etc/bash.bashrc && . install/setup.sh && colcon build --packages-select cpp_pkg python_pkg && . install/setup.sh


ENTRYPOINT ["/init.sh"]

CMD ["bash"]
#CMD ["ros2" ,"launch","test.launch.py"]
