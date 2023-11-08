#!/usr/bin/env bash
# This script converts xacro (URDF variant) into SDF for `pepper_robot_description` package

SCRIPT_DIR="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")" &>/dev/null && pwd)"
XACRO_PATH="$(dirname "${SCRIPT_DIR}")/urdf/pepper_robot.xacro"
SDF_PATH="$(dirname "${SCRIPT_DIR}")/pepper_robot/model.sdf"
TMP_URDF_PATH="/tmp/pepper_robot_tmp.urdf"

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

# Remove old SDF file
rm "${SDF_PATH}" 2>/dev/null

# Process xacro into URDF, then convert URDF to SDF and edit the SDF to use relative paths for meshes
xacro "${XACRO_PATH}" "${XACRO_ARGS[@]}" -o "${TMP_URDF_PATH}" &&
ign sdf -p "${TMP_URDF_PATH}" | sed 's/model:\/\/pepper_robot_description\///g' | sed 's/package:\/\/pepper_robot_description\///g' >"${SDF_PATH}" &&
echo "Created new ${SDF_PATH}"

# Remove temporary URDF file
rm "${TMP_URDF_PATH}" 2>/dev/null
