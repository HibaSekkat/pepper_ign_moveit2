cmake_minimum_required(VERSION 3.5)
project(pepper_robot_ign)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(pepper_robot_description REQUIRED)
find_package(pepper_robot_moveit_config REQUIRED)

# Install directories
install(DIRECTORY launch rviz worlds DESTINATION share/${PROJECT_NAME})

# Install python examples
set(EXAMPLES_DIR examples)
install(PROGRAMS
    ${EXAMPLES_DIR}/ex_follow_target.py
    DESTINATION lib/${PROJECT_NAME}
)

# Setup the project
ament_package()
