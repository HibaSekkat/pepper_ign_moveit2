# pepper_robot_ign

Gazebo configuration of pepper_robot.

## Instructions

### bridge

Communication between ROS 2 and Gazebo can be facilitated by utilising [ros_gz](https://github.com/gazebosim/ros_gz/tree/ros2) bridge. In order to do so, a configurable [bridge.launch.py](./launch/bridge.launch.py) script is included to simplify the process for `pepper_robot`. It can be launched separately or included in another launch script while passing the desired arguments.

```bash
ros2 launch pepper_robotign bridge.launch.py <arg_i>:=<val_i>
```

To see all arguments, please use `ros2 launch --show-args pepper_robot_ign bridge.launch.py`.

## Examples

### ex_follow_target

To see if everything is functioning properly, try using [ex_folow_target.launch.py](./launch/ex_folow_target.launch.py) script. It launches Gazebo, move_group of MoveIt 2 and ROS 2 \<–> IGN bridges that enable robot to follow a target. Simply start the simulation and move the target object around with Transform Control tool.

```bash
ros2 launch pepper_robot_ign ex_folow_target.launch.py
```

In order to verify control of the move base, try running `teleop_twist_keyboard`.

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args --remap /cmd_vel:=/pepper_robot/cmd_vel
```

## Directory Structure

The following directory structure is utilised for this package.

```bash
.
├── examples/                                # [dir] Examples
├── launch/                                  # [dir] ROS 2 launch scripts
    ├── examples/                            # [dir] Launch scripts for examples
    └── bridge.launch.py                     # Configurable launch script for bridging communication between ROS 2 and
├── rviz/ign_moveit.rviz                     # Generic RViz2 config that includes tf2 visualisation and MoveIt 2 planning
├── worlds/moveit_follow_target.sdf          # SDF of world used for ex_follow_target example
├── CMakeLists.txt                           # Colcon-enabled CMake recipe
└── package.xml                              # ROS 2 package metadata
```
