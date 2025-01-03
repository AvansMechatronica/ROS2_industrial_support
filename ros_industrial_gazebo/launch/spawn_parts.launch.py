<?xml version="1.0"?>
<launch>


  <node name="gear_part_0_spawner" pkg="gazebo_ros" type="spawn_model" output="screen"
    args="-x -3.2 -y -0.7 -z 1.5 -sdf -model gear_part_0 -file $(find casus_support)/meshes/part/gear_part/model.sdf"/>

  <node name="gasket_part_0_spawner" pkg="gazebo_ros" type="spawn_model" output="screen"
    args="-x -3.2 -y -0.3 -z 1.5 -sdf -model gasket_part_0 -file $(find casus_support)/meshes/part/gasket_part/model.sdf"/>

  <node name="pulley_part_0_spawner" pkg="gazebo_ros" type="spawn_model" output="screen"
    args="-x -2.8 -y -0.7 -z 1.5 -sdf -model pulley_part_0 -file $(find casus_support)/meshes/part/pulley_part/model.sdf"/>

  <node name="piston_rod_part_0_spawner" pkg="gazebo_ros" type="spawn_model" output="screen"
    args="-x -2.8 -y -0.3 -z 1.5 -sdf -model piston_rod_part_0 -file $(find casus_support)/meshes/part/piston_rod_part/model.sdf"/>


</launch>
