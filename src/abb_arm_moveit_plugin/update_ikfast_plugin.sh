search_mode=OPTIMIZE_MAX_JOINT
srdf_filename=abb_irb6640_with_camera_gripper.srdf
robot_name_in_srdf=abb_irb6640_with_camera_gripper
moveit_config_pkg=abb_irb6640_with_camera_gripper_moveit_config
robot_name=abb_irb6640_with_camera_gripper
planning_group_name=arm
ikfast_plugin_pkg=abb_arm_moveit_plugin
base_link_name=base_link
eef_link_name=link_8
ikfast_output_path=/home/dhara/arm_ws/src/abb_arm_moveit_plugin/src/abb_irb6640_with_camera_gripper_arm_ikfast_solver.cpp

rosrun moveit_kinematics create_ikfast_moveit_plugin.py\
  --search_mode=$search_mode\
  --srdf_filename=$srdf_filename\
  --robot_name_in_srdf=$robot_name_in_srdf\
  --moveit_config_pkg=$moveit_config_pkg\
  $robot_name\
  $planning_group_name\
  $ikfast_plugin_pkg\
  $base_link_name\
  $eef_link_name\
  $ikfast_output_path
