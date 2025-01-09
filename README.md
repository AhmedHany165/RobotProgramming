# Assessment 1


## 1. using this command to run the world in gazebo
```bash
ros2 launch limo_gazebosim limo_gazebo_diff.launch.py world:=src/cmp9767_tutorial/worlds/myworld.world
```

## 2. using this command to run navigation package

### 2.1 for running the defulat map
```bash 
ros2 launch limo_navigation limo_navigation.launch.py
```

### 2.2 for running my map
```bash 
ros2 launch limo_navigation limo_navigation.launch.py map:=src/cmp9767_tutorial/maps/my_map.yaml use_sim_time:=true
```

### 2.3 for running my map and my parameters
```bash 
ros2 launch limo_navigation limo_navigation.launch.py map:=src/cmp9767_tutorial/maps/my_map.yaml use_sim_time:=true params_file:=src/cmp9767_tutorial/params/nav2_params.yaml
```

## 3. using this command to run rqt gui
``` bash 
ros2 run rqt_gui rqt_gui
```
Go to Plugins/Configuration/Dynamic Reconfigure, find the local costmap to adjust its parameters.
Find the parameter for inflation_radius in the inflation_layer, change the value from 0.1 to 0.25. 

a saved map for my_world world is saved in maps folder as my_map 
    it has the map of this folder in addition to the red boxes.
    
## gfhfghfghs
 









ros2 launch limo_gazebosim limo_gazebo_diff.launch.py world:=src/cmp9767_tutorial/worlds/myworld3.world
ros2 launch limo_navigation limo_navigation.launch.py map:=src/cmp9767_tutorial/maps/my_map2.yaml use_sim_time:=true params_file:=src/cmp9767_tutorial/params/nav2_params.yaml
ros2 run cmp9767_tutorial demo_inspection2
ros2 run cmp9767_tutorial detector_3d
ros2 run cmp9767_tutorial counter_3d
ros2 topic echo /amcl_pose

