#!/usr/bin/env python
# coding: utf-8
import sys
import rospy
import moveit_commander
from geometry_msgs.msg import Pose, PoseStamped, Quaternion
from shape_msgs.msg import SolidPrimitive
from moveit_msgs.msg import CollisionObject, ExecuteTrajectoryActionFeedback
from moveit_commander import MoveGroupCommander,PlanningSceneInterface,RobotCommander, PlanningScene
from tf.transformations import quaternion_from_euler

def move_to_pose(pos, orientation, frame_id="/world", moveType='PTP', vel_scal=1.0, acc_scal=1.0):
    rospy.loginfo('inside pose fun')
    abb = MoveGroupCommander("arm")
    pose = PoseStamped()
    pose.header.frame_id = frame_id
    pose.header.stamp = rospy.Time.now()
    pose.pose.position.x, pose.pose.position.y, pose.pose.position.z = pos
    if len(orientation) == 3:
        pose.pose.orientation.x, pose.pose.orientation.y, pose.pose.orientation.z, pose.pose.orientation.w = quaternion_from_euler(*orientation)
    elif len(orientation) == 4:
        pose.pose.orientation.x, pose.pose.orientation.y, pose.pose.orientation.z, pose.pose.orientation.w = orientation

    if moveType == 'PTP':
        # try-except is necessary to give argument for plan()
        try:
            plan = abb.plan(pose)
            if plan.joint_trajectory.points:
                abb.set_max_velocity_scaling_factor(vel_scal)
                abb.set_max_acceleration_scaling_factor(acc_scal)
                valid_plan = True
                return plan, pose, valid_plan
        except:
            rospy.logerr("Path planning failed. Check the target pose")
            plan = None
            valid_plan = False
            return plan, pose, valid_plan
    elif moveType == 'LIN':
        plan, fraction = abb.compute_cartesian_path([pose.pose], 0.01, 0.0, True)
        # If we have a complete plan, execute the trajectory
        if 1-fraction < 0.2:
            plan = abb.retime_trajectory(moveit_commander.RobotCommander().get_current_state(), 
                                       plan, 
                                       velocity_scaling_factor=vel_scal,
                                       acceleration_scaling_factor=acc_scal)

            valid_plan = True
            return plan, pose, valid_plan
        else:
            rospy.logerr("Path planning failed. Check the target pose")
            plan = None
            valid_plan = False
            return plan, pose, valid_plan
        

def move_group_python_interface_tutorial():
        # Initialize the move_group API
        moveit_commander.roscpp_initialize(sys.argv)
        # Initialize the ROS node
        rospy.init_node('moveit_demo', anonymous=True)
        robot = RobotCommander()
        scene = moveit_commander.PlanningSceneInterface()
        # Connect to the abb move group
        abb = MoveGroupCommander("arm")
        # Initialize the move group for the right gripper
        gripper = MoveGroupCommander("gripper")                         
        # Increase the planning time since constraint planning can take a while
        abb.set_planning_time(15)                
        # Allow replanning to increase the odds of a solution
        abb.allow_replanning(True)         
        # Allow some leeway in position(meters) and orientation (radians)
        abb.set_goal_position_tolerance(0.0001)
        abb.set_goal_orientation_tolerance(0.1)
        # Get the name of the end-effector link
        end_effector_link = abb.get_end_effector_link()

        #rospy.Subscriber('/execute_trajectory/feedback',ExecuteTrajectoryActionFeedback, callback)

        # Start in the "resting" configuration stored in the SRDF file
        abb.set_named_target("down") 
        abb.go()
        rospy.sleep(1)
        # Open the gripper
        gripper.set_named_target("open")
        #gripper.set_random_target()
        gripper.go()
        rospy.sleep(1)
        print('PTP')
        ##
        plan,start = move_to_pose(pos=[2,0,1.77], orientation=[0,1.5,0],moveType='PTP',vel_scal=1.0)
        abb.execute(plan)
        ##
        print('LIN')
        start.pose.position.z -= 0.7
        plan,next = move_to_pose(pos=[start.pose.position.x,start.pose.position.y,start.pose.position.z], 
                        orientation=[start.pose.orientation.x,start.pose.orientation.y,start.pose.orientation.z,start.pose.orientation.w],
                        moveType='LIN',vel_scal=0.8)
        abb.execute(plan)
        #
        print('PTP')
        next.pose.position.z += 0.7
        next_pos, pose = move_to_pose(pos=[next.pose.position.x,next.pose.position.y,next.pose.position.z], 
                        orientation=[next.pose.orientation.x,next.pose.orientation.y,next.pose.orientation.z,next.pose.orientation.w],
                        moveType='PTP', vel_scal=0.1)
        abb.execute(next_pos)

        # Shut down MoveIt cleanly
        moveit_commander.roscpp_shutdown()

if __name__ == '__main__':
    try:
        move_group_python_interface_tutorial()
    except rospy.ROSInterruptException:
        pass

        