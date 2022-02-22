#!/usr/bin/env python
# coding: utf-8
import rospy
from time import sleep
import moveit_commander
from moveit_commander import MoveGroupCommander,PlanningSceneInterface
from std_msgs.msg import String, Int32, Float64MultiArray

def callback(data):
    target_joints = data.data
    print(target_joints)
    abb.set_named_target("down")
    abb.go()
    sleep(2)

    #abb.set_joint_value_target(target_joints)
    print('above go')
    abb.go(joints=target_joints, wait=False)
    sleep(2)
    print('afetr sleep')
    abb.stop()
    print('after stop')


def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/user_input", Float64MultiArray, callback)
    
    abb.allow_replanning(True)
    abb.set_planning_time(5)

    abb.set_num_planning_attempts(10)

    abb.set_goal_position_tolerance(0.01)

    abb.set_goal_orientation_tolerance(0.01)

    abb.set_goal_tolerance(0.01)

    abb.set_max_velocity_scaling_factor(1.0)

    abb.set_max_acceleration_scaling_factor(1.0)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
    

if __name__ == '__main__':
    abb = MoveGroupCommander("arm")
    listener()