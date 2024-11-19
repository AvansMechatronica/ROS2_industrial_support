<?xml version="1.0"?>
<launch>


  <node name="gear_part_0_spawner" pkg="gazebo_ros" type="spawn_model" output="screen"
    args="-x -3.25 -y 2.5 -z 1.5 -sdf -model gear_part_0 -file $(find casus_support)/meshes/part/gear_part/model.sdf"/>

  <node name="gasket_part_0_spawner" pkg="gazebo_ros" type="spawn_model" output="screen"
    args="-x -2.75 -y 2.5 -z 1.5 -sdf -model gasket_part_0 -file $(find casus_support)/meshes/part/gasket_part/model.sdf"/>



</launch>
