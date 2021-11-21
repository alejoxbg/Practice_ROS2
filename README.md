# Practice_ROS2
Just a practice to remember the basics about git, docker, python, c++ and ROS2


# ros2

## Resolve dependencies
```
#in your workspace
rosdep install -i --from-path src --rosdistro foxy -y
```

## Compile all the packages
```
colcon build
```
## source local_setup
```
#in your workspace root
. install/setup.bash
```

# ROS2 Packages

## python
Contains:

- package.xml file containing meta information about the package

- setup.py containing instructions for how to install the package

- setup.cfg is required when a package has executables, so ros2 run can find them

- /<package_name> - a directory with the same name as your package, used by ROS 2 tools to find your package contains __init__.py

## Creating Packages
```
ros2 pkg create --build-type ament_python <package_name>
```

## run a node
```
# in src
ros2 run my_package my_node
```
