# Practice_ROS2
Just a practice to remember the basics about git, docker, python, c++ and ROS2

This ROS2 package includes nodes in python and C++, subscriber and publisher for each one with custom msg, a ROS2 custom service in python (c++ on working) and a docker file to build a image and run the package with docker, algo i upload the docker imag to my repository if you want to test it. 


# Installation for local build

1. Clone the project repository in your ros2 worspace

```
git clone https://github.com/alejoxbg/Practice_ROS2.git
```

2. Build your ros2 worspace 
```
colcon build
source intall/setup.bash
```
# Run
```
ros2 lanuch python_pkg all_launch.launch.py
```

# Installation for docker
```
docker pull alejoxbg/test_ros2:latest
```

# Run
```
docker-compose up
```


# To do


- buils a ros2 foxy image with:
    - a copy of my workspace  ✅
    - build that workspace ✅
    - source that workspace ✅
    - run automaticly the roslaunch ✅
- The launchers might contains:
    - a publisher/suscriber of python publish to C++ node ✅
    - a publisher/suscriber of C++ publish to python node ✅
    - a service between those nodes ✅
    - at least a custom msg ✅
    - at leas a custom service ✅
    - 2 containers that cominucate each other 

PD: I will use docker compose to this


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

# ROS2 Packages python

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
# ROS2 Packages C++

Contains:

- package.xml file containing meta information about the package

- CMakeLists.txt file that describes how to build the code within the package


## Creating Packages
```
ros2 pkg create --build-type ament_cmake <package_name>
```

## run a node
```
# in src
ros2 run my_package my_node
```
