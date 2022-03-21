#!/usr/bin/env python
# coding: utf-8
import rospy
from geometry_msgs.msg import PoseStamped, Quaternion
from db_service_server import create_connection
from collision_object import add_box_gripper, attach_box, detach_box, remove_box, add_box_on_table, remove_box_from_table
from std_msgs.msg import Bool
from moveit_commander import MoveGroupCommander
from tf.transformations import quaternion_from_euler

def delete_entry_from_db(db_path, table_name, raw_id):
    """ Deletes entry according to raw_id from
        param: table_name
        return: successful operation
    """
    db_connect = create_connection(db_path)
    with db_connect:
        db_cursor = db_connect.cursor()
        query = "DELETE FROM %s WHERE id=?" % table_name
        db_cursor.execute(query, (raw_id,))
        db_connect.commit()
        return rospy.loginfo('-----Entry deleted successfully from %s-----'%table_name)

def add_entry_to_db(db_path, table_name, raw_id, table_id, order_time):
    """ Adds entry according to table_name
        
        return: successful operation
    """
    db_connect = create_connection(db_path)
    with db_connect:
        db_cursor = db_connect.cursor()
        query = "INSERT INTO %s (id_from_order_db,order_for_table,oldtime,newtime) VALUES (? ,?, ?,DateTime('now'))" % table_name
        db_cursor.execute(query,(raw_id, table_id, order_time))
        db_connect.commit()
        return rospy.loginfo('-----Entry added successfully in %s-----'%table_name)

def pick_position(pose_array, arm_move_group):
    pick_pose = PoseStamped()
    pick_pose.header.frame_id = arm_move_group.get_planning_frame()
    pick_pose.pose.position.x = pose_array.target_pick_position_x
    pick_pose.pose.position.y = pose_array.target_pick_position_y
    pick_pose.pose.position.z = pose_array.target_pick_position_z
    pick_pose.pose.orientation.x = pose_array.target_pick_orientation_x
    pick_pose.pose.orientation.y = pose_array.target_pick_orientation_y
    pick_pose.pose.orientation.z = pose_array.target_pick_orientation_z
    pick_pose.pose.orientation.w = pose_array.target_pick_orientation_w

    return pick_pose

def place_position(pose_array, arm_move_group):
    pose = PoseStamped()
    pose.header.frame_id = arm_move_group.get_planning_frame()
    pose.pose.position.x = pose_array.target_place_position_x
    pose.pose.position.y = pose_array.target_place_position_y
    pose.pose.position.z = pose_array.target_place_position_z
    pose.pose.orientation.x = pose_array.target_place_orientation_x
    pose.pose.orientation.y = pose_array.target_place_orientation_y
    pose.pose.orientation.z = pose_array.target_place_orientation_z
    pose.pose.orientation.w = pose_array.target_place_orientation_w

    return pose

def pick_box(pose, robot_group, arm_move_group, gripper_move_group, eef_link, planning_scene,execution_flag):
    if execution_flag == True:
        ## Put box on picking table
        add_box_on_table(tableid='0',scene=planning_scene)

        ## Go to picking TOP position
        arm_move_group.set_start_state(robot_group.get_current_state())
        arm_move_group.set_pose_target(pose, eef_link)
        arm_move_group.go(wait=False)
        rospy.loginfo('---picking TOP pose---')
        rospy.sleep(2)

        ## Open gripper_move_group
        gripper_move_group.set_named_target("open")
        gripper_move_group.go(wait=False)
        rospy.sleep(1)
        rospy.loginfo(execution_flag)
    if execution_flag == True:
        ## Go down in z direction to pick the box
        arm_move_group.set_start_state(robot_group.get_current_state())
        pose.pose.position.z = pose.pose.position.z - 0.66
        arm_move_group.set_pose_target(pose, eef_link)
        arm_move_group.go(wait=False)
        rospy.loginfo('---going down to pick---')
        rospy.loginfo(execution_flag)
        rospy.sleep(2)
    if execution_flag == True:
        ## Close gripper_move_group
        gripper_move_group.set_named_target("close")
        gripper_move_group.go(wait=False)
        rospy.sleep(1)

        remove_box_from_table(box_name='0', scene=planning_scene)

        ## box to gripper_move_group
        add_box_gripper(scene=planning_scene)
        attach_box(box_name='box', robot=robot_group, scene=planning_scene, eef_link=eef_link)
        rospy.loginfo(execution_flag)
    if execution_flag == True:
        ## Go up in z direction after picking the box
        arm_move_group.set_start_state(robot_group.get_current_state())
        pose.pose.position.z = pose.pose.position.z + 0.64
        arm_move_group.set_pose_target(pose, eef_link)
        arm_move_group.go(wait=False)
        rospy.loginfo('---going up after pick---')
        rospy.sleep(2)

        arm_move_group.clear_pose_targets()
        rospy.loginfo('---cleared all targets---')
        rospy.loginfo(execution_flag)

def place_box(pose, robot_group, arm_move_group, gripper_move_group, eef_link, planning_scene, table_name, execution_flag):
    if execution_flag == True:
        ## Go to placing TOP position
        arm_move_group.set_start_state(robot_group.get_current_state())
        arm_move_group.set_pose_target(pose, eef_link)
        arm_move_group.go(wait=False)
        rospy.loginfo('---placing TOP pose---')
        rospy.loginfo(execution_flag)
        rospy.sleep(4)
    if execution_flag == True:
        ## Go down in z direction to place the box
        arm_move_group.set_start_state(robot_group.get_current_state())
        pose.pose.position.z = pose.pose.position.z - 0.66
        arm_move_group.set_pose_target(pose, eef_link)
        arm_move_group.go(wait=False)
        rospy.loginfo('---going down to place---')
        rospy.loginfo(execution_flag)
        rospy.sleep(2)
    if execution_flag == True:
        ## Open gripper
        gripper_move_group.set_named_target("open")
        gripper_move_group.go()
        rospy.sleep(1)
        
        ## Remove box from gripper
        detach_box(box_name='box', scene=planning_scene, eef_link_name=eef_link)
        remove_box(box_name='box', scene=planning_scene)

        ## Place box on placing table
        add_box_on_table(table_name, planning_scene)
        rospy.loginfo(execution_flag)
        rospy.sleep(1)
    if execution_flag == True:
        ## Go up in z direction
        arm_move_group.set_start_state(robot_group.get_current_state())
        pose.pose.position.z = pose.pose.position.z + 0.64
        arm_move_group.set_pose_target(pose, eef_link)
        arm_move_group.go(wait=False)
        rospy.loginfo('---going up after place---')
        rospy.loginfo(execution_flag)
        rospy.sleep(2)

def go_to_safe_pose(robot, arm_move_group,eef_link):
    safe_pose = PoseStamped()
    safe_pose.header.frame_id = arm_move_group.get_planning_frame()
    ## Position for table 1
    safe_pose.pose.position.x = 0.0 
    safe_pose.pose.position.y = -2.0 
    safe_pose.pose.position.z = 1.78  
    q = quaternion_from_euler(0, 1.5707963, 1.5707963)
    safe_pose.pose.orientation = Quaternion(*q)

    arm_move_group.set_start_state(robot.get_current_state())
    arm_move_group.set_pose_target(safe_pose, eef_link)
    arm_move_group.go(joints=safe_pose,wait=False)
    rospy.sleep(2)
