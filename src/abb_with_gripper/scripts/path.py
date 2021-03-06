#!/usr/bin/env python
# coding: utf-8

import rospy
import sys
import numpy as np
import moveit_commander
from copy import deepcopy
import geometry_msgs.msg
import moveit_msgs.msg
from std_msgs.msg import Header
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
from tf.transformations import quaternion_from_euler
from geometry_msgs.msg import Pose, PoseStamped, Quaternion


class MoveItCartesianPath:
    def __init__(self):
        rospy.init_node("moveit_cartesian_path", anonymous=False)

        rospy.loginfo("Starting node moveit_cartesian_path")

        rospy.on_shutdown(self.cleanup)

        # Initialize the move_group API
        moveit_commander.roscpp_initialize(sys.argv)

        # Initialize the move group for the ur5_arm
        self.arm = moveit_commander.MoveGroupCommander('arm')

        # Get the name of the end-effector link
        end_effector_link = self.arm.get_end_effector_link()

        # Set the reference frame for pose targets
        reference_frame = "world"

        # Set the ur5_arm reference frame accordingly
        self.arm.set_pose_reference_frame(self.arm.get_planning_frame())

        # Allow replanning to increase the odds of a solution
        self.arm.allow_replanning(True)

        # Allow some leeway in position (meters) and orientation (radians)
        self.arm.set_goal_position_tolerance(0.01)
        self.arm.set_goal_orientation_tolerance(0.1)

        # Get the current pose so we can add it as a waypoint
        #start_pose = self.arm.get_current_pose(end_effector_link).pose

        ## Position for table 1
        start_pose = PoseStamped()
        start_pose.header.frame_id = self.arm.get_planning_frame()
        start_pose.pose.position.x = 0.0 
        start_pose.pose.position.y = 2.0 
        start_pose.pose.position.z = 1.78  
        q = quaternion_from_euler(0, 1.5707963, 1.5707963) #zyx
        start_pose.pose.orientation = Quaternion(*q)
        self.arm.set_start_state_to_current_state()
        self.arm.set_pose_target(start_pose, end_effector_link)
        self.arm.go()
        rospy.sleep(2)
        print('PTP')
        self.arm.set_start_state_to_current_state()
        self.arm.set_named_target('down')
        self.arm.go()
        rospy.sleep(2)

        print('LIN')
        # Initialize the waypoints list
        waypoints = []
        scale = 1.0
        wpose = self.arm.get_current_pose().pose
        wpose.position.z = 1.6  # First move up (z)
        wpose.position.x = 0.0
        wpose.position.y = 2.0
        #wpose.position.y += scale * 0.2  # and sideways (y)
        #waypoints.append(deepcopy(wpose))

        #wpose.position.x -= scale * 0.1  # Second move forward(+)/backwards(-) in (x)
        waypoints.append(deepcopy(wpose))

        #wpose.position.y -= scale * 0.1  # Third move sideways (y)
        #waypoints.append(deepcopy(wpose))

        # if np.sqrt((wpose.position.x-start_pose.position.x)**2+(wpose.position.x-start_pose.position.x)**2 \
        #     +(wpose.position.x-start_pose.position.x)**2)<0.1:
        #     rospy.loginfo("Warnig: target position overlaps with the initial position!")

        # self.arm.set_pose_target(wpose)

        # Set the internal state to the current state
        self.arm.set_start_state_to_current_state()

        # Plan the Cartesian path connecting the waypoints

        """moveit_commander.move_group.MoveGroupCommander.compute_cartesian_path(	 
                self, waypoints, eef_step, jump_threshold, avoid_collisios= True)
    
           Compute a sequence of waypoints that make the end-effector move in straight line segments that follow the 
           poses specified as waypoints. Configurations are computed for every eef_step meters; 
           The jump_threshold specifies the maximum distance in configuration space between consecutive points 
           in the resultingpath. The return value is a tuple: a fraction of how much of the path was followed, 
           the actual RobotTrajectory. 
        """
        plan, fraction = self.arm.compute_cartesian_path(waypoints, 0.01, 0.0, True)

        print(fraction)
        # plan = self.arm.plan()

        # If we have a complete plan, execute the trajectory
        if 1-fraction < 0.2:
            rospy.loginfo("Path computed successfully. Moving the arm.")
            num_pts = len(plan.joint_trajectory.points)
            rospy.loginfo("\n# intermediate waypoints = "+str(num_pts))
            self.arm.execute(plan)
            rospy.loginfo("Path execution complete.")
        else:
            rospy.loginfo("Path planning failed")

    def cleanup(self):
        rospy.loginfo("Stopping the robot")

        # Stop any current arm movement
        self.arm.stop()

        #Shut down MoveIt! cleanly
        rospy.loginfo("Shutting down Moveit!")
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)

if __name__ == "__main__":
    try:
        MoveItCartesianPath()
    except KeyboardInterrupt:
        print ("Shutting down MoveItCartesianPath node.")