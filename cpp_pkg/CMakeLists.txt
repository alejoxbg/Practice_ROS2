cmake_minimum_required(VERSION 3.5)
project(cpp_pkg)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(custom_msg_srv REQUIRED)
find_package(example_interfaces REQUIRED)

#ADDING NODES
add_executable(cpp_publisher src/cpp_pub.cpp)
ament_target_dependencies(cpp_publisher rclcpp std_msgs example_interfaces)

add_executable(cpp_subscriber src/cpp_sub.cpp)
ament_target_dependencies(cpp_subscriber custom_msg_srv rclcpp example_interfaces)

add_executable(client_cpp src/client_cpp.cpp)
ament_target_dependencies(client_cpp rclcpp std_msgs example_interfaces)

install(TARGETS
  cpp_publisher
  cpp_subscriber
  client_cpp
  DESTINATION lib/${PROJECT_NAME})
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

#ADDING LAUNCH FILES
install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}/
)


ament_package()
