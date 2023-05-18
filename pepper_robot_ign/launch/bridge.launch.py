#!/usr/bin/env -S ros2 launch
"""Launch various bridges between Ignition Transport and ROS 2"""

from typing import List

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, TextSubstitution
from launch_ros.actions import Node

DIR_BOTH = "@"
DIR_IGN_TO_ROS2 = "["
DIR_ROS2_TO_IGN = "]"

# Directory of all supported bridges with their indicated message types and direction
bridges = {
    "clock": ("rosgraph_msgs/msg/Clock" + DIR_IGN_TO_ROS2 + "ignition.msgs.Clock"),
    "joint_state": (
        "sensor_msgs/msg/JointState" + DIR_IGN_TO_ROS2 + "ignition.msgs.Model"
    ),
    "joint_trajectory": (
        "trajectory_msgs/msg/JointTrajectory"
        + DIR_ROS2_TO_IGN
        + "ignition.msgs.JointTrajectory"
    ),
    "joint_trajectory_progress": (
        "std_msgs/msg/Float32" + DIR_IGN_TO_ROS2 + "ignition.msgs.Float"
    ),
    "true_base_tf": (
        "tf2_msgs/msg/TFMessage" + DIR_IGN_TO_ROS2 + "ignition.msgs.Pose_V"
    ),
    "odom": ("nav_msgs/msg/Odometry" + DIR_IGN_TO_ROS2 + "ignition.msgs.Odometry"),
    "odom_tf": ("tf2_msgs/msg/TFMessage" + DIR_IGN_TO_ROS2 + "ignition.msgs.Pose_V"),
    "cmd_vel": ("geometry_msgs/msg/Twist" + DIR_ROS2_TO_IGN + "ignition.msgs.Twist"),
}


def generate_launch_description():

    # Declare all launch arguments
    declared_arguments = generate_declared_arguments()

    # Get substitution for all arguments
    robot_name = LaunchConfiguration("robot_name")
    prefix = LaunchConfiguration("prefix")
    enabled_bridges = {
        "clock": LaunchConfiguration("bridge_clock"),
        "joint_state": LaunchConfiguration("bridge_joint_state"),
        "joint_trajectory": LaunchConfiguration("bridge_joint_trajectory"),
        "joint_trajectory_progress": LaunchConfiguration(
            "bridge_joint_trajectory_progress"
        ),
        "true_base_tf": LaunchConfiguration("bridge_true_base_tf"),
        "odom": LaunchConfiguration("bridge_odom"),
        "odom_tf": LaunchConfiguration("bridge_odom_tf"),
        "cmd_vel": LaunchConfiguration("bridge_cmd_vel"),
    }
    ign_topic = {
        "clock": LaunchConfiguration("ign_clock"),
        "joint_state": LaunchConfiguration("ign_joint_state"),
        "joint_trajectory": LaunchConfiguration("ign_joint_trajectory"),
        "joint_trajectory_progress": LaunchConfiguration(
            "ign_joint_trajectory_progress"
        ),
        "true_base_tf": LaunchConfiguration("ign_true_base_tf"),
        "odom": LaunchConfiguration("ign_odom"),
        "odom_tf": LaunchConfiguration("ign_odom_tf"),
        "cmd_vel": LaunchConfiguration("ign_cmd_vel"),
    }
    ros_topic = {
        "clock": LaunchConfiguration("ros_clock"),
        "joint_state": LaunchConfiguration("ros_joint_state"),
        "joint_trajectory": LaunchConfiguration("ros_joint_trajectory"),
        "joint_trajectory_progress": LaunchConfiguration(
            "ros_joint_trajectory_progress"
        ),
        "true_base_tf": LaunchConfiguration("ros_true_base_tf"),
        "odom": LaunchConfiguration("ros_odom"),
        "odom_tf": LaunchConfiguration("ros_odom_tf"),
        "cmd_vel": LaunchConfiguration("ros_cmd_vel"),
    }
    use_sim_time = LaunchConfiguration("use_sim_time")
    log_level = LaunchConfiguration("log_level")

    # List of nodes to be launched
    nodes = [
        # Static tf remapping for true_base_tf
        Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            output="log",
            arguments=[
                # "--x",
                "0",
                # "--y",
                "0",
                # "--z",
                "0",
                # "--yaw",
                "0",
                # "--pitch",
                "0",
                # "--roll",
                "0",
                # "--frame-id",
                robot_name,
                # "--child-frame-id",
                "--ros-args",
                "--log-level",
                log_level,
            ],
            parameters=[{"use_sim_time": use_sim_time}],
            condition=IfCondition(enabled_bridges["true_base_tf"]),
        ),
        # Static tf remapping for odom_tf
        Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            output="log",
            arguments=[
                # "--x",
                "0",
                # "--y",
                "0",
                # "--z",
                "0",
                # "--yaw",
                "0",
                # "--pitch",
                "0",
                # "--roll",
                "0",
                "--frame-id",
                LaunchConfiguration('robot_name') + "/",
                # "--child-frame-id",
                LaunchConfiguration('prefix') + "pepper_robot_base_footprint",
                "--ros-args",
                "--log-level",
                log_level,
            ],
            parameters=[{"use_sim_time": use_sim_time}],
            condition=IfCondition(enabled_bridges["odom_tf"]),
        ),
    ]

    # List for logging
    logs = []

    # Add node for every enabled bridge
    # TODO: Use a single node for all topics (requires more complex conditioning)
    for bridge, bridge_type in bridges.items():
        nodes.append(
            Node(
                package="ros_ign_bridge",
                executable="parameter_bridge",
                output="log",
                arguments=[
                    [ign_topic[bridge], TextSubstitution(text="@"), bridge_type],
                    "--ros-args",
                    "--log-level",
                    log_level,
                ],
                parameters=[{"use_sim_time": use_sim_time}],
                remappings=[(ign_topic[bridge], ros_topic[bridge])],
                condition=IfCondition(enabled_bridges[bridge]),
            ),
        )
        logs.append(
            LogInfo(
                msg=[
                    "Bridge enabled between [ROS 2] ",
                    ros_topic[bridge],
                    " and [IGN] ",
                    ign_topic[bridge],
                ],
                condition=IfCondition(enabled_bridges[bridge]),
            )
        )

    return LaunchDescription(declared_arguments + nodes + logs)


