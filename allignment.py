import numpy as np

# Assuming you have the pose values for the link and inertial frame
link_pose = np.array([0, 0, 0, 0, 0, 0])
inertial_frame_pose = np.array([0.00312, 0, 0.11152, 0, 0, 0])

# Create transformation matrices
link_transform = np.eye(4)
inertial_frame_transform = np.eye(4)

# Fill the transformation matrices with pose values
link_transform[:3, 3] = link_pose[:3]
inertial_frame_transform[:3, 3] = inertial_frame_pose[:3]

# Check the transformation matrices
print("Link Transform:")
print(link_transform)
print("\nInertial Frame Transform:")
print(inertial_frame_transform)
