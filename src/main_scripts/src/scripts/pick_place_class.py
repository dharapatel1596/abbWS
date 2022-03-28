#!/usr/bin/env python
# coding: utf-8
import sys
import rospy
from geometry_msgs.msg import PoseStamped
from moveit_commander import MoveGroupCommander,PlanningSceneInterface, RobotCommander, roscpp_initialize
from collision_object import add_box_gripper, attach_box, detach_box, remove_box, add_box_on_table, remove_box_from_table

class PickPlaceClass(object):

    def __init__(self):

        ## Initialize the move_group API
        self.move_group = roscpp_initialize(sys.argv)

        ## Instantiate a RobotCommander object.  This object is an interface to
        ## the robot as a whole including end effector.
        self.robot = RobotCommander()

        ## Initialize the move group for manipulator
        self.abb = MoveGroupCommander("arm")

        ## Configure arm variables
        self.abb.allow_replanning(True)
        self.abb.set_planning_time(5)
        self.abb.set_num_planning_attempts(10)
        self.abb.set_goal_position_tolerance(0.01)
        self.abb.set_goal_orientation_tolerance(0.01)
        self.abb.set_goal_tolerance(0.01)
        self.abb.set_max_velocity_scaling_factor(1.0)
        self.abb.set_max_acceleration_scaling_factor(1.0)
        
        ## Initialize the move group for the gripper
        self.gripper = MoveGroupCommander("gripper")
        
        ## Get the name of the end-effector link
        self.end_effector_link = self.abb.get_end_effector_link()

        ## Instantiate Planning scene for RVIZ
        self.scene = PlanningSceneInterface()

        ## Instantiate Pose for placing position
        self.place_pose = PoseStamped()
        self.place_pose.header.frame_id = self.abb.get_planning_frame()

        ## Instantiate Pose for picking position
        self.pick_pose = PoseStamped()
        self.pick_pose.header.frame_id = self.abb.get_planning_frame()
    

    def pick_box(self,pose):

        ## Put box on picking table
        add_box_on_table(tableid='0',scene=self.scene)

        ## Go to picking TOP position
        self.abb.set_start_state(self.robot.get_current_state())
        self.abb.set_pose_target(pose, self.end_effector_link)
        self.abb.go(wait=False)
        rospy.loginfo('---after picking TOP pose---')
        rospy.sleep(2)

        ## Open self.gripper
        self.gripper.set_named_target("open")
        self.gripper.go(wait=False)
        rospy.sleep(1)
        
        ## Go down in z direction to pick the box
        self.abb.set_start_state(self.robot.get_current_state())
        pose.pose.position.z = pose.pose.position.z - 0.66
        self.abb.set_pose_target(pose, self.end_effector_link)
        self.abb.go(wait=False)
        rospy.loginfo('---reched down to pick---')
        rospy.sleep(2)

        ## Close self.gripper
        self.gripper.set_named_target("close")
        self.gripper.go(wait=False)
        rospy.sleep(1)

        remove_box_from_table(box_name='0',scene=self.scene)

        ## box to self.gripper
        add_box_gripper(self.scene)
        attach_box(box_name='box',robot=self.robot,scene=self.scene,eef_link=self.end_effector_link)

        ## Go up in z direction after picking the box
        self.abb.set_start_state(self.robot.get_current_state())
        pose.pose.position.z = pose.pose.position.z + 0.64
        self.abb.set_pose_target(pose, self.end_effector_link)
        self.abb.go(wait=False)
        rospy.loginfo('---gone up after pick---')
        rospy.sleep(2)

        ## Clear all pose from MoveIT
        self.abb.clear_pose_targets()
        rospy.loginfo('---cleared all targets---')

    def place_box(self,pose,table_name):

        ## Go to placing TOP position
        self.abb.set_start_state(self.robot.get_current_state())
        self.abb.set_pose_target(pose, self.end_effector_link)
        self.abb.go(wait=False)
        rospy.loginfo('---after placing TOP pose---')
        rospy.sleep(4)

        ## Go down in z direction to place the box
        self.abb.set_start_state(self.robot.get_current_state())
        pose.pose.position.z = pose.pose.position.z - 0.66
        self.abb.set_pose_target(pose, self.end_effector_link)
        self.abb.go(wait=False)
        rospy.loginfo('---gone down to place---')
        rospy.sleep(2)

        ## Open gripper
        self.gripper.set_named_target("open")
        self.gripper.go()
        rospy.sleep(1)
        
        ## Remove box from gripper
        detach_box(box_name='box', scene=self.scene, eef_link_name=self.end_effector_link)
        remove_box(box_name='box',scene=self.scene)

        ## Place box on placing table
        add_box_on_table(table_name,self.scene)
        rospy.sleep(1)

        ## Go up in z direction
        self.abb.set_start_state(self.robot.get_current_state())
        pose.pose.position.z = pose.pose.position.z + 0.64
        self.abb.set_pose_target(pose,self.end_effector_link)
        self.abb.go(wait=False)
        rospy.loginfo('---after placing pose---')
        rospy.sleep(2)

        ## Clear all pose from MoveIT
        self.abb.clear_pose_targets()
        rospy.loginfo('---cleared all targets---')

    def home_position(self):
        self.abb.set_named_target("down")
        self.abb.go(wait=False)
        rospy.sleep(2)
