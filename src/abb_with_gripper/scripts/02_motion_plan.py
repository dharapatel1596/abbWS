#!/usr/bin/env python
# coding: utf-8
import rospy
from time import sleep
import moveit_commander
from moveit_commander import MoveGroupCommander,PlanningSceneInterface
import db

if __name__ == '__main__':
    rospy.init_node("abb_motion_plan_py")

    abb = MoveGroupCommander("arm")

    abb.set_named_target("down")
    abb.go()
    sleep(2)

    abb.allow_replanning(True)
    abb.set_planning_time(5)

    abb.set_num_planning_attempts(10)

    abb.set_goal_position_tolerance(0.01)

    abb.set_goal_orientation_tolerance(0.01)

    abb.set_goal_tolerance(0.01)

    abb.set_max_velocity_scaling_factor(1.0)

    abb.set_max_acceleration_scaling_factor(1.0)
    
    abb.set_joint_value_target(db.target_jointsdown)
    abb.go()
    sleep(2)

    abb.set_joint_value_target(db.target_joints)
    abb.go()
    sleep(2)
      
    moveit_commander.roscpp_shutdown()