#!/usr/bin/env python
# coding: utf-8
import sys
import rospy
from moveit_commander import MoveGroupCommander,PlanningSceneInterface, RobotCommander, roscpp_initialize
from std_msgs.msg import  Float64MultiArray
from geometry_msgs.msg import PoseStamped
from collision_object import add_box_gripper, attach_box, detach_box, remove_box, add_box_on_table, remove_box_from_table

def get_order():
    rospy.init_node('listener', anonymous=True)
    ## Name of the subscriber topic should be same as publisher topic
    rospy.Subscriber("/robot_line", Float64MultiArray, callback)
    abb.allow_replanning(True)
    abb.set_planning_time(5)
    abb.set_num_planning_attempts(10)
    abb.set_goal_position_tolerance(0.01)
    abb.set_goal_orientation_tolerance(0.01)
    abb.set_goal_tolerance(0.01)
    abb.set_max_velocity_scaling_factor(1.0)
    abb.set_max_acceleration_scaling_factor(1.0)
    ## spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

def callback(data):
        target_pose_raw = data.data
        #print(target_pose_raw)

        ## Define placing position -> target_pose
        target_pose.pose.position.x = target_pose_raw[0]
        target_pose.pose.position.y = target_pose_raw[1]
        target_pose.pose.position.z = target_pose_raw[2]
        target_pose.pose.orientation.x = target_pose_raw[3]
        target_pose.pose.orientation.y = target_pose_raw[4]
        target_pose.pose.orientation.z = target_pose_raw[5]
        target_pose.pose.orientation.w = target_pose_raw[6]
        #print('Picking position: %s' %target_pose)
        
        ## Define picking position -> target_pose_pick
        target_pose_pick.pose.position.x = target_pose_raw[7]
        target_pose_pick.pose.position.y = target_pose_raw[8]
        target_pose_pick.pose.position.z = target_pose_raw[9]
        target_pose_pick.pose.orientation.x = target_pose_raw[10]
        target_pose_pick.pose.orientation.y = target_pose_raw[11]
        target_pose_pick.pose.orientation.z = target_pose_raw[12]
        target_pose_pick.pose.orientation.w = target_pose_raw[13]
        #print('Placing position: %s' %target_pose_pick)

        tableid = str(target_pose_raw[14])
        print("Order for table number: %s" %tableid)

        ## Put box on picking table
        add_box_on_table(tableid='0',scene=scene)

        ## Go to placing picking TOP position
        abb.set_start_state(robot.get_current_state())
        abb.set_pose_target(target_pose_pick, end_effector_link)
        abb.go()
        rospy.sleep(2)

        ## Open gripper
        gripper.set_named_target("open")
        gripper.go()
        rospy.sleep(1)
        
        ## Go down in z direction to pick the box
        abb.set_start_state(robot.get_current_state())
        target_pose_pick.pose.position.z = target_pose_pick.pose.position.z - 0.66
        abb.set_pose_target(target_pose_pick, end_effector_link)
        abb.go()
        rospy.sleep(2)

        ## Close gripper
        gripper.set_named_target("close")
        gripper.go()
        rospy.sleep(1)

        remove_box_from_table(box_name='0',scene=scene)

        ## box to gripper
        add_box_gripper(scene)
        attach_box(box_name='box',robot=robot,scene=scene,eef_link=end_effector_link)

        ## Go up in z direction after picking the box
        abb.set_start_state(robot.get_current_state())
        target_pose_pick.pose.position.z = target_pose_pick.pose.position.z + 0.64
        abb.set_pose_target(target_pose_pick, end_effector_link)
        abb.go()
        rospy.sleep(2)
        
        ## Go to placing TOP position
        abb.set_start_state(robot.get_current_state())
        abb.set_pose_target(target_pose, end_effector_link)
        abb.go()
        rospy.sleep(2)

        ## Go down in z direction to place the box
        abb.set_start_state(robot.get_current_state())
        target_pose.pose.position.z = target_pose.pose.position.z - 0.66
        abb.set_pose_target(target_pose, end_effector_link)
        abb.go()
        rospy.sleep(2)

        ## Open gripper
        gripper.set_named_target("open")
        gripper.go()
        rospy.sleep(1)
        
        ## Remove box from gripper
        detach_box(box_name='box',scene=scene,eef_link_name=end_effector_link)
        remove_box(box_name='box',scene=scene)

        ## Place box on placing table
        add_box_on_table(tableid,scene)
        rospy.sleep(1)

        ## Go up in z direction
        abb.set_start_state(robot.get_current_state())
        target_pose.pose.position.z = target_pose.pose.position.z + 0.64
        abb.set_pose_target(target_pose, end_effector_link)
        abb.go()
        rospy.sleep(2)

        remove_box_from_table(tableid,scene)
        rospy.sleep(1)
    

if __name__ == '__main__':

    ## Initialize the move_group API
    roscpp_initialize(sys.argv)

    ## Instantiate a RobotCommander object.  This object is an interface to
    ## the robot as a whole including end effector.
    robot = RobotCommander()

    ## Initialize the move group for manipulator
    abb = MoveGroupCommander("arm")
    
    ## Initialize the move group for the gripper
    gripper = MoveGroupCommander("gripper")
    
    ## Get the name of the end-effector link
    end_effector_link = abb.get_end_effector_link()

    scene = PlanningSceneInterface()
    ## Instantiate Pose for placing position
    target_pose = PoseStamped()
    target_pose.header.frame_id = abb.get_planning_frame()

    ## Instantiate Pose for picking position
    target_pose_pick = PoseStamped()
    target_pose_pick.header.frame_id = abb.get_planning_frame()

    ## Start the subscriber
    get_order()