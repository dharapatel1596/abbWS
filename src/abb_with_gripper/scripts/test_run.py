#!/usr/bin/env python
# coding: utf-8
from fileinput import close
import sys
import rospy
from math import pi
from time import sleep
import moveit_commander
from geometry_msgs.msg import Pose, PoseStamped, Quaternion
from moveit_commander import MoveGroupCommander,PlanningSceneInterface,RobotCommander
from tf.transformations import quaternion_from_euler



def move_group_python_interface_tutorial():
        # Initialize the move_group API
        moveit_commander.roscpp_initialize(sys.argv)

        # Initialize the ROS node
        rospy.init_node('moveit_demo', anonymous=True)
        
        robot = RobotCommander()

        # Connect to the abb move group
        abb = MoveGroupCommander("arm")
        
        # Initialize the move group for the right gripper
        gripper = MoveGroupCommander("gripper")
                                
        # Increase the planning time since contraint planning can take a while
        abb.set_planning_time(15)
                        
        # Allow replanning to increase the odds of a solution
        abb.allow_replanning(True)
        
        # Set the right arm reference frame
        #abb.set_pose_reference_frame("world")
                
        # Allow some leeway in position(meters) and orientation (radians)
        abb.set_goal_position_tolerance(0.05)
        abb.set_goal_orientation_tolerance(0.1)
        
        # Get the name of the end-effector link
        end_effector_link = abb.get_end_effector_link()
        #print(abb.get_current_pose())


        # Start in the "resting" configuration stored in the SRDF file
        abb.set_named_target("up")
         
        # # Plan and execute a trajectory to the goal configuration
        abb.go()
        rospy.sleep(1)
        
        # Open the gripper
        #gripper.set_named_target("open")
        gripper.set_random_target()
        gripper.go()
        rospy.sleep(1)

        start_pose = PoseStamped()
        start_pose.header.frame_id = abb.get_planning_frame()
        # Position for table 1
        start_pose.pose.position.x = 0.0 # 20 cm
        start_pose.pose.position.y = 1.80 # -11 cm
        start_pose.pose.position.z = 1.7725  # 60 cm
        # start_pose.pose.orientation.x = -0.5
        # start_pose.pose.orientation.y = 0.5
        # start_pose.pose.orientation.z = 0.5
        # start_pose.pose.orientation.w = 0.5
        q = quaternion_from_euler(0, 1.5707963, 1.5707963) #zyx
        start_pose.pose.orientation = Quaternion(*q)

        # Position for table 2
        # start_pose.pose.position.x = -1.0 # 20 cm
        # start_pose.pose.position.y = 1.5 # -11 cm
        # start_pose.pose.position.z = 1.7725  # 60 cm
        # # start_pose.pose.orientation.x = -0.5
        # # start_pose.pose.orientation.y = 0.5
        # # start_pose.pose.orientation.z = 0.5
        # # start_pose.pose.orientation.w = 0.5
        # q = quaternion_from_euler(0, 1.5707963, 1.5707963) #zyx
        # start_pose.pose.orientation = Quaternion(*q)

         # Position for table 0
        # start_pose.pose.position.x = 1.8 # 20 cm
        # start_pose.pose.position.y = 0.0 # -11 cm
        # start_pose.pose.position.z = 1.7725  # 60 cm
        # # start_pose.pose.orientation.x = 1.45743564202e-05
        # # start_pose.pose.orientation.y = 0.6
        # # #start_pose.pose.orientation.z = 0.5
        # # start_pose.pose.orientation.w = 0.8 
        # q = quaternion_from_euler(0, 1.5, 0) #zyx
        # start_pose.pose.orientation = Quaternion(*q)

        print (start_pose)
        # IK Fast
        #abb.set_position_target([start_pose.pose.position.x, start_pose.pose.position.y, start_pose.pose.position.z],
        #                       abb.get_end_effector_link())
        
        # KDL
        # abb.set_start_state(robot.get_current_state())
        # abb.set_pose_target(start_pose, end_effector_link)
        # abb.go()
        # rospy.sleep(2)
        

        # Shut down MoveIt cleanly
        moveit_commander.roscpp_shutdown()

if __name__ == '__main__':
    try:
        move_group_python_interface_tutorial()
    except rospy.ROSInterruptException:
        pass

        