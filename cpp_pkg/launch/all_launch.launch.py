import os
from launch import LaunchDescription
from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory

from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

cpp_pkg='cpp_pkg'

def generate_launch_description():
    cpp_pub=Node(package=cpp_pkg,executable='cpp_publisher')
    cpp_sub=Node(package=cpp_pkg,executable='cpp_subscriber')
    python_nodes = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('python_pkg'), ''),
            '/test.launch.py'])
        )
    return LaunchDescription([
        cpp_sub,
        cpp_pub,
        python_nodes,
    ])