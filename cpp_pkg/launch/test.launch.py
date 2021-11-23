from launch import LaunchDescription
from launch_ros.actions import Node

cpp_pkg='cpp_pkg'

def generate_launch_description():
    cpp_pub=Node(package=cpp_pkg,executable='cpp_publisher')
    cpp_sub=Node(package=cpp_pkg,executable='cpp_subscriber')
    client_cpp=Node(package=cpp_pkg,executable='client_cpp')

    return LaunchDescription([
        cpp_sub,
        cpp_pub,
        client_cpp,
    ])