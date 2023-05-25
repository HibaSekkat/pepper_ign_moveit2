from typing import List

MOVE_GROUP_ARM: str = "left_arm"
MOVE_GROUP_GRIPPER: str = "l_gripper"

OPEN_GRIPPER_JOINT_POSITIONS: List[float] = [
    0.2,
    0.2,
    0.2,
    0.2,
    0.2,
    0.2,
]
CLOSED_GRIPPER_JOINT_POSITIONS: List[float] = [
    1.3,
    1.3,
    1.3,
    1.3,
    1.3,
    1.3,
]


def joint_names(prefix: str = "pepper_robot_") -> List[str]:
    return [
        prefix + "LShoulderPitch",
        prefix + "LShoulderRoll",
        prefix + "LElbowYaw",
        prefix + "LElbowRoll",
        prefix + "LWristYaw",
        prefix + "LHand",
    ]


def base_link_name(prefix: str = "pepper_robot_") -> str:
    return prefix + "link_base"


def end_effector_name(prefix: str = "pepper_robot_") -> str:
    return prefix + "end_effector"


def gripper_joint_names(prefix: str = "pepper_robot_") -> List[str]:
    return [
        prefix + "LFinger1",
        prefix + "LFinger2",
        prefix + "LFinger3",
        prefix + "LFinger4",
        prefix + "LThumb1",
        prefix + "LThumb2",
    ]