def generate_declared_arguments() -> List[DeclareLaunchArgument]:
    """
    Generate list of all launch arguments that are declared for this launch script.
    """

    return [
        # Naming of the world and robot
        DeclareLaunchArgument(
            "world_name",
            default_value="default",
            description="Name of the Ignition Gazebo world, which affects some of the Ignition topic names.",
        ),
        DeclareLaunchArgument(
            "robot_name",
            default_value="pepper_robot",
            description="Name of the robot, which affects most of the Ignition topic names.",
        ),
        DeclareLaunchArgument(
            "prefix",
            default_value="robot_",
            description="Prefix for all robot entities. If modified, then joint names in the configuration of controllers must also be updated.",
        ),
        # Bridge enablers
        DeclareLaunchArgument(
            "bridge_clock",
            default_value="true",
            description="Flag to enable bridging of `clock` (IGN -> ROS 2).",
        ),
        DeclareLaunchArgument(
            "bridge_joint_state",
            default_value="false",
            description="Flag to enable bridging of `joint_state` (IGN -> ROS 2).",
        ),
        DeclareLaunchArgument(
            "bridge_joint_trajectory",
            default_value="false",
            description="Flag to enable bridging of `joint_trajectory` (ROS 2 -> IGN).",
        ),
        DeclareLaunchArgument(
            "bridge_joint_trajectory_progress",
            default_value="false",
            description="Flag to enable bridging of `joint_trajectory_progress` (IGN -> ROS 2).",
        ),
        DeclareLaunchArgument(
            "bridge_true_base_tf",
            default_value="true",
            description="Flag to enable bridging of `true_base_tf` (IGN -> ROS 2).",
        ),
        DeclareLaunchArgument(
            "bridge_odom",
            default_value="false",
            description="Flag to enable bridging of `odom` (IGN -> ROS 2).",
        ),
        DeclareLaunchArgument(
            "bridge_odom_tf",
            default_value="false",
            description="Flag to enable bridging of `odom_tf` (IGN -> ROS 2).",
        ),
        DeclareLaunchArgument(
            "bridge_cmd_vel",
            default_value="true",
            description="Flag to enable bridging of `cmd_vel` (ROS 2 -> IGN).",
        ),
        # Source topic names
        DeclareLaunchArgument(
            "ign_clock",
            default_value=["/world/", LaunchConfiguration("world_name"), "/clock"],
            description="Ignition topic for `clock`.",
        ),
        DeclareLaunchArgument(
            "ign_joint_state",
            default_value=[
                "/world/",
                LaunchConfiguration("world_name"),
                "/model/",
                LaunchConfiguration("robot_name"),
                "/joint_state",
            ],
            description="Ignition topic for `joint_state`.",
        ),
        DeclareLaunchArgument(
            "ign_joint_trajectory",
            default_value=[
                "/model/",
                LaunchConfiguration("robot_name"),
                "/joint_trajectory",
            ],
            description="Ignition topic for `joint_trajectory`.",
        ),
        DeclareLaunchArgument(
            "ign_joint_trajectory_progress",
            default_value=[
                "/model/",
                LaunchConfiguration("robot_name"),
                "/joint_trajectory_progress",
            ],
            description="Ignition topic for `joint_trajectory_progress`.",
        ),
        DeclareLaunchArgument(
            "ign_true_base_tf",
            default_value=["/model/", LaunchConfiguration("robot_name"), "/pose"],
            description="Ignition topic for `true_base_tf`.",
        ),
        DeclareLaunchArgument(
            "ign_odom",
            default_value=["/model/", LaunchConfiguration("robot_name"), "/odom"],
            description="Ignition topic for `odom`.",
        ),
        DeclareLaunchArgument(
            "ign_odom_tf",
            default_value=["/model/", LaunchConfiguration("robot_name"), "/tf"],
            description="Ignition topic for `odom_tf`.",
        ),
        DeclareLaunchArgument(
            "ign_cmd_vel",
            default_value=["/model/", LaunchConfiguration("robot_name"), "/cmd_vel"],
            description="Ignition topic for `cmd_vel`.",
        ),
        # ROS topic names
        DeclareLaunchArgument(
            "ros_clock", default_value="/clock", description="ROS 2 topic for `clock`."
        ),
        DeclareLaunchArgument(
            "ros_joint_state",
            default_value=["/", LaunchConfiguration("robot_name"), "/joint_states"],
            description="ROS 2 topic for `joint_states`.",
        ),
        DeclareLaunchArgument(
            "ros_joint_trajectory",
            default_value=["/", LaunchConfiguration("robot_name"), "/joint_trajectory"],
            description="ROS 2 topic for `joint_trajectory`.",
        ),
        DeclareLaunchArgument(
            "ros_joint_trajectory_progress",
            default_value=[
                "/",
                LaunchConfiguration("robot_name"),
                "/joint_trajectory_progress",
            ],
            description="ROS 2 topic for `joint_trajectory_progress`.",
        ),
        DeclareLaunchArgument(
            "ros_true_base_tf",
            default_value="/tf",
            description="ROS 2 topic for `true_base_tf`.",
        ),
        DeclareLaunchArgument(
            "ros_odom",
            default_value=["/", LaunchConfiguration("robot_name"), "/odom"],
            description="ROS 2 topic for `odom`.",
        ),
        DeclareLaunchArgument(
            "ros_odom_tf", default_value="/tf", description="ROS 2 topic for `odom_tf`."
        ),
        DeclareLaunchArgument(
            "ros_cmd_vel",
            default_value=["/", LaunchConfiguration("robot_name"), "/cmd_vel"],
            description="ROS 2 topic for `cmd_vel`.",
        ),
        # Miscellaneous
        DeclareLaunchArgument(
            "use_sim_time",
            default_value="true",
            description="If true, use simulated clock.",
        ),
        DeclareLaunchArgument(
            "log_level",
            default_value="warn",
            description="The level of logging that is applied to all ROS 2 nodes launched by this script.",
        ),
    ]
