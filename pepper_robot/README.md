# pepper_robot

Metapackage for pepper_robot.

## Functionality

During the build stage, this package converts xacros of [pepper_robot_description](../pepper_robot_description) and [pepper_robot_moveit_config](../pepper_robot_moveit_config) into auto-generated URDF, SDF and SRDF descriptions for convenience.

## Directory Structure

The following directory structure is utilised for this package.

```bash
.
├── CMakeLists.txt # Colcon-enabled CMake recipe
└── package.xml    # ROS 2 package metadata
```
