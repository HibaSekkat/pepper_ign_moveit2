#!/usr/bin/env bash
# This script converts xacro (URDF variant) into URDF for `pepper_robot_description` package

SCRIPT_DIR="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")" &>/dev/null && pwd)"
XACRO_PATH="$(dirname "${SCRIPT_DIR}")/urdf/pepper_robot.urdf.xacro"
URDF_PATH="$(dirname "${SCRIPT_DIR}")/urdf/pepper_robot.urdf"

# Arguments for xacro
XACRO_ARGS=(
    name:=pepper_robot
    ros2_control:=true
    ros2_control_plugin:=fake
    ros2_control_command_interface:=position
)

# Remove old URDF file
rm "${URDF_PATH}" 2>/dev/null

# Process xacro into URDF
xacro "${XACRO_PATH}" "${XACRO_ARGS[@]}" "${@:1}" -o "${URDF_PATH}" &&
echo "Created new ${URDF_PATH}"
