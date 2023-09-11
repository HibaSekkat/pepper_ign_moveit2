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
        prefix + "LShoulderPitch",
        prefix +"LShoulderRoll",
        prefix +"LElbowYaw",
        prefix +"LElbowRoll",
        prefix +"LWristYaw",
        prefix +"LHand",
    ]

def base_link_name(prefix: str = "") -> str:
    return prefix +"base_link"


def end_effector_name(prefix: str = "") -> str:
    return prefix +"left_eef"


def gripper_joint_names(prefix: str = "") -> List[str]:
    return [
        prefix +"LFinger11",
        prefix +"LFinger12",
        prefix +"LFinger13",
        prefix +"LFinger21",
        prefix +"LFinger22",
        prefix +"LFinger23",
        prefix +"LFinger31",
        prefix +"LFinger32",
        prefix +"LFinger33",
        prefix +"LFinger41",
        prefix +"LFinger42",
        prefix +"LFinger43",
        prefix +"LThumb1",
        prefix +"LThumb2",
    ]
