import os
from launch import LaunchDescription
from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory

from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

py_pkg='python_pkg'

def generate_launch_description():
    python_pub=Node(package=py_pkg,executable='python_node_pub')
    python_sub=Node(package=py_pkg,executable='python_node_sub')
    cpp_nodes = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('cpp_pkg'), 'launch'),
            '/test.launch.py'])
        )
    return LaunchDescription([
        python_sub,
        python_pub,
        cpp_nodes,
    ])