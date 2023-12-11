<sdf version='1.7'>
  <model name='pepper_robot'>
    <link name='base_link'>
      <inertial>
        <pose>-0.0302 0.002192 -1.68079 0 -0 0</pose>
        <mass>15.485</mass>
        <inertia>
          <ixx>20.2656</ixx>
          <ixy>-0.00116473</ixy>
          <ixz>0.667579</ixz>
          <iyy>18.1698</iyy>
          <iyz>-0.000613168</iyz>
          <izz>21.9583</izz>
        </inertia>
      </inertial>
      <collision name='base_link_fixed_joint_lump__Tibia_collision'>
        <pose>0 0 0.334 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/KneePitch_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='base_link_fixed_joint_lump__Tibia_visual'>
        <pose>0 0 0.334 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/KneePitch.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='KneePitch' type='revolute'>
      <pose relative_to='base_link'>0 0 0.334 0 -0 0</pose>
      <parent>base_link</parent>
      <child>Pelvis</child>
      <axis>
        <xyz>0 -1 0</xyz>
        <limit>
          <lower>-0.514872</lower>
          <upper>0.514872</upper>
          <effort>27.702</effort>
          <velocity>2.93276</velocity>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='Pelvis'>
      <pose relative_to='KneePitch'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0.073618 0.001063 -0.966838 0 -0 0</pose>
        <mass>2.4592</mass>
        <inertia>
          <ixx>3.70658</ixx>
          <ixy>0.000421548</ixy>
          <ixz>0.0227469</ixz>
          <iyy>2.92633</iyy>
          <iyz>0.000503874</iyz>
          <izz>1.86247</izz>
        </inertia>
      </inertial>
      <collision name='Pelvis_collision'>
        <pose>0 0 0.268 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/HipPitch_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='Pelvis_visual'>
        <pose>0 0 0.268 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/HipPitch.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='HipPitch' type='revolute'>
      <pose relative_to='Pelvis'>0 0 0.268 0 -0 0</pose>
      <parent>Pelvis</parent>
      <child>Hip</child>
      <axis>
        <xyz>0 -1 0</xyz>
        <limit>
          <lower>-1.03847</lower>
          <upper>1.03847</upper>
          <effort>0</effort>
          <velocity>2.93276</velocity>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='Hip'>
      <pose relative_to='HipPitch'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0.017775 -0.002762 -0.647289 0 -0 0</pose>
        <mass>1.0234</mass>
        <inertia>
          <ixx>0.258524</ixx>
          <ixy>-9.15468e-05</ixy>
          <ixz>0.00408172</ixz>
          <iyy>0.355197</iyy>
          <iyz>-0.00130527</iyz>
          <izz>0.181933</izz>
        </inertia>
      </inertial>
      <collision name='Hip_collision'>
        <pose>0 0 0.079 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/HipRoll_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='Hip_visual'>
        <pose>0 0 0.079 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/HipRoll.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='HipRoll' type='revolute'>
      <pose relative_to='Hip'>0 0 0.079 0 -0 0</pose>
      <parent>Hip</parent>
      <child>torso</child>
      <axis>
        <xyz>-1 0 0</xyz>
        <limit>
          <lower>-0.514872</lower>
          <upper>0.514872</upper>
          <effort>0</effort>
          <velocity>2.27032</velocity>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='torso'>
      <pose relative_to='HipRoll'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>-0.304907 0.004527 0.396729 0 -0 0</pose>
        <mass>3.9953</mass>
        <inertia>
          <ixx>4.59559</ixx>
          <ixy>6.33591e-05</ixy>
          <ixz>0.669875</ixz>
          <iyy>4.07322</iyy>
          <iyz>-0.00019916</iyz>
          <izz>3.40466</izz>
        </inertia>
      </inertial>
      <collision name='torso_collision'>
        <pose>2e-05 0 0.139 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/Torso_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='torso_visual'>
        <pose>2e-05 0 0.139 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/Torso.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='HeadYaw' type='revolute'>
      <pose relative_to='torso'>-0.038 0 0.3089 0 -0 0</pose>
      <parent>torso</parent>
      <child>Neck</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-2.08567</lower>
          <upper>2.08567</upper>
          <effort>5.428</effort>
          <velocity>7.33998</velocity>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='Neck'>
      <pose relative_to='HeadYaw'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>-0.013872 -0.000805 0.028009 0 -0 0</pose>
        <mass>0.27391</mass>
        <inertia>
          <ixx>0.00442204</ixx>
          <ixy>-2.24163e-10</ixy>
          <ixz>0.000119272</ixz>
          <iyy>0.00470934</iyy>
          <iyz>1.46649e-09</iyz>
          <izz>0.00441196</izz>
        </inertia>
      </inertial>
      <collision name='Neck_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/HeadYaw_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='Neck_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/HeadYaw.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='HeadPitch' type='revolute'>
      <pose relative_to='Neck'>0 0 0 0 -0 0</pose>
      <parent>Neck</parent>
      <child>Head</child>
      <axis>
        <xyz>0 1 0</xyz>
        <limit>
          <lower>-0.706858</lower>
          <upper>0.4451</upper>
          <effort>0</effort>
          <velocity>0.1</velocity>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='Head'>
      <pose relative_to='HeadPitch'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0.04713 -0.001042 1.17396 0 -0 0</pose>
        <mass>1.5189</mass>
        <inertia>
          <ixx>0.929494</ixx>
          <ixy>0.000587077</ixy>
          <ixz>0.0392706</ixz>
          <iyy>0.915423</iyy>
          <iyz>5.12637e-06</iyz>
          <izz>0.954452</izz>
        </inertia>
      </inertial>
      <collision name='Head_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/HeadPitch_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='Head_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/HeadPitch.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='LShoulderPitch' type='revolute'>
      <pose relative_to='torso'>-0.057 0.14974 0.22582 0 -0 0</pose>
      <parent>torso</parent>
      <child>LShoulder</child>
      <axis>
        <xyz>0 1 0</xyz>
        <limit>
          <lower>-2.08567</lower>
          <upper>2.08567</upper>
          <effort>5.428</effort>
          <velocity>7.33998</velocity>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='LShoulder'>
      <pose relative_to='LShoulderPitch'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>7.5e-05 -0.000487 -0.000251 0 -0 0</pose>
        <mass>0.3125</mass>
        <inertia>
          <ixx>0.00858661</ixx>
          <ixy>-1.93407e-09</ixy>
          <ixz>6.39477e-10</ixz>
          <iyy>0.00858661</iyy>
          <iyz>-2.0848e-09</iyz>
          <izz>0.0103178</izz>
        </inertia>
      </inertial>
      <collision name='LShoulder_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LShoulderPitch_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='LShoulder_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LShoulderPitch.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='LShoulderRoll' type='revolute'>
      <pose relative_to='LShoulder'>0 0 0 0 -0 0</pose>
      <parent>LShoulder</parent>
      <child>LBicep</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>0.00872665</lower>
          <upper>1.56207</upper>
          <effort>2.666</effort>
          <velocity>9.22756</velocity>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='LBicep'>
      <pose relative_to='LShoulderRoll'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0.170866 0.074779 -0.003171 0 -0 0</pose>
        <mass>0.50527</mass>
        <inertia>
          <ixx>0.0248553</ixx>
          <ixy>0.00128992</ixy>
          <ixz>0.00171375</ixz>
          <iyy>0.0721283</iyy>
          <iyz>6.91816e-05</iyz>
          <izz>0.0680929</izz>
        </inertia>
      </inertial>
      <collision name='LBicep_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LShoulderRoll_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='LBicep_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LShoulderRoll.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='LElbowYaw' type='revolute'>
      <pose relative_to='LBicep'>0.1812 0.015 0.00013 0 -0.157079 0</pose>
      <parent>LBicep</parent>
      <child>LElbow</child>
      <axis>
        <xyz>1 0 0</xyz>
        <limit>
          <lower>-2.08567</lower>
          <upper>2.08567</upper>
          <effort>5.428</effort>
          <velocity>7.33998</velocity>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='LElbow'>
      <pose relative_to='LElbowYaw'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>-1e-06 0.002573 0.001116 0 -0 0</pose>
        <mass>0.27495</mass>
        <inertia>
          <ixx>0.00301552</ixx>
          <ixy>-1.04539e-10</ixy>
          <ixz>-4.22691e-12</ixz>
          <iyy>0.00304689</iyy>
          <iyz>-3.01268e-10</iyz>
          <izz>0.00304688</izz>
        </inertia>
      </inertial>
      <collision name='LElbow_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LElbowYaw_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='LElbow_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LElbowYaw.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='LElbowRoll' type='revolute'>
      <pose relative_to='LElbow'>0 0 0 0 -0 0</pose>
      <parent>LElbow</parent>
      <child>LForeArm</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-1.56207</lower>
          <upper>-0.00872665</upper>
          <effort>2.666</effort>
          <velocity>9.22756</velocity>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='LForeArm'>
      <pose relative_to='LElbowRoll'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0.474585 0.035389 0.003583 0 -0 0</pose>
        <mass>0.16579</mass>
        <inertia>
          <ixx>0.00720278</ixx>
          <ixy>0.00113472</ixy>
          <ixz>4.30017e-05</ixz>
          <iyy>0.00997783</iyy>
          <iyz>1.77852e-06</iyz>
          <izz>0.00968335</izz>
        </inertia>
      </inertial>
      <collision name='LForeArm_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LElbowRoll_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='LForeArm_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LElbowRoll.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='LWristYaw' type='revolute'>
      <pose relative_to='LForeArm'>0.15 0 0 0 -0 0</pose>
      <parent>LForeArm</parent>
      <child>l_wrist</child>
      <axis>
        <xyz>1 0 0</xyz>
        <limit>
          <lower>-1.82387</lower>
          <upper>1.82387</upper>
          <effort>0.2014</effort>
          <velocity>17.3835</velocity>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='l_wrist'>
      <pose relative_to='LWristYaw'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0.105085 -0.024287 0.018005 0 -0 0</pose>
        <mass>0.27555</mass>
        <inertia>
          <ixx>0.0117777</ixx>
          <ixy>0.000822933</ixy>
          <ixz>-0.00334266</ixz>
          <iyy>0.0380805</iyy>
          <iyz>-0.000150213</iyz>
          <izz>0.0405282</izz>
        </inertia>
      </inertial>
      <collision name='l_wrist_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LWristYaw_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='l_wrist_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LWristYaw.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='LFinger11' type='revolute'>
      <pose relative_to='l_wrist'>0.0821 -0.0268 0.004 1.74402 1.04064 -0.033434</pose>
      <parent>l_wrist</parent>
      <child>LFinger11_link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-1e+16</lower>
          <upper>1e+16</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='LFinger11_link'>
      <pose relative_to='LFinger11'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0 0 0 0 -0 0</pose>
        <mass>0.0017342</mass>
        <inertia>
          <ixx>3.46781e-06</ixx>
          <ixy>-3.25905e-08</ixy>
          <ixz>-1.77572e-07</ixz>
          <iyy>9.06796e-06</iyy>
          <iyz>-5.0427e-08</iyz>
          <izz>9.98141e-06</izz>
        </inertia>
      </inertial>
      <collision name='LFinger11_link_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LFinger11_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='LFinger11_link_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LFinger11.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='LFinger12' type='revolute'>
      <pose relative_to='LFinger11_link'>0.018 0 0 0 0 -1.0472</pose>
      <parent>LFinger11_link</parent>
      <child>LFinger12_link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-1e+16</lower>
          <upper>1e+16</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='LFinger12_link'>
      <pose relative_to='LFinger12'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0 0 0 0 -0 0</pose>
        <mass>0.0017342</mass>
        <inertia>
          <ixx>3.46781e-06</ixx>
          <ixy>-3.25905e-08</ixy>
          <ixz>-1.77572e-07</ixz>
          <iyy>9.06796e-06</iyy>
          <iyz>-5.0427e-08</iyz>
          <izz>9.98141e-06</izz>
        </inertia>
      </inertial>
      <collision name='LFinger12_link_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LFinger12_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='LFinger12_link_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LFinger12.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='LFinger13' type='revolute'>
      <pose relative_to='LFinger12_link'>0.018 0 0 0 0 -1.0472</pose>
      <parent>LFinger12_link</parent>
      <child>LFinger13_link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-1e+16</lower>
          <upper>1e+16</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='LFinger13_link'>
      <pose relative_to='LFinger13'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0 0 0 0 -0 0</pose>
        <mass>0.00121197</mass>
        <inertia>
          <ixx>2.09224e-06</ixx>
          <ixy>-1.14574e-07</ixy>
          <ixz>1.41679e-08</ixz>
          <iyy>4.04999e-06</iyy>
          <iyz>-5.70419e-09</iyz>
          <izz>4.41654e-06</izz>
        </inertia>
      </inertial>
      <collision name='LFinger13_link_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LFinger13_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='LFinger13_link_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LFinger13.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='LFinger21' type='revolute'>
      <pose relative_to='l_wrist'>0.0873 -0.0073 0.006 1.5708 1.0472 -0.061086</pose>
      <parent>l_wrist</parent>
      <child>LFinger21_link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-1e+16</lower>
          <upper>1e+16</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='LFinger21_link'>
      <pose relative_to='LFinger21'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0 0 0 0 -0 0</pose>
        <mass>0.0017342</mass>
        <inertia>
          <ixx>3.46781e-06</ixx>
          <ixy>-3.25906e-08</ixy>
          <ixz>-1.77572e-07</ixz>
          <iyy>9.06796e-06</iyy>
          <iyz>-5.0427e-08</iyz>
          <izz>9.98141e-06</izz>
        </inertia>
      </inertial>
      <collision name='LFinger21_link_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LFinger21_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='LFinger21_link_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LFinger21.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='LFinger22' type='revolute'>
      <pose relative_to='LFinger21_link'>0.018 0 0 0 0 -1.0472</pose>
      <parent>LFinger21_link</parent>
      <child>LFinger22_link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-1e+16</lower>
          <upper>1e+16</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='LFinger22_link'>
      <pose relative_to='LFinger22'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0 0 0 0 -0 0</pose>
        <mass>0.0017342</mass>
        <inertia>
          <ixx>3.46781e-06</ixx>
          <ixy>-3.25914e-08</ixy>
          <ixz>-1.77572e-07</ixz>
          <iyy>9.06796e-06</iyy>
          <iyz>-5.04271e-08</iyz>
          <izz>9.98141e-06</izz>
        </inertia>
      </inertial>
      <collision name='LFinger22_link_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LFinger22_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='LFinger22_link_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LFinger22.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='LFinger23' type='revolute'>
      <pose relative_to='LFinger22_link'>0.018 0 0 0 0 -1.0472</pose>
      <parent>LFinger22_link</parent>
      <child>LFinger23_link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-1e+16</lower>
          <upper>1e+16</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='LFinger23_link'>
      <pose relative_to='LFinger23'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0 0 0 0 -0 0</pose>
        <mass>0.00121197</mass>
        <inertia>
          <ixx>2.09224e-06</ixx>
          <ixy>-1.14574e-07</ixy>
          <ixz>1.41678e-08</ixz>
          <iyy>4.04999e-06</iyy>
          <iyz>-5.70416e-09</iyz>
          <izz>4.41654e-06</izz>
        </inertia>
      </inertial>
      <collision name='LFinger23_link_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LFinger23_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='LFinger23_link_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LFinger23.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='LFinger31' type='revolute'>
      <pose relative_to='l_wrist'>0.0833 0.0123 0.004 1.46636 1.04483 -0.029314</pose>
      <parent>l_wrist</parent>
      <child>LFinger31_link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-1e+16</lower>
          <upper>1e+16</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='LFinger31_link'>
      <pose relative_to='LFinger31'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0 0 0 0 -0 0</pose>
        <mass>0.0017342</mass>
        <inertia>
          <ixx>3.46781e-06</ixx>
          <ixy>-3.25905e-08</ixy>
          <ixz>-1.77572e-07</ixz>
          <iyy>9.06796e-06</iyy>
          <iyz>-5.0427e-08</iyz>
          <izz>9.98141e-06</izz>
        </inertia>
      </inertial>
      <collision name='LFinger31_link_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LFinger31_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='LFinger31_link_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LFinger31.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='LFinger32' type='revolute'>
      <pose relative_to='LFinger31_link'>0.018 0 0 0 0 -1.0472</pose>
      <parent>LFinger31_link</parent>
      <child>LFinger32_link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-1e+16</lower>
          <upper>1e+16</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='LFinger32_link'>
      <pose relative_to='LFinger32'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0 0 0 0 -0 0</pose>
        <mass>0.0017342</mass>
        <inertia>
          <ixx>3.46781e-06</ixx>
          <ixy>-3.25906e-08</ixy>
          <ixz>-1.77572e-07</ixz>
          <iyy>9.06796e-06</iyy>
          <iyz>-5.0427e-08</iyz>
          <izz>9.98141e-06</izz>
        </inertia>
      </inertial>
      <collision name='LFinger32_link_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LFinger32_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='LFinger32_link_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LFinger32.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='LFinger33' type='revolute'>
      <pose relative_to='LFinger32_link'>0.018 0 0 0 0 -1.0472</pose>
      <parent>LFinger32_link</parent>
      <child>LFinger33_link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-1e+16</lower>
          <upper>1e+16</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='LFinger33_link'>
      <pose relative_to='LFinger33'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0 0 0 0 -0 0</pose>
        <mass>0.00121197</mass>
        <inertia>
          <ixx>2.09224e-06</ixx>
          <ixy>-1.14574e-07</ixy>
          <ixz>1.41681e-08</ixz>
          <iyy>4.04999e-06</iyy>
          <iyz>-5.70419e-09</iyz>
          <izz>4.41654e-06</izz>
        </inertia>
      </inertial>
      <collision name='LFinger33_link_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LFinger33_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='LFinger33_link_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LFinger33.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='LFinger41' type='revolute'>
      <pose relative_to='l_wrist'>0.074 0.0309 0 1.39757 1.04064 0.068339</pose>
      <parent>l_wrist</parent>
      <child>LFinger41_link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-1e+16</lower>
          <upper>1e+16</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='LFinger41_link'>
      <pose relative_to='LFinger41'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0 0 0 0 -0 0</pose>
        <mass>0.0017342</mass>
        <inertia>
          <ixx>3.46781e-06</ixx>
          <ixy>-3.25905e-08</ixy>
          <ixz>-1.77572e-07</ixz>
          <iyy>9.06796e-06</iyy>
          <iyz>-5.0427e-08</iyz>
          <izz>9.98141e-06</izz>
        </inertia>
      </inertial>
      <collision name='LFinger41_link_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LFinger41_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='LFinger41_link_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LFinger41.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='LFinger42' type='revolute'>
      <pose relative_to='LFinger41_link'>0.018 0 0 0 0 -1.0472</pose>
      <parent>LFinger41_link</parent>
      <child>LFinger42_link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-1e+16</lower>
          <upper>1e+16</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='LFinger42_link'>
      <pose relative_to='LFinger42'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0 0 0 0 -0 0</pose>
        <mass>0.0017342</mass>
        <inertia>
          <ixx>3.46781e-06</ixx>
          <ixy>-3.25905e-08</ixy>
          <ixz>-1.77572e-07</ixz>
          <iyy>9.06796e-06</iyy>
          <iyz>-5.0427e-08</iyz>
          <izz>9.98141e-06</izz>
        </inertia>
      </inertial>
      <collision name='LFinger42_link_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LFinger42_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='LFinger42_link_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LFinger42.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='LFinger43' type='revolute'>
      <pose relative_to='LFinger42_link'>0.018 0 0 0 0 -1.0472</pose>
      <parent>LFinger42_link</parent>
      <child>LFinger43_link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-1e+16</lower>
          <upper>1e+16</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='LFinger43_link'>
      <pose relative_to='LFinger43'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0 0 0 0 -0 0</pose>
        <mass>0.00121197</mass>
        <inertia>
          <ixx>2.09224e-06</ixx>
          <ixy>-1.14574e-07</ixy>
          <ixz>1.41681e-08</ixz>
          <iyy>4.04999e-06</iyy>
          <iyz>-5.70413e-09</iyz>
          <izz>4.41654e-06</izz>
        </inertia>
      </inertial>
      <collision name='LFinger43_link_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LFinger43_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='LFinger43_link_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LFinger43.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='LHand' type='revolute'>
      <pose relative_to='l_wrist'>0.025 0 0 0 -0 0</pose>
      <parent>l_wrist</parent>
      <child>l_gripper</child>
      <axis>
        <xyz>1 0 0</xyz>
        <limit>
          <lower>0.02</lower>
          <upper>0.98</upper>
          <effort>0.144</effort>
          <velocity>12.56</velocity>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='l_gripper'>
      <pose relative_to='LHand'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0 0 0 0 -0 0</pose>
        <mass>0.27555</mass>
        <inertia>
          <ixx>0.0117777</ixx>
          <ixy>0.000822933</ixy>
          <ixz>-0.00334266</ixz>
          <iyy>0.0380805</iyy>
          <iyz>-0.000150213</iyz>
          <izz>0.0405282</izz>
        </inertia>
      </inertial>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='LThumb1' type='revolute'>
      <pose relative_to='l_wrist'>0.0482 -0.0357 -0.0199 -1.95836 0.60626 0.533978</pose>
      <parent>l_wrist</parent>
      <child>LThumb1_link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-1e+16</lower>
          <upper>1e+16</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='LThumb1_link'>
      <pose relative_to='LThumb1'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0 0 0 0 -0 0</pose>
        <mass>0.0017342</mass>
        <inertia>
          <ixx>3.46781e-06</ixx>
          <ixy>-3.25905e-08</ixy>
          <ixz>-1.77572e-07</ixz>
          <iyy>9.06796e-06</iyy>
          <iyz>-5.04269e-08</iyz>
          <izz>9.98141e-06</izz>
        </inertia>
      </inertial>
      <collision name='LThumb1_link_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LThumb1_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='LThumb1_link_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LThumb1.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='LThumb2' type='revolute'>
      <pose relative_to='LThumb1_link'>0.022 0 0 0 0 -1.0472</pose>
      <parent>LThumb1_link</parent>
      <child>LThumb2_link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-1e+16</lower>
          <upper>1e+16</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='LThumb2_link'>
      <pose relative_to='LThumb2'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0 0 0 0 -0 0</pose>
        <mass>0.00121197</mass>
        <inertia>
          <ixx>2.09224e-06</ixx>
          <ixy>-1.14574e-07</ixy>
          <ixz>1.41679e-08</ixz>
          <iyy>4.04999e-06</iyy>
          <iyz>-5.70419e-09</iyz>
          <izz>4.41654e-06</izz>
        </inertia>
      </inertial>
      <collision name='LThumb2_link_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LThumb2_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='LThumb2_link_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/LThumb2.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='RShoulderPitch' type='revolute'>
      <pose relative_to='torso'>-0.057 -0.14974 0.22582 0 -0 0</pose>
      <parent>torso</parent>
      <child>RShoulder</child>
      <axis>
        <xyz>0 1 0</xyz>
        <limit>
          <lower>-2.08567</lower>
          <upper>2.08567</upper>
          <effort>5.428</effort>
          <velocity>7.33998</velocity>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='RShoulder'>
      <pose relative_to='RShoulderPitch'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>7.5e-05 -0.000487 -0.000251 0 -0 0</pose>
        <mass>0.3125</mass>
        <inertia>
          <ixx>0.00858661</ixx>
          <ixy>-1.93407e-09</ixy>
          <ixz>6.39477e-10</ixz>
          <iyy>0.00858661</iyy>
          <iyz>-2.0848e-09</iyz>
          <izz>0.0103178</izz>
        </inertia>
      </inertial>
      <collision name='RShoulder_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RShoulderPitch_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='RShoulder_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RShoulderPitch.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='RShoulderRoll' type='revolute'>
      <pose relative_to='RShoulder'>0 0 0 0 -0 0</pose>
      <parent>RShoulder</parent>
      <child>RBicep</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-1.56207</lower>
          <upper>-0.00872665</upper>
          <effort>2.666</effort>
          <velocity>9.22756</velocity>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='RBicep'>
      <pose relative_to='RShoulderRoll'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0.913474 -0.165714 0.001045 0 -0 0</pose>
        <mass>0.50527</mass>
        <inertia>
          <ixx>0.0248553</ixx>
          <ixy>0.00128992</ixy>
          <ixz>0.00171375</ixz>
          <iyy>0.0721283</iyy>
          <iyz>6.91816e-05</iyz>
          <izz>0.0680929</izz>
        </inertia>
      </inertial>
      <collision name='RBicep_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RShoulderRoll_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='RBicep_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RShoulderRoll.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='RElbowYaw' type='revolute'>
      <pose relative_to='RBicep'>0.1812 -0.015 0.00013 0 -0.157079 0</pose>
      <parent>RBicep</parent>
      <child>RElbow</child>
      <axis>
        <xyz>1 0 0</xyz>
        <limit>
          <lower>-2.08567</lower>
          <upper>2.08567</upper>
          <effort>5.428</effort>
          <velocity>7.33998</velocity>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='RElbow'>
      <pose relative_to='RElbowYaw'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>-1e-06 0.002573 0.001116 0 -0 0</pose>
        <mass>0.27495</mass>
        <inertia>
          <ixx>0.00301552</ixx>
          <ixy>-1.04539e-10</ixy>
          <ixz>-4.22691e-12</ixz>
          <iyy>0.00304689</iyy>
          <iyz>-3.01268e-10</iyz>
          <izz>0.00304688</izz>
        </inertia>
      </inertial>
      <collision name='RElbow_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RElbowYaw_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='RElbow_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RElbowYaw.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='RElbowRoll' type='revolute'>
      <pose relative_to='RElbow'>0 0 0 0 -0 0</pose>
      <parent>RElbow</parent>
      <child>RForeArm</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>0.00872665</lower>
          <upper>1.56207</upper>
          <effort>2.666</effort>
          <velocity>9.22756</velocity>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='RForeArm'>
      <pose relative_to='RElbowRoll'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0.480719 -0.025038 -0.003296 0 -0 0</pose>
        <mass>0.16579</mass>
        <inertia>
          <ixx>0.00720278</ixx>
          <ixy>-0.00113472</ixy>
          <ixz>4.30017e-05</ixz>
          <iyy>0.00997783</iyy>
          <iyz>-1.77852e-06</iyz>
          <izz>0.00968335</izz>
        </inertia>
      </inertial>
      <collision name='RForeArm_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RElbowRoll_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='RForeArm_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RElbowRoll.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='RWristYaw' type='revolute'>
      <pose relative_to='RForeArm'>0.15 0 0 0 -0 0</pose>
      <parent>RForeArm</parent>
      <child>r_wrist</child>
      <axis>
        <xyz>1 0 0</xyz>
        <limit>
          <lower>-1.82387</lower>
          <upper>1.82387</upper>
          <effort>0.2014</effort>
          <velocity>17.3835</velocity>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='r_wrist'>
      <pose relative_to='RWristYaw'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0.094831 0.016332 0.027291 0 -0 0</pose>
        <mass>0.27555</mass>
        <inertia>
          <ixx>0.0117777</ixx>
          <ixy>-0.000822933</ixy>
          <ixz>-0.00334266</ixz>
          <iyy>0.0380805</iyy>
          <iyz>0.000150213</iyz>
          <izz>0.0405282</izz>
        </inertia>
      </inertial>
      <collision name='r_wrist_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RWristYaw_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='r_wrist_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RWristYaw.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='RFinger11' type='revolute'>
      <pose relative_to='r_wrist'>0.0821 0.0268 0.004 1.39757 1.04064 0.033433</pose>
      <parent>r_wrist</parent>
      <child>RFinger11_link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-1e+16</lower>
          <upper>1e+16</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='RFinger11_link'>
      <pose relative_to='RFinger11'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0 0 0 0 -0 0</pose>
        <mass>0.0017342</mass>
        <inertia>
          <ixx>3.46781e-06</ixx>
          <ixy>-3.25905e-08</ixy>
          <ixz>-1.77572e-07</ixz>
          <iyy>9.06796e-06</iyy>
          <iyz>-5.0427e-08</iyz>
          <izz>9.98141e-06</izz>
        </inertia>
      </inertial>
      <collision name='RFinger11_link_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RFinger11_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='RFinger11_link_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RFinger11.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='RFinger12' type='revolute'>
      <pose relative_to='RFinger11_link'>0.018 0 0 0 0 -1.0472</pose>
      <parent>RFinger11_link</parent>
      <child>RFinger12_link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-1e+16</lower>
          <upper>1e+16</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='RFinger12_link'>
      <pose relative_to='RFinger12'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0 0 0 0 -0 0</pose>
        <mass>0.0017342</mass>
        <inertia>
          <ixx>3.46781e-06</ixx>
          <ixy>-3.25905e-08</ixy>
          <ixz>-1.77572e-07</ixz>
          <iyy>9.06796e-06</iyy>
          <iyz>-5.0427e-08</iyz>
          <izz>9.98141e-06</izz>
        </inertia>
      </inertial>
      <collision name='RFinger12_link_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RFinger12_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='RFinger12_link_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RFinger12.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='RFinger13' type='revolute'>
      <pose relative_to='RFinger12_link'>0.018 0 0 0 0 -1.0472</pose>
      <parent>RFinger12_link</parent>
      <child>RFinger13_link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-1e+16</lower>
          <upper>1e+16</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='RFinger13_link'>
      <pose relative_to='RFinger13'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0 0 0 0 -0 0</pose>
        <mass>0.00121197</mass>
        <inertia>
          <ixx>2.09224e-06</ixx>
          <ixy>-1.14574e-07</ixy>
          <ixz>1.41679e-08</ixz>
          <iyy>4.04999e-06</iyy>
          <iyz>-5.70419e-09</iyz>
          <izz>4.41654e-06</izz>
        </inertia>
      </inertial>
      <collision name='RFinger13_link_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RFinger13_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='RFinger13_link_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RFinger13.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='RFinger21' type='revolute'>
      <pose relative_to='r_wrist'>0.0873 0.0073 0.006 1.5708 1.0472 0.061086</pose>
      <parent>r_wrist</parent>
      <child>RFinger21_link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-1e+16</lower>
          <upper>1e+16</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='RFinger21_link'>
      <pose relative_to='RFinger21'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0 0 0 0 -0 0</pose>
        <mass>0.0017342</mass>
        <inertia>
          <ixx>3.46781e-06</ixx>
          <ixy>-3.25906e-08</ixy>
          <ixz>-1.77572e-07</ixz>
          <iyy>9.06796e-06</iyy>
          <iyz>-5.0427e-08</iyz>
          <izz>9.98141e-06</izz>
        </inertia>
      </inertial>
      <collision name='RFinger21_link_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RFinger21_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='RFinger21_link_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RFinger21.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='RFinger22' type='revolute'>
      <pose relative_to='RFinger21_link'>0.018 0 0 0 0 -1.0472</pose>
      <parent>RFinger21_link</parent>
      <child>RFinger22_link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-1e+16</lower>
          <upper>1e+16</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='RFinger22_link'>
      <pose relative_to='RFinger22'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0 0 0 0 -0 0</pose>
        <mass>0.0017342</mass>
        <inertia>
          <ixx>3.46781e-06</ixx>
          <ixy>-3.25914e-08</ixy>
          <ixz>-1.77572e-07</ixz>
          <iyy>9.06796e-06</iyy>
          <iyz>-5.04271e-08</iyz>
          <izz>9.98141e-06</izz>
        </inertia>
      </inertial>
      <collision name='RFinger22_link_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RFinger22_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='RFinger22_link_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RFinger22.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='RFinger23' type='revolute'>
      <pose relative_to='RFinger22_link'>0.018 0 0 0 0 -1.0472</pose>
      <parent>RFinger22_link</parent>
      <child>RFinger23_link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-1e+16</lower>
          <upper>1e+16</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='RFinger23_link'>
      <pose relative_to='RFinger23'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0 0 0 0 -0 0</pose>
        <mass>0.00121197</mass>
        <inertia>
          <ixx>2.09224e-06</ixx>
          <ixy>-1.14574e-07</ixy>
          <ixz>1.41678e-08</ixz>
          <iyy>4.04999e-06</iyy>
          <iyz>-5.70416e-09</iyz>
          <izz>4.41654e-06</izz>
        </inertia>
      </inertial>
      <collision name='RFinger23_link_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RFinger23_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='RFinger23_link_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RFinger23.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='RFinger31' type='revolute'>
      <pose relative_to='r_wrist'>0.0833 -0.0123 0.004 1.67523 1.04483 0.029316</pose>
      <parent>r_wrist</parent>
      <child>RFinger31_link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-1e+16</lower>
          <upper>1e+16</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='RFinger31_link'>
      <pose relative_to='RFinger31'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0 0 0 0 -0 0</pose>
        <mass>0.0017342</mass>
        <inertia>
          <ixx>3.46781e-06</ixx>
          <ixy>-3.25905e-08</ixy>
          <ixz>-1.77572e-07</ixz>
          <iyy>9.06796e-06</iyy>
          <iyz>-5.0427e-08</iyz>
          <izz>9.98141e-06</izz>
        </inertia>
      </inertial>
      <collision name='RFinger31_link_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RFinger31_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='RFinger31_link_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RFinger31.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='RFinger32' type='revolute'>
      <pose relative_to='RFinger31_link'>0.018 0 0 0 0 -1.0472</pose>
      <parent>RFinger31_link</parent>
      <child>RFinger32_link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-1e+16</lower>
          <upper>1e+16</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='RFinger32_link'>
      <pose relative_to='RFinger32'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0 0 0 0 -0 0</pose>
        <mass>0.0017342</mass>
        <inertia>
          <ixx>3.46781e-06</ixx>
          <ixy>-3.25906e-08</ixy>
          <ixz>-1.77572e-07</ixz>
          <iyy>9.06796e-06</iyy>
          <iyz>-5.0427e-08</iyz>
          <izz>9.98141e-06</izz>
        </inertia>
      </inertial>
      <collision name='RFinger32_link_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RFinger32_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='RFinger32_link_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RFinger32.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='RFinger33' type='revolute'>
      <pose relative_to='RFinger32_link'>0.018 0 0 0 0 -1.0472</pose>
      <parent>RFinger32_link</parent>
      <child>RFinger33_link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-1e+16</lower>
          <upper>1e+16</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='RFinger33_link'>
      <pose relative_to='RFinger33'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0 0 0 0 -0 0</pose>
        <mass>0.00121197</mass>
        <inertia>
          <ixx>2.09224e-06</ixx>
          <ixy>-1.14574e-07</ixy>
          <ixz>1.41681e-08</ixz>
          <iyy>4.04999e-06</iyy>
          <iyz>-5.70419e-09</iyz>
          <izz>4.41654e-06</izz>
        </inertia>
      </inertial>
      <collision name='RFinger33_link_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RFinger33_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='RFinger33_link_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RFinger33.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='RFinger41' type='revolute'>
      <pose relative_to='r_wrist'>0.074 -0.0309 0 1.74402 1.04064 -0.068339</pose>
      <parent>r_wrist</parent>
      <child>RFinger41_link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-1e+16</lower>
          <upper>1e+16</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='RFinger41_link'>
      <pose relative_to='RFinger41'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0 0 0 0 -0 0</pose>
        <mass>0.0017342</mass>
        <inertia>
          <ixx>3.46781e-06</ixx>
          <ixy>-3.25905e-08</ixy>
          <ixz>-1.77572e-07</ixz>
          <iyy>9.06796e-06</iyy>
          <iyz>-5.0427e-08</iyz>
          <izz>9.98141e-06</izz>
        </inertia>
      </inertial>
      <collision name='RFinger41_link_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RFinger41_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='RFinger41_link_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RFinger41.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='RFinger42' type='revolute'>
      <pose relative_to='RFinger41_link'>0.018 0 0 0 0 -1.0472</pose>
      <parent>RFinger41_link</parent>
      <child>RFinger42_link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-1e+16</lower>
          <upper>1e+16</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='RFinger42_link'>
      <pose relative_to='RFinger42'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0 0 0 0 -0 0</pose>
        <mass>0.0017342</mass>
        <inertia>
          <ixx>3.46781e-06</ixx>
          <ixy>-3.25905e-08</ixy>
          <ixz>-1.77572e-07</ixz>
          <iyy>9.06796e-06</iyy>
          <iyz>-5.0427e-08</iyz>
          <izz>9.98141e-06</izz>
        </inertia>
      </inertial>
      <collision name='RFinger42_link_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RFinger42_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='RFinger42_link_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RFinger42.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='RFinger43' type='revolute'>
      <pose relative_to='RFinger42_link'>0.018 0 0 0 0 -1.0472</pose>
      <parent>RFinger42_link</parent>
      <child>RFinger43_link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-1e+16</lower>
          <upper>1e+16</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='RFinger43_link'>
      <pose relative_to='RFinger43'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0 0 0 0 -0 0</pose>
        <mass>0.00121197</mass>
        <inertia>
          <ixx>2.09224e-06</ixx>
          <ixy>-1.14574e-07</ixy>
          <ixz>1.41681e-08</ixz>
          <iyy>4.04999e-06</iyy>
          <iyz>-5.70413e-09</iyz>
          <izz>4.41654e-06</izz>
        </inertia>
      </inertial>
      <collision name='RFinger43_link_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RFinger43_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='RFinger43_link_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RFinger43.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='RHand' type='revolute'>
      <pose relative_to='r_wrist'>0.025 0 0 0 -0 0</pose>
      <parent>r_wrist</parent>
      <child>r_gripper</child>
      <axis>
        <xyz>1 0 0</xyz>
        <limit>
          <lower>0.02</lower>
          <upper>0.98</upper>
          <effort>0.144</effort>
          <velocity>12.56</velocity>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='r_gripper'>
      <pose relative_to='RHand'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0 0 0 0 -0 0</pose>
        <mass>0.27555</mass>
        <inertia>
          <ixx>0.0117777</ixx>
          <ixy>-0.000822933</ixy>
          <ixz>-0.00334266</ixz>
          <iyy>0.0380805</iyy>
          <iyz>0.000150213</iyz>
          <izz>0.0405282</izz>
        </inertia>
      </inertial>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='RThumb1' type='revolute'>
      <pose relative_to='r_wrist'>0.0482 0.0357 -0.0199 -1.18323 0.60626 -0.533978</pose>
      <parent>r_wrist</parent>
      <child>RThumb1_link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-1e+16</lower>
          <upper>1e+16</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='RThumb1_link'>
      <pose relative_to='RThumb1'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0 0 0 0 -0 0</pose>
        <mass>0.0017342</mass>
        <inertia>
          <ixx>3.46781e-06</ixx>
          <ixy>-3.25905e-08</ixy>
          <ixz>-1.77572e-07</ixz>
          <iyy>9.06796e-06</iyy>
          <iyz>-5.04269e-08</iyz>
          <izz>9.98141e-06</izz>
        </inertia>
      </inertial>
      <collision name='RThumb1_link_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RThumb1_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='RThumb1_link_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RThumb1.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='RThumb2' type='revolute'>
      <pose relative_to='RThumb1_link'>0.022 0 0 0 0 -1.0472</pose>
      <parent>RThumb1_link</parent>
      <child>RThumb2_link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <limit>
          <lower>-1e+16</lower>
          <upper>1e+16</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='RThumb2_link'>
      <pose relative_to='RThumb2'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0 0 0 0 -0 0</pose>
        <mass>0.00121197</mass>
        <inertia>
          <ixx>2.09224e-06</ixx>
          <ixy>-1.14574e-07</ixy>
          <ixz>1.41679e-08</ixz>
          <iyy>4.04999e-06</iyy>
          <iyz>-5.70419e-09</iyz>
          <izz>4.41654e-06</izz>
        </inertia>
      </inertial>
      <collision name='RThumb2_link_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RThumb2_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode/>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='RThumb2_link_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/RThumb2.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
      <self_collide>0</self_collide>
    </link>
    <joint name='WheelB' type='revolute'>
      <pose relative_to='base_link'>-0.17 0 0.07 0 0 -3.14159</pose>
      <parent>base_link</parent>
      <child>WheelB_link</child>
      <axis>
        <xyz>1 0 0</xyz>
        <limit>
          <effort>3.25</effort>
          <velocity>6.28319</velocity>
          <lower>-1e+16</lower>
          <upper>1e+16</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='WheelB_link'>
      <pose relative_to='WheelB'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>-0.002008 0.00247 -0.000445 0 -0 0</pose>
        <mass>1.29464</mass>
        <inertia>
          <ixx>0.147598</ixx>
          <ixy>1.39831e-09</ixy>
          <ixz>-1.61447e-08</ixz>
          <iyy>0.146385</iyy>
          <iyz>9.74789e-10</iyz>
          <izz>0.147598</izz>
        </inertia>
      </inertial>
      <collision name='WheelB_link_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/WheelB_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode>
              <kp>1e+07</kp>
              <kd>1</kd>
              <min_depth>0.003</min_depth>
            </ode>
          </contact>
          <friction>
            <ode>
              <mu>0.5</mu>
              <mu2>0.5</mu2>
              <fdir1>1 0 0</fdir1>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='WheelB_link_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/WheelB.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
    </link>
    <joint name='WheelFL' type='revolute'>
      <pose relative_to='base_link'>0.09 0.155 0.07 0 -0 1.07517</pose>
      <parent>base_link</parent>
      <child>WheelFL_link</child>
      <axis>
        <xyz>1 0 0</xyz>
        <limit>
          <effort>3.25</effort>
          <velocity>6.28319</velocity>
          <lower>-1e+16</lower>
          <upper>1e+16</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='WheelFL_link'>
      <pose relative_to='WheelFL'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>-0.001246 -0.000588 0.000128 0 -0 0</pose>
        <mass>1.29464</mass>
        <inertia>
          <ixx>0.147598</ixx>
          <ixy>1.39831e-09</ixy>
          <ixz>-1.85947e-08</ixz>
          <iyy>0.146385</iyy>
          <iyz>-1.69324e-10</iyz>
          <izz>0.147598</izz>
        </inertia>
      </inertial>
      <collision name='WheelFL_link_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/WheelFL_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode>
              <kp>1e+07</kp>
              <kd>1</kd>
              <min_depth>0.003</min_depth>
            </ode>
          </contact>
          <friction>
            <ode>
              <mu>1</mu>
              <mu2>0</mu2>
              <fdir1>1 0 0</fdir1>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='WheelFL_link_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/WheelFL.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
    </link>
    <joint name='WheelFR' type='revolute'>
      <pose relative_to='base_link'>0.09 -0.155 0.07 0 0 -1.07517</pose>
      <parent>base_link</parent>
      <child>WheelFR_link</child>
      <axis>
        <xyz>1 0 0</xyz>
        <limit>
          <effort>3.25</effort>
          <velocity>6.28319</velocity>
          <lower>-1e+16</lower>
          <upper>1e+16</upper>
        </limit>
        <dynamics>
          <spring_reference>0</spring_reference>
          <spring_stiffness>0</spring_stiffness>
        </dynamics>
      </axis>
    </joint>
    <link name='WheelFR_link'>
      <pose relative_to='WheelFR'>0 0 0 0 -0 0</pose>
      <inertial>
        <pose>0 -1e-06 0 0 -0 0</pose>
        <mass>1.29464</mass>
        <inertia>
          <ixx>0.147598</ixx>
          <ixy>-1.30569e-09</ixy>
          <ixz>-1.75702e-08</ixz>
          <iyy>0.146385</iyy>
          <iyz>2.21159e-10</iyz>
          <izz>0.147598</izz>
        </inertia>
      </inertial>
      <collision name='WheelFR_link_collision'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/WheelFR_0.10.stl</uri>
          </mesh>
        </geometry>
        <surface>
          <contact>
            <ode>
              <kp>1e+07</kp>
              <kd>1</kd>
              <min_depth>0.003</min_depth>
            </ode>
          </contact>
          <friction>
            <ode>
              <mu>0</mu>
              <mu2>1</mu2>
              <fdir1>0 1 0</fdir1>
            </ode>
          </friction>
        </surface>
      </collision>
      <visual name='WheelFR_link_visual'>
        <pose>0 0 0 0 -0 0</pose>
        <geometry>
          <mesh>
            <scale>0.1 0.1 0.1</scale>
            <uri>model://pepper_robot_description/pepper_robot/meshes/WheelFR.dae</uri>
          </mesh>
        </geometry>
      </visual>
      <gravity>1</gravity>
    </link>
    <plugin name='ignition::gazebo::systems::DiffDrive' filename='ignition-gazebo-diff-drive-system'>
      <left_joint>WheelFL</left_joint>
      <right_joint>WheelFR</right_joint>
      <back_joint>WheelB</back_joint>
      <wheel_separation>0.170</wheel_separation>
      <wheel_radius>0.07</wheel_radius>
    </plugin>
    <plugin name='ign_ros2_control::IgnitionROS2ControlPlugin' filename='ign_ros2_control-system'>
      <parameters>/root/ws/src/pepper_ign_moveit2/pepper_robot_moveit_config/config/controllers_effort.yaml</parameters>
    </plugin>
    <static>0</static>
    <plugin name='ignition::gazebo::systems::PosePublisher' filename='ignition-gazebo-pose-publisher-system'>
      <use_pose_vector_msg>1</use_pose_vector_msg>
      <publish_nested_model_pose>1</publish_nested_model_pose>
      <publish_link_pose>0</publish_link_pose>
      <publish_collision_pose>0</publish_collision_pose>
      <publish_visual_pose>0</publish_visual_pose>
    </plugin>
  </model>
</sdf>