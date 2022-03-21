#!/usr/bin/env python
# coding: utf-8
import sys
import os
import rospy
from moveit_commander import MoveGroupCommander,PlanningSceneInterface, RobotCommander, roscpp_initialize
from std_msgs.msg import Bool
from geometry_msgs.msg import PoseStamped
from collision_object import add_box_gripper, attach_box, detach_box, remove_box, add_box_on_table, remove_box_from_table

# def get_order():
    
#     abb.allow_replanning(True)
#     abb.set_planning_time(5)
#     abb.set_num_planning_attempts(10)
#     abb.set_goal_position_tolerance(0.01)
#     abb.set_goal_orientation_tolerance(0.01)
#     abb.set_goal_tolerance(0.01)
#     abb.set_max_velocity_scaling_factor(1.0)
#     abb.set_max_acceleration_scaling_factor(1.0)
#     ## Name of the subscriber topic should be same as publisher topic
#     rospy.Subscriber("/stop_motion", Bool, callback)
#     ## spin() simply keeps python from exiting until this node is stopped
#     rospy.spin()

class sensors(object):
    def __init__(self):
        self.execution_flag = None
    
    def pick_box(self,pose, robot_group, arm_move_group, gripper_move_group, eef_link, planning_scene,exec_flag):
        if exec_flag == True:
            if self.execution_flag == True:
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
                rospy.loginfo(self.execution_flag)
            if self.execution_flag == True:
                ## Go down in z direction to pick the box
                arm_move_group.set_start_state(robot_group.get_current_state())
                pose.pose.position.z = pose.pose.position.z - 0.66
                arm_move_group.set_pose_target(pose, eef_link)
                arm_move_group.go(wait=False)
                rospy.loginfo('---going down to pick---')
                rospy.loginfo(self.execution_flag)
                rospy.sleep(2)
            if self.execution_flag == True:
                ## Close gripper_move_group
                gripper_move_group.set_named_target("close")
                gripper_move_group.go(wait=False)
                rospy.sleep(1)

                remove_box_from_table(box_name='0', scene=planning_scene)

                ## box to gripper_move_group
                add_box_gripper(scene=planning_scene)
                attach_box(box_name='box', robot=robot_group, scene=planning_scene, eef_link=eef_link)
                rospy.loginfo(self.execution_flag)
            if self.execution_flag == True:
                ## Go up in z direction after picking the box
                arm_move_group.set_start_state(robot_group.get_current_state())
                pose.pose.position.z = pose.pose.position.z + 0.64
                arm_move_group.set_pose_target(pose, eef_link)
                arm_move_group.go(wait=False)
                rospy.loginfo('---going up after pick---')
                rospy.sleep(2)

                arm_move_group.clear_pose_targets()
                rospy.loginfo('---cleared all targets---')
                rospy.loginfo(self.execution_flag)

    def place_box(self,pose, robot_group, arm_move_group, gripper_move_group, eef_link, planning_scene, table_name,exec_flag):
        if exec_flag == True:
            if self.execution_flag == True:
                ## Go to placing TOP position
                arm_move_group.set_start_state(robot_group.get_current_state())
                arm_move_group.set_pose_target(pose, eef_link)
                arm_move_group.go(wait=False)
                rospy.loginfo('---placing TOP pose---')
                rospy.loginfo(self.execution_flag)
                rospy.sleep(4)
            if self.execution_flag == True:
                ## Go down in z direction to place the box
                arm_move_group.set_start_state(robot_group.get_current_state())
                pose.pose.position.z = pose.pose.position.z - 0.66
                arm_move_group.set_pose_target(pose, eef_link)
                arm_move_group.go(wait=False)
                rospy.loginfo('---going down to place---')
                rospy.loginfo(self.execution_flag)
                rospy.sleep(2)
            if self.execution_flag == True:
                ## Open gripper
                gripper_move_group.set_named_target("open")
                gripper_move_group.go()
                rospy.sleep(1)
                
                ## Remove box from gripper
                detach_box(box_name='box', scene=planning_scene, eef_link_name=eef_link)
                remove_box(box_name='box', scene=planning_scene)

                ## Place box on placing table
                add_box_on_table(table_name, planning_scene)
                rospy.loginfo(self.execution_flag)
                rospy.sleep(1)
            if self.execution_flag == True:
                ## Go up in z direction
                arm_move_group.set_start_state(robot_group.get_current_state())
                pose.pose.position.z = pose.pose.position.z + 0.64
                arm_move_group.set_pose_target(pose, eef_link)
                arm_move_group.go(wait=False)
                rospy.loginfo('---going up after place---')
                rospy.loginfo(self.execution_flag)
                rospy.sleep(2)

    def callback(self,data):

            self.execution_flag = not(data.data)
            #print('execute= %s'%execution_flag)
            if self.execution_flag == False:
                #rospy.loginfo('stop robot')
                abb.stop()
            #else:
                #self.main_process()
                
    def check_for_sensor(self):
            rospy.Subscriber("/stop_motion", Bool, self.callback)

if __name__ == '__main__':
    
    ## Initialize the move_group API
    roscpp_initialize(sys.argv)

    ## Instantiate a RobotCommander object.  This object is an interface to
    ## the robot as a whole including end effector.
    robot = RobotCommander()

    ## Initialize the move group for manipulator
    abb = MoveGroupCommander("arm")
    
    ## Initialize the move group for the gripper
    #gripper = MoveGroupCommander("gripper")
    
    ## Get the name of the end-effector link
    end_effector_link = abb.get_end_effector_link()

    #scene = PlanningSceneInterface()
    ## Instantiate Pose for placing position
    #target_pose = PoseStamped()
    #target_pose.header.frame_id = abb.get_planning_frame()

    ## Instantiate Pose for picking position
    #target_pose_pick = PoseStamped()
    #target_pose_pick.header.frame_id = abb.get_planning_frame()

    # Start the subscriber
    try:
        rospy.init_node('order_receiver', anonymous=True)
        r = rospy.Rate(20)
        check = sensors()
        check.execution_flag = True
        while not rospy.is_shutdown():
            check.check_for_sensor()
            r.sleep()

    except rospy.ROSInterruptException:
        pass