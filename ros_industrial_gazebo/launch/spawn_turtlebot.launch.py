<?xml version="1.0"?>
<launch>
  <arg name="turtlebot_system" value="turtlebot_"/>
  <arg name="base"      value="$(optenv TURTLEBOT_BASE kobuki)"/>
  <arg name="stacks"    value="$(optenv TURTLEBOT_STACKS hexagons)"/>
  <arg name="3d_sensor" value="$(optenv TURTLEBOT_3D_SENSOR kinect)"/>

  <!-- Parameters and nodes for Turtlebot -->
    <param name="$(arg turtlebot_system)description"
      command="$(find xacro)/xacro '$(find turtlebot_description)/robots/$(arg base)_$(arg stacks)_$(arg 3d_sensor).urdf.xacro'"/>

    <!-- Spawn the turtlebot slightly above the floor level so that it is always spawned on the ground. -->
    <node name="$(arg turtlebot_system)spawner" pkg="gazebo_ros" type="spawn_model" output="screen"
      args="-x -1.5 -y -1 -z 0.1 -urdf -unpause -param $(arg turtlebot_system)description -model mobile_base">
    </node>

    <!-- Ensure that the TFs for Turtlebot are made available. -->
    <node pkg="robot_state_publisher" type="robot_state_publisher"  name="turtlebot_state_publisher">
      <param name="publish_frequency" type="double" value="50.0" />
      <remap from="robot_description" to="turtlebot_description"/>
    </node>
</launch>
