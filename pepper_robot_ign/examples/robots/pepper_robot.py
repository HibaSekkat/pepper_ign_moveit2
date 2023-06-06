from typing import List

MOVE_GROUP_ARM: str = "head"
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


def joint_names(str="") -> List[str]:
    return [
        "LShoulderPitch",
        "LShoulderRoll",
        "LElbowYaw",
        "LElbowRoll",
        "LWristYaw",
        "LHand",
    ]


def base_link_name(str="") -> str:
    return "link_base"


def end_effector_name(str="") -> str:
    return "end_effector"


def gripper_joint_names(str="") -> List[str]:
    return [
        "LFinger11",
        "LFinger12",
        "LFinger13",
        "RFinger11",
        "RFinger12",
        "RFinger13",
        "LFinger21",
        "LFinger22",
        "LFinger23",
        "RFinger21",
        "RFinger22",
        "RFinger23",
        "LFinger31",
        "LFinger32",
        "LFinger33",
        "RFinger31",
        "RFinger32",
        "RFinger33",
        "LFinger41",
        "LFinger42",
        "LFinger43",
        "RFinger41",
        "RFinger42",
        "RFinger43",
        "LThumb1",
        "RThumb1",
        "LThumb2",
        "RThumb2",
    ]
