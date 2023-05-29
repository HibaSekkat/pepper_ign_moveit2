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


def joint_names(str = "") -> List[str]:
    return [
        "LShoulderPitch",
        "LShoulderRoll",
        "LElbowYaw",
        "LElbowRoll",
        "LWristYaw",
        "LHand",
    ]


def base_link_name(str = "") -> str:
    return "link_base"


def end_effector_name(str = "") -> str:
    return "end_effector"


def gripper_joint_names(str = "") -> List[str]:
    return [
        "LFinger1",
        "LFinger2",
        "LFinger3",
        "LFinger4",
        "LThumb1",
        "LThumb2",
    ]
