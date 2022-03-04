#!/usr/bin/env python
# coding: utf-8
import sys
import rospy
from moveit_commander import MoveGroupCommander,PlanningSceneInterface, RobotCommander, roscpp_initialize
from std_msgs.msg import  Float64MultiArray
from geometry_msgs.msg import PoseStamped
from collision_object import add_box_gripper, attach_box, detach_box, remove_box, add_box_on_table, remove_box_from_table

topic_name = '/robot_line'
class get_order_from_publisher(object):
    def __init__(self):

        ## Initialize the move_group API
        self.move_group = roscpp_initialize(sys.argv)

        ## Instantiate a RobotCommander object.  This object is an interface to
        ## the robot as a whole including end effector.
        self.robot = RobotCommander()

        ## Initialize the move group for manipulator
        self.abb = MoveGroupCommander("arm")

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

        self.scene = PlanningSceneInterface()
        ## Instantiate Pose for placing position
        self.target_pose = PoseStamped()
        self.target_pose.header.frame_id = self.abb.get_planning_frame()

        ## Instantiate Pose for picking position
        self.target_pose_pick = PoseStamped()
        self.target_pose_pick.header.frame_id = self.abb.get_planning_frame()


    def register_subscriber(self,sub_to):
        
        ## Name of the subscriber topic should be same as publisher topic
        rospy.Subscriber(sub_to, Float64MultiArray, self.callback)
       
    def callback(self,data):
            self.target_pose_raw = data.data
            #print(target_pose_raw)

            ## Define placing position -> target_pose
            self.target_pose.pose.position.x = self.target_pose_raw[0]
            self.target_pose.pose.position.y = self.target_pose_raw[1]
            self.target_pose.pose.position.z = self.target_pose_raw[2]
            self.target_pose.pose.orientation.x = self.target_pose_raw[3]
            self.target_pose.pose.orientation.y = self.target_pose_raw[4]
            self.target_pose.pose.orientation.z = self.target_pose_raw[5]
            self.target_pose.pose.orientation.w = self.target_pose_raw[6]
            #print('Picking position: %s' %target_pose)
            
            ## Define picking position -> target_pose_pick
            self.target_pose_pick.pose.position.x = self.target_pose_raw[7]
            self.target_pose_pick.pose.position.y = self.target_pose_raw[8]
            self.target_pose_pick.pose.position.z = self.target_pose_raw[9]
            self.target_pose_pick.pose.orientation.x = self.target_pose_raw[10]
            self.target_pose_pick.pose.orientation.y = self.target_pose_raw[11]
            self.target_pose_pick.pose.orientation.z = self.target_pose_raw[12]
            self.target_pose_pick.pose.orientation.w = self.target_pose_raw[13]
            #print('Placing position: %s' %target_pose_pick)

            tableid = str(self.target_pose_raw[14])
            print("Order for table number: %s" %tableid)

            ## Put box on picking table
            add_box_on_table(tableid='0',scene=self.scene)

            ## Go to placing picking TOP position
            self.abb.set_start_state(self.robot.get_current_state())
            self.abb.set_pose_target(self.target_pose_pick, self.end_effector_link)
            self.abb.go()
            rospy.sleep(2)

            ## Open gripper
            self.gripper.set_named_target("open")
            self.gripper.go()
            rospy.sleep(1)
            
            ## Go down in z direction to pick the box
            self.abb.set_start_state(self.robot.get_current_state())
            self.target_pose_pick.pose.position.z = self.target_pose_pick.pose.position.z - 0.66
            self.abb.set_pose_target(self.target_pose_pick, self.end_effector_link)
            self.abb.go()
            rospy.sleep(2)

            ## Close gripper
            self.gripper.set_named_target("close")
            self.gripper.go()
            rospy.sleep(1)

            remove_box_from_table(box_name='0',scene=self.scene)

            ## box to gripper
            add_box_gripper(self.scene)
            attach_box(box_name='box',robot=self.robot,scene=self.scene,eef_link=self.end_effector_link)

            ## Go up in z direction after picking the box
            self.abb.set_start_state(self.robot.get_current_state())
            self.target_pose_pick.pose.position.z = self.target_pose_pick.pose.position.z + 0.64
            self.abb.set_pose_target(self.target_pose_pick, self.end_effector_link)
            self.abb.go()
            rospy.sleep(2)
            
            ## Go to placing TOP position
            self.abb.set_start_state(self.robot.get_current_state())
            self.abb.set_pose_target(self.target_pose, self.end_effector_link)
            self.abb.go()
            rospy.sleep(2)

            ## Go down in z direction to place the box
            self.abb.set_start_state(self.robot.get_current_state())
            self.target_pose.pose.position.z = self.target_pose.pose.position.z - 0.66
            self.abb.set_pose_target(self.target_pose, self.end_effector_link)
            self.abb.go()
            rospy.sleep(2)

            ## Open gripper
            self.gripper.set_named_target("open")
            self.gripper.go()
            rospy.sleep(1)
            
            ## Remove box from gripper
            detach_box(box_name='box',scene=self.scene,eef_link_name=self.end_effector_link)
            remove_box(box_name='box',scene=self.scene)

            ## Place box on placing table
            add_box_on_table(tableid,self.scene)
            rospy.sleep(1)

            ## Go up in z direction
            self.abb.set_start_state(self.robot.get_current_state())
            self.target_pose.pose.position.z = self.target_pose.pose.position.z + 0.64
            self.abb.set_pose_target(self.target_pose,self.end_effector_link)
            self.abb.go()
            rospy.sleep(2)

            remove_box_from_table(tableid,self.scene)
            rospy.sleep(1)
    

if __name__ == '__main__':
    try:
        rospy.init_node('order_receiver', anonymous=True)
         ## spin() simply keeps python from exiting until this node is stopped
        rospy.spin()
        start = get_order_from_publisher()
        start.register_subscriber(topic_name)
    except rospy.ROSInterruptException:
        pass