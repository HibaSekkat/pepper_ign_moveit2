#!/usr/bin/env bash
# This script converts xacro (SRDF variant) into SRDF for `pepper_robot_description` package

SCRIPT_DIR="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")" &>/dev/null && pwd)"
XACRO_PATH="$(dirname "${SCRIPT_DIR}")/srdf/pepper_robot.srdf.xacro"
SRDF_PATH="$(dirname "${SCRIPT_DIR}")/srdf/pepper_robot.srdf"

# Arguments for xacro
XACRO_ARGS=(
    name:=pepper_robot
  
)

# Remove old SRDF file
rm "${SRDF_PATH}" 2>/dev/null

# Process xacro into SRDF
xacro "${XACRO_PATH}" "${XACRO_ARGS[@]}" -o "${SRDF_PATH}" &&
echo "Created new ${SRDF_PATH}"
