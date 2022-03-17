#!/usr/bin/env python
# coding: utf-8
import sys
import os
import rospy
from moveit_commander import MoveGroupCommander,PlanningSceneInterface, RobotCommander, roscpp_initialize
from std_msgs.msg import Bool
from geometry_msgs.msg import PoseStamped
from collision_object import add_box_gripper, attach_box, detach_box, remove_box, add_box_on_table, remove_box_from_table

def get_order():
    
    abb.allow_replanning(True)
    abb.set_planning_time(5)
    abb.set_num_planning_attempts(10)
    abb.set_goal_position_tolerance(0.01)
    abb.set_goal_orientation_tolerance(0.01)
    abb.set_goal_tolerance(0.01)
    abb.set_max_velocity_scaling_factor(1.0)
    abb.set_max_acceleration_scaling_factor(1.0)
    ## Name of the subscriber topic should be same as publisher topic
    rospy.Subscriber("/stop_motion", Bool, callback)
    ## spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

def callback(data):
    if data.data == True:
        print('-----inside callback--------')
        abb.stop()
        #current_pose = robot.get_current_state()
        #abb.set_start_state(robot.get_current_state())
        #abb.set_pose_target(current_pose,end_effector_link)
        #abb.go(wait=False)
        #os.system('rosnode kill main_order_receiver')
        print('-------robot stop------')
        rospy.spin()
    else:
        print('---false received----')


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
        while not rospy.is_shutdown():
            get_order()
            r.sleep()

    except rospy.ROSInterruptException:
        pass