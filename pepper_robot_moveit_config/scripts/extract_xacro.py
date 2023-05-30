import re

srdf_file_path = "/root/ws/src/pepper_ign_moveit2/pepper_robot_moveit_config/srdf/pepper_robot.srdf"
output_file_path = "/root/ws/src/pepper_ign_moveit2/pepper_robot_moveit_config/srdf/output.xacro"

with open(srdf_file_path, "r") as file:
    srdf_content = file.read()

xacro_regex = r"<xacro>(.*?)</xacro>"
xacro_match = re.search(xacro_regex, srdf_content, re.DOTALL)
if xacro_match:
    xacro_content = xacro_match.group(1)
else:
    xacro_content = ""

with open(output_file_path, "w") as file:
    file.write(xacro_content)