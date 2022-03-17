#!/usr/bin/env python
# coding: utf-8
import rospy
from time import sleep
#import moveit_commander
from moveit_commander import MoveGroupCommander,PlanningSceneInterface, RobotCommander
#import db
from geometry_msgs.msg import Pose, PoseStamped, Quaternion
from tf.transformations import quaternion_from_euler

if __name__ == '__main__':
    rospy.init_node("abb_motion_plan_py")
    robot = RobotCommander()
    abb = MoveGroupCommander("arm")

    # abb.set_named_target("down")
    # abb.go()
    # sleep(2)

    abb.allow_replanning(True)
    abb.set_planning_time(5)

    abb.set_num_planning_attempts(10)

    abb.set_goal_position_tolerance(0.01)

    abb.set_goal_orientation_tolerance(0.01)

    abb.set_goal_tolerance(0.01)

    abb.set_max_velocity_scaling_factor(1.0)

    abb.set_max_acceleration_scaling_factor(1.0)
    end_effector_link = abb.get_end_effector_link()
    start_pose = PoseStamped()
    start_pose.header.frame_id = abb.get_planning_frame()
    ## Position for table 1
    start_pose.pose.position.x = 0.0 
    start_pose.pose.position.y = 2.0 
    start_pose.pose.position.z = 1.78  
    # start_pose.pose.orientation.x = -0.5
    # start_pose.pose.orientation.y = 0.5
    # start_pose.pose.orientation.z = 0.5
    # start_pose.pose.orientation.w = 0.5
    q = quaternion_from_euler(0, 1.5707963, 1.5707963) #zyx
    start_pose.pose.orientation = Quaternion(*q)

    while 1:

        #print('start pose')
        abb.set_start_state(robot.get_current_state())
        abb.set_pose_target(start_pose, end_effector_link)
        #abb_plan_path(pose=start_pose)
        abb.go(wait=False)
        rospy.sleep(1)
        print('table finished')
        rospy.sleep(5)
        

        abb.set_named_target("down")
        abb.go(wait=False)
        rospy.sleep(1)
        print('down finish')
        rospy.sleep(5)
        
      
    #moveit_commander.roscpp_shutdown()