#!/usr/bin/env bash
# This script converts URDF into SRDF for `pepper_robot_description` package

SCRIPT_DIR="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")" &>/dev/null && pwd)"
URDF_PATH="$(dirname "${SCRIPT_DIR}")/urdf/pepper_robot.urdf"
SRDF_PATH="$(dirname "${SCRIPT_DIR}")/srdf/pepper_robot.srdf"

# Remove old SRDF file
rm "${SRDF_PATH}" 2>/dev/null

# Process URDF into SRDF
rosrun srdfdom urdf_to_srdf "${URDF_PATH}" "${SRDF_PATH}"

echo "Created new ${SRDF_PATH}"
