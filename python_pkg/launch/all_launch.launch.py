import os
from launch import LaunchDescription
from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory

from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    python_nodes = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('python_pkg'), ''),
            '/test.launch.py'])
        )
    cpp_nodes = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('cpp_pkg'), 'launch'),
            '/test.launch.py'])
        )
    return LaunchDescription([
        python_nodes,
        cpp_nodes,
    ])