<?xml version="1.0"?>
<launch>

  <!-- these are the arguments you can pass this launch file, for example paused:=true -->
  <arg name="paused" default="true"/>
  <arg name="use_sim_time" default="true"/>
  <arg name="gui" default="true"/>
  <arg name="rviz" default = "false"/>
  <arg name="headless" default="false"/>
  <arg name="debug" default="false"/>
  <arg name="extra_gazebo_args" default="--verbose"/>

  <!-- We resume the logic in empty_world.launch, changing only the name of the world to be launched -->
  <include file="$(find gazebo_ros)/launch/empty_world.launch">
    <arg name="world_name" value="$(find casus_gazebo)/worlds/casus.world"/>
    <arg name="debug" value="$(arg debug)" />
    <arg name="gui" value="$(arg gui)" />
    <arg name="paused" value="$(arg paused)"/>
    <arg name="use_sim_time" value="$(arg use_sim_time)"/>
    <arg name="headless" value="$(arg headless)"/>
    <arg name="extra_gazebo_args" value="$(arg extra_gazebo_args)"/>
  </include>

  <!-- Load the URDF into the ROS Parameter Server -->
  <include file="$(find casus_support)/launch/load_casus.launch"/>

  <!-- Start move_group -->
  <include file="$(find casus_moveit_config)/launch/move_group.launch"/>

  <!-- Spawn the URDF objects into Gazebo -->
  <include file="$(find casus_gazebo)/launch/spawn_static_world_objects.launch"/>
  <include file="$(find casus_gazebo)/launch/spawn_robots.launch"/>
  <node pkg="casus_utilities" type="timed_roslaunch.sh" name="timed_roslaunch" output="screen"
    args="7 casus_gazebo spawn_turtlebot.launch" />

  <!-- Start the conveyor spawner node -->
  <node name="conveyor_spawner" pkg="casus_gazebo" type="conveyor_spawner_node" output="screen">
    <rosparam command="load" file="$(find casus_gazebo)/config/conveyor_objects.yaml"/>
    <remap from="/start_spawn" to="/spawn_object_once"/>
  </node>

  <node name="spawn_object_once" pkg="casus_utilities" type="spawn_object_once.py" output="screen"/>

  <!-- Velocity muxer and controller for turtlebot-->
  <node pkg="nodelet" type="nodelet" name="mobile_base_nodelet_manager" args="manager"/>
  <node pkg="nodelet" type="nodelet" name="cmd_vel_mux"
        args="load yocs_cmd_vel_mux/CmdVelMuxNodelet mobile_base_nodelet_manager">
    <param name="yaml_cfg_file" value="$(find casus_gazebo)/param/mux.yaml" />
    <remap from="cmd_vel_mux/output" to="mobile_base/commands/velocity"/>
  </node>

  <!-- Fake laser -->
  <node pkg="nodelet" type="nodelet" name="laserscan_nodelet_manager" args="manager"/>
  <node pkg="nodelet" type="nodelet" name="depthimage_to_laserscan"
        args="load depthimage_to_laserscan/DepthImageToLaserScanNodelet laserscan_nodelet_manager">
    <param name="scan_height" value="10"/>
    <param name="output_frame_id" value="camera_depth_frame"/>
    <param name="range_min" value="0.45"/>
    <remap from="image" to="/camera/depth/image_raw"/>
    <remap from="scan" to="/scan"/>
  </node>

  <!-- Combine joint state information from two robots. -->
  <node name="joint_state_publisher" pkg="joint_state_publisher" type="joint_state_publisher">
    <rosparam param="source_list">[/robot1/joint_states]</rosparam>
    <remap from="/joint_states" to="/combined_joint_states"/>
  </node>


  <!-- Start RVIZ with Gazebo if necessary -->
  <node if="$(arg rviz)" name="rviz" pkg="rviz" type="rviz" args="-d $(find casus_support)/config/casus.rviz"/>

  <node pkg="robot_state_publisher" type="robot_state_publisher"  name="robots_state_publisher">
    <param name="publish_frequency" type="double" value="50.0"/>
    <remap from="/joint_states" to="/combined_joint_states"/>
  </node>

  <node pkg="tf2_ros" type="static_transform_publisher" name="map_to_odom" args="-4.0 -0.2 0 0 0 0 1 map odom"/>
  <node pkg="tf2_ros" type="static_transform_publisher" name="map_to_world" args="0 0 0 0 0 0 1 map world"/>

</launch>
