from typing import List

MOVE_GROUP_ARM: str = "left_arm"
MOVE_GROUP_GRIPPER: str = "LHand"

OPEN_GRIPPER_JOINT_POSITIONS: List[float] = [
    1.3,
    1.3,
    1.3,
    1.3,
    1.3,
    1.3,
    1.3,
    1.3,
    1.3,
    1.3,
    1.3,
    1.3,
    1.3,
    1.3,
]
CLOSED_GRIPPER_JOINT_POSITIONS: List[float] = [
    0.2,
    0.2,
    0.2,
    0.2,
    0.2,
    0.2,
    0.2,
    0.2,
    0.2,
    0.2,
    0.2,
    0.2,
    0.2,
    0.2,
]

def joint_names(prefix: str = "") -> List[str]:
    return [
        "LShoulderPitch",
        "LShoulderRoll",
        "LElbowYaw",
        "LElbowRoll",
        "LWristYaw",
        "LHand",
    ]

def base_link_name(prefix: str = "") -> str:
    return "base_link"


def end_effector_name(prefix: str = "") -> str:
    return "left_eef"


def gripper_joint_names(prefix: str = "") -> List[str]:
    return [
        "LFinger11",
        "LFinger12",
        "LFinger13",
        "LFinger21",
        "LFinger22",
        "LFinger23",
        "LFinger31",
        "LFinger32",
        "LFinger33",
        "LFinger41",
        "LFinger42",
        "LFinger43",
        "LThumb1",
        "LThumb2",
    ]
