cmake_minimum_required(VERSION 3.8)
project(nodes_topics_cpp)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

add_executable(my_node src/my_node.cpp)
ament_target_dependencies(my_node rclcpp)

add_executable(number_pub_node_cpp src/number_pub_node_cpp.cpp)
ament_target_dependencies(number_pub_node_cpp rclcpp std_msgs)

add_executable(counter_node_cpp src/counter_node_cpp.cpp)
ament_target_dependencies(counter_node_cpp rclcpp std_msgs)

install(TARGETS 
  my_node
  number_pub_node_cpp
  counter_node_cpp 
  DESTINATION lib/${PROJECT_NAME}

)

ament_package()
