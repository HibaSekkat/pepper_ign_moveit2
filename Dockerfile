ARG ROS_DISTRO=galactic
FROM ros:${ROS_DISTRO}-ros-base

### Use bash by default
SHELL ["/bin/bash", "-c"]

### Define working directory
ARG WS_DIR=/root/ws
ENV WS_DIR=${WS_DIR}
ENV WS_SRC_DIR=${WS_DIR}/src
ENV WS_INSTALL_DIR=${WS_DIR}/install
ENV WS_LOG_DIR=${WS_DIR}/log
WORKDIR ${WS_DIR}

### Install pip & trimesh (for collision geometry)
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
    python3-pip && \
    rm -rf /var/lib/apt/lists/* && \
    python3 -m pip install --no-cache-dir trimesh==3.23.5

### Install Gazebo
ARG IGNITION_VERSION=fortress
ENV IGNITION_VERSION=${IGNITION_VERSION}
RUN apt-get update && \
    apt-get install -yq --no-install-recommends \
    gz-${IGNITION_VERSION} && \
    rm -rf /var/lib/apt/lists/*

### Import required repositories, then install their dependencies and build
COPY ./pepper_robot.repos ${WS_SRC_DIR}/pepper_robot/pepper_robot.repos
RUN vcs import --shallow ${WS_SRC_DIR} < ${WS_SRC_DIR}/pepper_robot/pepper_robot.repos && \
    rosdep update --rosdistro="${ROS_DISTRO}" && \
    apt-get update && \
    rosdep install -y -r -i --rosdistro "${ROS_DISTRO}" --from-paths ${WS_SRC_DIR} && \
    rm -rf /var/lib/apt/lists/* && \
    source "/opt/ros/${ROS_DISTRO}/setup.bash" && \
    colcon build --merge-install --symlink-install --cmake-args "-DCMAKE_BUILD_TYPE=Release" && \
    rm -rf ${WS_LOG_DIR}

### Copy over all `package.xml` manifests, then install dependencies
COPY ./pepper_robot/package.xml ${WS_SRC_DIR}/pepper_robot/pepper_robot/package.xml
COPY ./pepper_robot_ign/package.xml ${WS_SRC_DIR}/pepper_robot/pepper_robot_ign/package.xml
COPY ./pepper_robot_description/package.xml ${WS_SRC_DIR}/pepper_robot/pepper_robot_description/package.xml
COPY ./pepper_robot_moveit_config/package.xml ${WS_SRC_DIR}/pepper_robot/pepper_robot_moveit_config/package.xml
RUN rosdep update --rosdistro="${ROS_DISTRO}" && \
    apt-get update && \
    rosdep install -y -r -i --rosdistro "${ROS_DISTRO}" --from-paths ${WS_SRC_DIR} && \
    rm -rf /var/lib/apt/lists/*

### Copy over the rest of pepper_robot, then build
COPY ./ ${WS_SRC_DIR}/pepper_robot/
RUN source "/opt/ros/${ROS_DISTRO}/setup.bash" && \
    colcon build --merge-install --symlink-install --cmake-args "-DCMAKE_BUILD_TYPE=Release" && \
    rm -rf ${WS_LOG_DIR}

### Add workspace to the ROS entrypoint
RUN sed -i '$i source "${WS_INSTALL_DIR}/local_setup.bash" --' /ros_entrypoint.sh && \
    ### Disable `set -e` from the ROS entrypoint
    sed -i '$i set +e' /ros_entrypoint.sh && \
    ### Source the ROS entrypoint inside `~/.bashrc` to enable autocompletion
    sed -i '$a source /ros_entrypoint.sh' ~/.bashrc
