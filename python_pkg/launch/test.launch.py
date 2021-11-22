from launch import LaunchDescription
from launch_ros.actions import Node

py_pkg='python_pkg'

def generate_launch_description():
    python_pub=Node(package=py_pkg,executable='python_node_pub')
    python_sub=Node(package=py_pkg,executable='python_node_sub')

    return LaunchDescription([
        python_sub,
        python_pub,
    ])