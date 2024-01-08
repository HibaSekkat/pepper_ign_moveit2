cmake_minimum_required(VERSION 3.5)
project(pepper_robot_description)

# Find dependencies
find_package(ament_cmake REQUIRED)

set(SCRIPTS_DIR scripts)
install(PROGRAMS
    ${SCRIPTS_DIR}/xacro2sdf_direct.bash
    ${SCRIPTS_DIR}/xacro2sdf.bash
    ${SCRIPTS_DIR}/xacro2urdf.bash
    DESTINATION lib/${PROJECT_NAME}
)

# Install directories
install(DIRECTORY config launch pepper_robot pepper_robot/meshes rviz urdf DESTINATION share/${PROJECT_NAME})

ament_environment_hooks("${CMAKE_CURRENT_SOURCE_DIR}/hooks/${PROJECT_NAME}.dsv.in")
ament_environment_hooks("${CMAKE_CURRENT_SOURCE_DIR}/hooks/${PROJECT_NAME}.sh.in")

# Setup the project
ament_package()
