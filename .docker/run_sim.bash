#!/usr/bin/env bash

## Configuration
# Flags for running the container
DOCKER_RUN_OPTS="${DOCKER_RUN_OPTS:-
    --detach
    --rm
    --network host
    --ipc host
}"
# Name of the container (force name to prevent unique suffix)
CONTAINER_NAME="${CONTAINER_NAME:-"pepper_ign_moveit2"}"
# Command to run inside the detached container
CONTAINER_CMD="${CONTAINER_CMD:-"ros2 launch pepper_ign_moveit2 gz.launch.py"}"

## If the current user is not in the docker group, all docker commands will be run as root
WITH_SUDO=""
if ! grep -qi /etc/group -e "docker.*${USER}"; then
    echo "INFO: The current user ${USER} is not detected in the docker group. All docker commands will be run as root."
    WITH_SUDO="sudo"
fi

## Get path to the compose file
SCRIPT_DIR="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")" &>/dev/null && pwd)"

## Run the container with simulation
CONTAINER_NAME="${CONTAINER_NAME}" DOCKER_RUN_OPTS="${DOCKER_RUN_OPTS}" "${SCRIPT_DIR}/run.bash" "${CONTAINER_CMD}"
IS_SUCCESS=$?

if [ "${IS_SUCCESS}" -eq 0 ]; then
    ## If susccessful, join the container
    "${SCRIPT_DIR}/join.bash"

    ## Once done with the interactive session, kill the container to clean up
    # shellcheck disable=SC2206
    DOCKER_KILL_CMD=(
        ${WITH_SUDO} docker kill "${CONTAINER_NAME}"
    )
    echo -e "\033[1;90m${DOCKER_KILL_CMD[*]}\033[0m" | xargs
    # shellcheck disable=SC2048
    ${DOCKER_KILL_CMD[*]}
fi
