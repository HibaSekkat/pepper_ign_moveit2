#!/usr/bin/env -S ros2 launch
"""Configure and setup move group for planning with MoveIt 2"""

from os import path
from typing import List

import yaml
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import (
    Command,
    FindExecutable,
    LaunchConfiguration,
    PathJoinSubstitution,
    PythonExpression,
)
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    # Declare all launch arguments
    declared_arguments = generate_declared_arguments()

    # Get substitution for all arguments
    moveit_config_package = "pepper_robot_moveit_config"
    name = LaunchConfiguration("name")
    prefix = LaunchConfiguration("prefix")
    gripper = LaunchConfiguration("gripper")
    safety_limits = LaunchConfiguration("safety_limits")
    safety_position_margin = LaunchConfiguration("safety_position_margin")
    safety_k_position = LaunchConfiguration("safety_k_position")
    collision_chassis = LaunchConfiguration("collision_chassis")
    collision_wheels = LaunchConfiguration("collision_wheels")
    collision_left_arm = LaunchConfiguration("collision_left_arm")
    collision_gripper = LaunchConfiguration("collision_gripper")
    high_quality_mesh = LaunchConfiguration("high_quality_mesh")
    publish_state = LaunchConfiguration("publish_state")
    execute_trajectories = LaunchConfiguration("execute_trajectories")
    mimic_gripper_joints = LaunchConfiguration("mimic_gripper_joints")
    ros2_control = LaunchConfiguration("ros2_control")
    ros2_control_plugin = LaunchConfiguration("ros2_control_plugin")
    ros2_control_command_interface = LaunchConfiguration(
        "ros2_control_command_interface"
    )
    servo = LaunchConfiguration("servo")
    gazebo_preserve_fixed_joint = LaunchConfiguration("gazebo_preserve_fixed_joint")
    gazebo_self_collide = LaunchConfiguration("gazebo_self_collide")
    gazebo_self_collide_fingers = LaunchConfiguration("gazebo_self_collide_fingers")
    gazebo_diff_drive = LaunchConfiguration("gazebo_diff_drive")
    gazebo_joint_trajectory_controller = LaunchConfiguration(
        "gazebo_joint_trajectory_controller"
    )
    gazebo_joint_state_publisher = LaunchConfiguration("gazebo_joint_state_publisher")
    gazebo_pose_publisher = LaunchConfiguration("gazebo_pose_publisher")
    enable_rviz = LaunchConfiguration("enable_rviz")
    rviz_config = LaunchConfiguration("rviz_config")
    use_sim_time = LaunchConfiguration("use_sim_time")
    log_level = LaunchConfiguration("log_level")

    # URDF
    urdf_file_path = "/root/ws/src/pepper_ign_moveit2/pepper_robot_description/urdf/pepper_robot.urdf"

    xacro_cmd = [
        PathJoinSubstitution([FindExecutable(name="xacro")]),
        " ",
        urdf_file_path,
        " ",
        "name:=",
        name,
        " ",
        "prefix:=",
        prefix,
        " ",
        "gripper:=",
        gripper,
        " ",
        "safety_limits:=",
        safety_limits,
        " ",
        "safety_position_margin:=",
        safety_position_margin,
        " ",
        "safety_k_position:=",
        safety_k_position,
        " ",
        "collision_chassis:=",
        collision_chassis,
        " ",
        "collision_wheels:=",
        collision_wheels,
        " ",
        "collision_left_arm:=",
        collision_left_arm,
        " ",
        "collision_gripper:=",
        collision_gripper,
        " ",
        "high_quality_mesh:=",
        high_quality_mesh,
        " ",
        "mimic_gripper_joints:=",
        mimic_gripper_joints,
        " ",
        "ros2_control:=",
        ros2_control,
        " ",
        "ros2_control_plugin:=",
        ros2_control_plugin,
        " ",
        "ros2_control_command_interface:=",
        ros2_control_command_interface,
        " ",
        "gazebo_preserve_fixed_joint:=",
        gazebo_preserve_fixed_joint,
        " ",
        "gazebo_self_collide:=",
        gazebo_self_collide,
        " ",
        "gazebo_self_collide_fingers:=",
        gazebo_self_collide_fingers,
        " ",
        "gazebo_diff_drive:=",
        gazebo_diff_drive,
        " ",
        "gazebo_joint_trajectory_controller:=",
        gazebo_joint_trajectory_controller,
        " ",
        "gazebo_joint_state_publisher:=",
        gazebo_joint_state_publisher,
        " ",
        "gazebo_pose_publisher:=",
        gazebo_pose_publisher,
    ]

    _robot_description_xml = Command(xacro_cmd)
    robot_description = {"robot_description": _robot_description_xml}

    # SRDF
    srdf_file_path = "/root/ws/src/pepper_ign_moveit2/pepper_robot_moveit_config/srdf/pepper_robot.srdf"
    with open(srdf_file_path, "r") as file:
        srdf_content = file.read()

    _robot_description_semantic_xml = {"value": srdf_content}
    robot_description_semantic = {"robot_description_semantic": _robot_description_semantic_xml}

    # Kinematics
    kinematics = load_yaml(
        moveit_config_package, path.join("config", "kinematics.yaml")
    )

    # Joint limits
    joint_limits = {
        "robot_description_planning": load_yaml(
            moveit_config_package, path.join("config", "joint_limits.yaml")
        )
    }

    # Servo
    servo_params = {
        "moveit_servo": load_yaml(
            moveit_config_package, path.join("config", "servo.yaml")
        )
    }
    servo_params["moveit_servo"].update({"use_gazebo": use_sim_time})

    # Planning pipeline
    planning_pipeline = {
        "planning_pipelines": ["ompl"],
        "default_planning_pipeline": "ompl",
        "ompl": {
            "planning_plugin": "ompl_interface/OMPLPlanner",
            # TODO: Re-enable `default_planner_request_adapters/AddRuckigTrajectorySmoothing` once its issues are resolved
            "request_adapters": "default_planner_request_adapters/AddTimeOptimalParameterization default_planner_request_adapters/ResolveConstraintFrames default_planner_request_adapters/FixWorkspaceBounds default_planner_request_adapters/FixStartStateBounds default_planner_request_adapters/FixStartStateCollision default_planner_request_adapters/FixStartStatePathConstraints",
            # TODO: Reduce start_state_max_bounds_error once spawning with specific joint configuration is enabled
            "start_state_max_bounds_error": 1.5707963,
        },
    }
    _ompl_yaml = load_yaml(
        moveit_config_package, path.join("config", "ompl_planning.yaml")
    )
    planning_pipeline["ompl"].update(_ompl_yaml)

    # Planning scene
    planning_scene_monitor_parameters = {
        "publish_planning_scene": True,
        "publish_geometry_updates": True,
        "publish_state_updates": True,
        "publish_transforms_updates": True,
    }

    # MoveIt controller manager
    moveit_controller_manager_yaml = load_yaml(
        moveit_config_package, path.join("config", "moveit_controller_manager.yaml")
    )
    moveit_controller_manager = {
        "moveit_controller_manager": "moveit_simple_controller_manager/MoveItSimpleControllerManager",
        "moveit_simple_controller_manager": moveit_controller_manager_yaml,
    }

    # Trajectory execution
    trajectory_execution = {
        "allow_trajectory_execution": execute_trajectories,
        "moveit_manage_controllers": False,
        "trajectory_execution.allowed_execution_duration_scaling": 1.2,
        "trajectory_execution.allowed_goal_duration_margin": 0.5,
        "trajectory_execution.allowed_start_tolerance": 0.1,
    }

    # Controller parameters
    declared_arguments.append(
        DeclareLaunchArgument(
            "__controller_parameters__basename",
            default_value=["controllers_", ros2_control_command_interface, ".yaml"],
        )
    )
    controller_parameters = PathJoinSubstitution(
        [
            FindPackageShare(moveit_config_package),
            "config",
            LaunchConfiguration("__controller_parameters__basename"),
        ]
    )

    # List of nodes to be launched
    nodes = [
        # robot_state_publisher
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            output="log",
            arguments=["--ros-args", "--log-level", log_level],
            parameters=[
                robot_description,
                {
                    "publish_frequency": 50.0,
                    "frame_prefix": "",
                    "use_sim_time": use_sim_time,
                },
            ],
            condition=IfCondition(publish_state),
        ),
        # ros2_control_node (only for fake controller)
        Node(
            package="controller_manager",
            executable="ros2_control_node",
            output="log",
            arguments=["--ros-args", "--log-level", log_level],
            parameters=[
                robot_description,
                controller_parameters,
                {"use_sim_time": use_sim_time},
            ],
            condition=(
                IfCondition(
                    PythonExpression(
                        [
                            "'",
                            ros2_control_plugin,
                            "'",
                            " == ",
                            "'fake'",
                            " and ",
                            "'",
                            execute_trajectories,
                            "'",
                        ]
                    )
                )
            ),
        ),
        # move_group (with execution)
        Node(
            package="moveit_ros_move_group",
            executable="move_group",
            output="log",
            arguments=["--ros-args", "--log-level", log_level],
            parameters=[
                robot_description,
                robot_description_semantic,
                kinematics,
                joint_limits,
                planning_pipeline,
                trajectory_execution,
                planning_scene_monitor_parameters,
                moveit_controller_manager,
                {"use_sim_time": use_sim_time},
            ],
            condition=IfCondition(execute_trajectories),
        ),
        # move_group (without execution)
        Node(
            package="moveit_ros_move_group",
            executable="move_group",
            output="log",
            arguments=["--ros-args", "--log-level", log_level],
            parameters=[
                robot_description,
                robot_description_semantic,
                kinematics,
                joint_limits,
                planning_pipeline,
                trajectory_execution,
                planning_scene_monitor_parameters,
                {"use_sim_time": use_sim_time},
            ],
            condition=UnlessCondition(execute_trajectories),
        ),
        # move_servo
        Node(
            package="moveit_servo",
            executable="servo_node_main",
            output="log",
            arguments=["--ros-args", "--log-level", log_level],
            parameters=[
                robot_description,
                robot_description_semantic,
                kinematics,
                joint_limits,
                planning_pipeline,
                trajectory_execution,
                planning_scene_monitor_parameters,
                servo_params,
                {"use_sim_time": use_sim_time},
            ],
        condition=IfCondition(servo),
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
            parameters=[
                robot_description,
                robot_description_semantic,
                kinematics,
                planning_pipeline,
                joint_limits,
                {"use_sim_time": use_sim_time},
            ],
            condition=IfCondition(enable_rviz),
        ),
    ]

    # Add nodes for loading controllers
    for controller in moveit_controller_manager_yaml["controller_names"] + [
        "joint_state_broadcaster"
    ]:
        nodes.append(
            # controller_manager_spawner
            Node(
                package="controller_manager",
                executable="spawner",
                output="log",
                arguments=[controller, "--ros-args", "--log-level", log_level],
                parameters=[{"use_sim_time": use_sim_time}],
                condition=IfCondition(execute_trajectories),
            ),
        )

    return LaunchDescription(declared_arguments + nodes)


