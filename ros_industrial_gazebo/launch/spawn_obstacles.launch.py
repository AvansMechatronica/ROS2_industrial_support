<?xml version="1.0"?>
<launch>
  <arg name="pallettruck_prefix" value="pallettruck_"/>
  <arg name="pallet_prefix" value="pallet_"/>
  <arg name="parent" value="world"/>


  <!-- Parameters and nodes in the global namespace. -->
<!--
  <param name="$(arg pallettruck_prefix)description"
    command="$(find xacro)/xacro '$(find casus_support)/urdf/pallettruck/pallettruck.xacro' pallettruck_prefix:=$(arg pallettruck_prefix) pallettruck_parent:=$(arg parent) x:=-5 y:=2 Y:=1.57"/>

  <node name="$(arg pallettruck_prefix)spawner" pkg="gazebo_ros" type="spawn_model" output="screen"
    args="-urdf -model $(arg pallettruck_prefix) -param $(arg pallettruck_prefix)description"/>
-->
  <!-- Parameters and nodes in the global namespace. -->
<!--
  <param name="$(arg pallet_prefix)description"
    command="$(find xacro)/xacro '$(find casus_support)/urdf/pallet/pallet.xacro' pallet_prefix:=$(arg pallet_prefix) pallet_parent:=$(arg parent) x:=-1.5 y:=1 "/>

  <node name="$(arg pallet_prefix)spawner" pkg="gazebo_ros" type="spawn_model" output="screen"
    args="-urdf -model $(arg pallet_prefix) -param $(arg pallet_prefix)description"/>
-->

</launch>
