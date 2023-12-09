#!/usr/bin/env python3

import sys
from os import listdir, path
import numpy as np

import trimesh
from pcg_gazebo.parsers.sdf import SDF, create_sdf_element

# Note: Both `trimesh` and `pcg_gazebo` can be installed via `pip`
# `trimesh` is used to estimate volume and inertial properties from meshes of links
# `pcg_gazebo` is used for its SDF parser


def main():

    # Total mass taken from datasheet (given as ~18.0kg)
    # You can also use your own estimate of total mass if you managed to weigh pepper_robot yourself :)
    total_mass = 28
    if len(sys.argv) > 1:
        if float(sys.argv[1]) > 0.0:
            total_mass = float(sys.argv[1])
        else:
            print(
                "Error: Total mass of pepper_robot (first argument) must be positive."
            )
            exit(1)
    print(
        "Estimating inertial properties for each link to add up to %f kg" % total_mass
    )

    ## Get path to all visual meshes (automatic mode)
    visual_mesh_dir = path.join(
         path.dirname(path.dirname(path.realpath(__file__))),
         "pepper_robot",
         "meshes",
         "visual",
    )
    visual_mesh_basenames = listdir(visual_mesh_dir)
    visual_mesh_basenames.sort()

    ## Get path to specific visual meshes (manual mode)
    #visual_mesh_dir = path.join(
    #    path.dirname(path.dirname(path.realpath(__file__))),
    #    "pepper_robot",
    #    "meshes",
    #    "visual",
    #)
    #visual_mesh_basenames = ["HeadPitch.dae"]
    #visual_mesh_basenames.sort()

    # Load all meshes
    meshes = {}
    for mesh_basename in visual_mesh_basenames:
        link_name = path.splitext(mesh_basename)[0]
        mesh_path = path.join(visual_mesh_dir, mesh_basename)
        meshes[link_name] = trimesh.load(mesh_path, force="mesh", ignore_materials=True)

    # Compute the total volume of the robot in order to estimate the required density
    total_volume = 0
    for link_name in meshes:
        mesh = meshes[link_name]
        print("Volume estimate of %s: %f m^3" % (link_name, mesh.volume))
        if link_name == "finger":
            total_volume += mesh.volume
            print("Note: Finger volume added twice to the total volume")
        else:
            total_volume += mesh.volume

    # Compute average density
    average_density = total_mass / total_volume
    print("Average density estimate: %f kg/m^3" % average_density)

    # Estimate inertial properties for each link
    mass = {}
    inertia = {}
    centre_of_mass = {}
    for link_name in meshes:
        mesh = meshes[link_name]
        mesh.density = average_density
        mass = {'HeadPitch': 1.5189, 'HeadYaw': 0.27391, 'HipPitch': 2.4592,
                'HipRoll': 1.0234, 'KneePitch': 15.485, 'LElbowRoll': 0.16579,
                'LElbowYaw': 0.27495, 'LFinger11': 2e-06, 'LFinger12': 2e-06,
                'LFinger13': 2e-06, 'LFinger21': 2e-06, 'LFinger22': 2e-06,
                'LFinger23': 2e-06, 'LFinger31': 2e-06, 'LFinger32': 2e-06,
                'LFinger33': 2e-06, 'LFinger41': 2e-06, 'LFinger42': 2e-06,
                'LFinger43': 2e-06, 'LShoulderPitch': 0.3125, 'LShoulderRoll': 0.50527,
                'LThumb1': 2e-06, 'LThumb2': 2e-06, 'LWristYaw': 0.27555,
                'RElbowRoll': 0.16579, 'RElbowYaw': 0.27495, 'RFinger11': 2e-06,
                'RFinger12': 2e-06, 'RFinger13': 2e-06, 'RFinger21': 2e-06,
                'RFinger22': 2e-06, 'RFinger23': 2e-06, 'RFinger31': 2e-06,
                'RFinger32': 2e-06, 'RFinger33': 2e-06, 'RFinger41': 2e-06,
                'RFinger42': 2e-06, 'RFinger43': 2e-06, 'RShoulderPitch': 0.3125,
                'RShoulderRoll': 0.50527, 'RThumb1': 2e-06, 'RThumb2': 2e-06,
                'RWristYaw': 0.27555, 'Torso': 3.9953, 'WheelB': 1.29464,
                'WheelFL': 1.29464, 'WheelFR': 1.29464}
        centre_of_mass = {'HeadPitch': np.array([ 4.71298e-02, -1.04194e-03, 1.17396e+00]), 'HeadYaw' : np.array([-1.38721e-02, -8.05403e-04, 2.80087e-02]), 'Torso' : np.array([-3.04907e-01, 4.52667e-03, 3.96729e-01]), 'HipPitch' : np.array([7.36182e-02, 1.06276e-03, -9.66838e-01]), 'HipRoll' : np.array([1.77752e-02, -2.76230e-03, -6.47289e-01]), 'KneePitch' : np.array([-3.01996e-02, 2.19190e-03, -2.01479e+00]), 'LElbowRoll' : np.array([4.74585e-01, 3.53885e-02, 3.58340e-03]), 'LElbowYaw' : np.array([-7.45174e-07, 2.57313e-03, 1.11591e-03]), 'LShoulderPitch' : np.array([7.45188e-05, -4.87069e-04, -2.50686e-04]), 'LShoulderRoll' : np.array([1.70866e-01, 7.47789e-02, -3.17106e-03]), 'LWristYaw' : np.array([1.05085e-01, -2.42869e-02, 1.80051e-02]), 'RElbowRoll' : np.array([4.80719e-01, -2.50383e-02, -3.29600e-03]), 'RElbowYaw' : np.array([-7.45174e-07, 2.57313e-03, 1.11591e-03]), 'RShoulderPitch' : np.array([7.45188e-05, -4.87069e-04, -2.50686e-04]), 'RShoulderRoll' : np.array([9.13474e-01, -1.65714e-01, 1.04498e-03]), 'RWristYaw' : np.array([9.48306e-02, 1.63322e-02, 2.72905e-02]), 'WheelB' : np.array([-2.00775e-03, 2.47023e-03, -4.44721e-04]), 'WheelFL' : np.array([-1.24554e-03, -5.88167e-04, 1.27514e-04]), 'WheelFR' : np.array([-1.80919e-03, 2.10450e-04, -7.75170e-04])}
        #mass[link_name] = max(mesh.mass, 1e-10])}
        inertia[link_name] = mesh.moment_inertia
        centre_of_mass[link_name] = mesh.center_mass
        #print(centre_of_mass)
    # Create a new SDF with one model
    sdf = SDF()
    sdf.add_model(name="pepper_robot")
    model = sdf.models[0]

    # Set inertial properties for each link into the SDF
    for link_name in meshes:
        link = create_sdf_element("link")
        link.mass = mass[link_name]
        link.inertia.ixx = inertia[link_name][0][0]
        link.inertia.iyy = inertia[link_name][1][1]
        link.inertia.izz = inertia[link_name][2][2]
        link.inertia.ixy = inertia[link_name][0][1]
        link.inertia.ixz = inertia[link_name][0][2]
        link.inertia.iyz = inertia[link_name][1][2]
        link.inertial.pose = [
            centre_of_mass[link_name][0],
            centre_of_mass[link_name][1],
            centre_of_mass[link_name][2],
            0.0,
            0.0,
            0.0,
        ]
        model.add_link(link_name, link)

    # Write into output file
    output_file = "pepper_robot_inertial_out.sdf"
    sdf.export_xml(output_file)
    print('Results written into "%s"' % output_file)


if __name__ == "__main__":
    main()