def load_yaml(package_name: str, file_path: str):
    """
    Load yaml configuration based on package name and file path relative to its share.
    """

    package_path = get_package_share_directory(package_name)
    absolute_file_path = path.join(package_path, file_path)
    return parse_yaml(absolute_file_path)


def parse_yaml(absolute_file_path: str):
    """
    Parse yaml from file, given its absolute file path.
    """

    try:
        with open(absolute_file_path, "r") as file:
            return yaml.safe_load(file)
    except EnvironmentError:
        return None


def generate_declared_arguments() -> List[DeclareLaunchArgument]:
    """
    Generate list of all launch arguments that are declared for this launch script.
    """

    return [
        # Locations of robot resources
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
            default_value="pepper_robot_",
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
            "collision_chassis",
            default_value="true",
            description="Flag to enable collision geometry for the chassis of pepper_robot.",
        ),
        DeclareLaunchArgument(
            "collision_wheels",
            default_value="true",
            description="Flag to enable collision geometry for the wheels of pepper_robot.",
        ),
        DeclareLaunchArgument(
            "collision_left_arm",
            default_value="true",
            description="Flag to enable collision geometry for manipulator's left_arm.",
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
        # State publishing
        DeclareLaunchArgument(
            "publish_state",
            default_value="true",
            description="Flag to enable robot state publisher.",
        ),
        # Execution
        DeclareLaunchArgument(
            "execute_trajectories",
            default_value="true",
            description="Flag to enable execution of trajectories for MoveIt 2.",
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
        # Servo
        DeclareLaunchArgument(
            "servo",
            default_value="true",
            description="Flag to enable MoveIt2 Servo for manipulator.",
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
            "gazebo_diff_drive",
            default_value="true",
            description="Flag to enable DiffDrive Gazebo plugin for pepper_robot.",
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
            "enable_rviz", default_value="true", description="Flag to enable RViz2."
        ),
        DeclareLaunchArgument(
            "rviz_config",
            default_value=path.join(
                get_package_share_directory("pepper_robot_moveit_config"),
                "rviz",
                "moveit.rviz",
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
