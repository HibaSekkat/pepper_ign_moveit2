#!/usr/bin/env bash
# This script converts xacro (URDF variant) into SDF for `pepper_robot_description` package

SCRIPT_DIR="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")" &>/dev/null && pwd)"
XACRO_PATH="$(dirname "${SCRIPT_DIR}")/urdf/pepper_robot.urdf.xacro"
SDF_PATH="$(dirname "${SCRIPT_DIR}")/pepper_robot/model.sdf"

# Arguments for xacro
XACRO_ARGS=(
    name:=pepper_robot
    ros2_control:=true
    ros2_control_plugin:=fake
    ros2_control_command_interface:=position
)

# Remove old SDF file
rm "${SDF_PATH}" 2>/dev/null

# Process xacro into URDF, then convert URDF to SDF and edit the SDF to use relative paths for meshes
"${SCRIPT_DIR}/xacro2sdf_direct.bash" "${XACRO_PATH}" "${XACRO_ARGS[@]}" "${@:1}" >"${SDF_PATH}" &&
echo "Created new ${SDF_PATH}"
