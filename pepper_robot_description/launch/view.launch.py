#!/usr/bin/env -S ros2 launch
"""Visualisation of URDF model for pepper_robot in RViz2"""

from os import path
from typing import List

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import (
    Command,
    FindExecutable,
    LaunchConfiguration,
    PathJoinSubstitution,
)
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch_ros.descriptions import ParameterValue
def generate_launch_description() -> LaunchDescription:

    # Declare all launch arguments
    declared_arguments = generate_declared_arguments()

    # Get substitution for all arguments
    rviz_config = LaunchConfiguration("rviz_config")
    use_sim_time = LaunchConfiguration("use_sim_time")
    log_level = LaunchConfiguration("log_level")

    # Extract URDF from description file
    urdf_file_path = "/root/ws/src/pepper_ign_moveit2/pepper_robot_description/urdf/pepper_robot.urdf"

    with open(urdf_file_path, "r") as urdf_file:
        urdf_content = urdf_file.read()

    robot_description = {"robot_description": urdf_content}

    # List of nodes to be launched
    nodes = [
        # robot_state_publisher
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            output="log",
            arguments=["--ros-args", "--log-level", log_level],
            parameters=[robot_description, {"use_sim_time": use_sim_time}],
        ),
        # rviz2
        Node(
            package="rviz2",
            executable="rviz2",
            output="log",
            arguments=[
                "--display-config",
                rviz_config,
                "--ros-args",
                "--log-level",
                log_level,
            ],
            #parameters=[{"use_sim_time": use_sim_time}],
        ),
        # joint_state_publisher_gui
        Node(
            package="joint_state_publisher_gui",
            executable="joint_state_publisher_gui",
            output="log",
            arguments=["--ros-args", "--log-level", log_level],
            parameters=[{"use_sim_time": use_sim_time}],
        ),
    ]

    return LaunchDescription(declared_arguments + nodes)


def generate_declared_arguments() -> List[DeclareLaunchArgument]:
    """
    Generate list of all launch arguments that are declared for this launch script.
    """

    return [
        # Location of xacro/URDF to visualise
        DeclareLaunchArgument(
            "description_package",
            default_value="pepper_robot_description",
            description="Custom package with robot description.",
        ),
        DeclareLaunchArgument(
            "description_filepath",
            default_value=path.join("urdf", "pepper_robot.urdf"),
            description="Path to xacro or URDF description of the robot, relative to share of `description_package`.",
        ),
        # Naming of the robot
        DeclareLaunchArgument(
            "name",
            default_value="pepper_robot",
            description="Name of the robot.",
        ),
        DeclareLaunchArgument(
            "prefix",
            default_value="",
            description="Prefix for all robot entities. If modified, then joint names in the configuration of controllers must also be updated.",
        ),
        #gripper
         DeclareLaunchArgument(
            "gripper",
            default_value="true",
            description="Flag to enable default gripper.",
        ),
        # Safety controller
        DeclareLaunchArgument(
            "safety_limits",
            default_value="true",
            description="Flag to enable safety limits controllers on manipulator joints.",
        ),
        DeclareLaunchArgument(
            "safety_position_margin",
            default_value="0.15",
            description="Lower and upper margin for position limits of all safety controllers.",
        ),
        DeclareLaunchArgument(
            "safety_k_position",
            default_value="20",
            description="Parametric k-position factor of all safety controllers.",
        ),
        # Collision geometry
        DeclareLaunchArgument(
            "collision_wheels",
            default_value="true",
            description="Flag to enable collision geometry for the wheels of Summit XL.",
        ),
        DeclareLaunchArgument(
            "collision_arm",
            default_value="true",
            description="Flag to enable collision geometry for manipulator's arm.",
        ),
        DeclareLaunchArgument(
            "collision_gripper",
            default_value="true",
            description="Flag to enable collision geometry for manipulator's gripper (hand and fingers).",
        ),
         # Geometry
        DeclareLaunchArgument(
            "high_quality_mesh",
            default_value="true",
            description="Flag to select the high or low quality model.",
        ),
        # Gripper
        DeclareLaunchArgument(
            "mimic_gripper_joints",
            default_value="false",
            description="Flag to mimic joints of the gripper.",
        ),
        # ROS 2 control
        DeclareLaunchArgument(
            "ros2_control",
            default_value="true",
            description="Flag to enable ros2 controllers for manipulator.",
        ),
        DeclareLaunchArgument(
            "ros2_control_plugin",
            default_value="ign",
            description="The ros2_control plugin that should be loaded for the manipulator ('fake', 'ign', 'real' or custom).",
        ),
        DeclareLaunchArgument(
            "ros2_control_command_interface",
            default_value="effort",
            description="The output control command interface provided by ros2_control ('position', 'velocity' or 'effort').",
        ),
        # Gazebo
        DeclareLaunchArgument(
            "gazebo_preserve_fixed_joint",
            default_value="false",
            description="Flag to preserve fixed joints and prevent lumping when generating SDF for Gazebo.",
        ),
        DeclareLaunchArgument(
            "gazebo_self_collide",
            default_value="false",
            description="Flag to enable self-collision of all robot links when generating SDF for Gazebo.",
        ),
        DeclareLaunchArgument(
            "gazebo_self_collide_fingers",
            default_value="true",
            description="Flag to enable self-collision of robot between fingers (finger tips) when generating SDF for Gazebo.",
        ),
        DeclareLaunchArgument(
            "gazebo_joint_trajectory_controller",
            default_value="false",
            description="Flag to enable JointTrajectoryController Gazebo plugin for manipulator.",
        ),
        DeclareLaunchArgument(
            "gazebo_joint_state_publisher",
            default_value="false",
            description="Flag to enable JointStatePublisher Gazebo plugin for all joints.",
        ),
        DeclareLaunchArgument(
            "gazebo_pose_publisher",
            default_value="true",
            description="Flag to enable PosePublisher Gazebo plugin for true pose of robot.",
        ),
        # Miscellaneous
        DeclareLaunchArgument(
            "rviz_config",
            default_value=path.join(
                get_package_share_directory("pepper_robot_description"),
                "rviz",
                "view.rviz",
            ),
            description="Path to configuration for RViz2.",
        ),
        DeclareLaunchArgument(
            "use_sim_time",
            default_value="false",
            description="If true, use simulated clock.",
        ),
        DeclareLaunchArgument(
            "log_level",
            default_value="warn",
            description="The level of logging that is applied to all ROS 2 nodes launched by this script.",
        ),
    ]
