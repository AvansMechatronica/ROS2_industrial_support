<?xml version="1.0"?>
<launch>
  <arg name="robot1_prefix" value="robot1_"/>
  <arg name="robot1_type" value="ur10"/>
  <arg name="vacuum_gripper1_prefix" value="vacuum_gripper1_"/>
  <arg name="gripper1_plugin_name" value="gripper1"/>


  <!-- Parameters and nodes in the namespace of robot1. -->
  <group ns="/robot1">
    <param name="tf_prefix" value="robot1"/>

    <param name="/robot1/$(arg robot1_prefix)description"
       command="$(find xacro)/xacro '$(find casus_support)/urdf/robot_system/robot_system.xacro' robot_type:=$(arg robot1_type) robot_prefix:=$(arg robot1_prefix) vacuum_gripper_prefix:=$(arg vacuum_gripper1_prefix) robot_param:=/robot1/$(arg robot1_prefix)description gripper_plugin_name:=$(arg gripper1_plugin_name)"/>

    <!-- Load the controllers for robot1. -->
    <rosparam file="$(find casus_gazebo)/config/r1_joint_state_controller.yaml" command="load"/>
    <rosparam file="$(find casus_gazebo)/config/robot1_controller.yaml" command="load"/>

    <!-- Spawn robot1, its state publisher and controller. -->
    <node name="robot1_spawner" pkg="gazebo_ros" type="spawn_model"
      args="-x -4 -y -1 -z 0.95 -Y -1.56 -urdf -model robot1 -param robot1_description -J robot1_elbow_joint 1.57 -J robot1_shoulder_lift_joint -1.57 -J robot1_shoulder_pan_joint 1.24 -J robot1_wrist_1_joint -1.57 -J robot1_wrist_2_joint -1.57" respawn="false" output="screen">
    </node>

    <node name="robot1_controller_spawner" pkg="controller_manager" type="spawner"
      args="r1_joint_state_controller robot1_controller">
    </node>
  </group>

</launch>
