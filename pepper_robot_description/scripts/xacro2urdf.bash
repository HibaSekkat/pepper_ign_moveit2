#!/usr/bin/env bash
# This script converts xacro (URDF variant) into URDF for `pepper_robot_description` package

SCRIPT_DIR="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")" &>/dev/null && pwd)"
XACRO_PATH="$(dirname "${SCRIPT_DIR}")/urdf/pepper_robot.xacro"
URDF_PATH="$(dirname "${SCRIPT_DIR}")/urdf/pepper_robot.urdf"


# Arguments for xacro
XACRO_ARGS=(
    name:=pepper_robot
    prefix:=
    gripper:=true
    collision_arm:=true
    collision_gripper:=true
    ros2_control:=true
    ros2_control_plugin:=ign
    ros2_control_command_interface:=effort
    gazebo_preserve_fixed_joint:=false
    gazebo_self_collide:=false
    gazebo_self_collide_fingers:=true
    gazebo_joint_trajectory_controller:=false
    gazebo_joint_state_publisher:=false
    gazebo_pose_publisher:=true
)

# Remove old URDF file
rm "${URDF_PATH}" 2>/dev/null

# Process xacro into URDF
xacro "${XACRO_PATH}" "${XACRO_ARGS[@]}" -o "${URDF_PATH}" &&
echo "Created new ${URDF_PATH}"
