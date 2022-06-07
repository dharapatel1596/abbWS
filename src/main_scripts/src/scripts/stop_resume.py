#!/usr/bin/env python
# coding: utf-8
import sys
import rospy
import moveit_commander
from geometry_msgs.msg import Pose, PoseStamped, Quaternion
from shape_msgs.msg import SolidPrimitive
from moveit_msgs.msg import CollisionObject
from moveit_commander import MoveGroupCommander,PlanningSceneInterface,RobotCommander, PlanningScene
from tf.transformations import quaternion_from_euler
from gazebo_msgs.msg import ModelState
        
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
        
        # Set the right arm reference frame
        #abb.set_pose_reference_frame("world")
                
        # Allow some leeway in position(meters) and orientation (radians)
        abb.set_goal_position_tolerance(0.05)
        abb.set_goal_orientation_tolerance(0.1)
        
        # Get the name of the end-effector link
        end_effector_link = abb.get_end_effector_link()
        #print(abb.get_current_pose())

         # Start in the "resting" configuration stored in the SRDF file
        abb.set_named_target("down") 
        abb.go()
        rospy.sleep(1)
        
        # Open the gripper
        gripper.set_named_target("open")
        #gripper.set_random_target()
        gripper.go()
        rospy.sleep(1)

        ## Adding Objects to the Planning Scene
        ## ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        ## First, we will create a box in the planning scene between the fingers:
        box_name = "box"
        box_pose = PoseStamped()
        box_pose.header.frame_id = "world"
        box_pose.pose.orientation.w = 1.0
        box_pose.pose.position.x = 2.0
        box_pose.pose.position.y = 0.0
        box_pose.pose.position.z = 0.95

        scene.add_box(box_name, box_pose, size=(0.06, 0.06, 0.06))

        # Position for table 0
        start_pose1 = PoseStamped()
        start_pose1.header.frame_id = abb.get_planning_frame()
        start_pose1.pose.position.x = 2.0
        start_pose1.pose.position.y = 0.0 
        start_pose1.pose.position.z = 1.77 
        q = quaternion_from_euler(0, 0, 0) #zyx, 
        start_pose1.pose.orientation = Quaternion(*q)
        ## Position for table 1
        table1 = PoseStamped()
        table1.header.frame_id = abb.get_planning_frame()
        table1.pose.position.x = 0.0 
        table1.pose.position.y = 2.0 
        table1.pose.position.z = 1.77
        q = quaternion_from_euler(0, 1.5707963, 1.5707963) #zyx
        table1.pose.orientation = Quaternion(*q)

        abb.set_start_state_to_current_state()
        abb.set_pose_target(start_pose1, end_effector_link)
        #abb_plan_path(pose=start_pose)
        abb.go(wait=False)
        rospy.sleep(2)

        # go down in z direction to pick the box
        abb.set_start_state_to_current_state()
        start_pose1.pose.position.z = start_pose1.pose.position.z - 0.7
        abb.set_pose_target(start_pose1, end_effector_link)
        abb.go(wait=False)
        rospy.sleep(2)

        ## attach box
        grasping_group = 'gripper'
        touch_links = robot.get_link_names(group=grasping_group)
        scene.attach_box(end_effector_link, box_name, touch_links=touch_links)

        # go up in z direction
        abb.set_start_state_to_current_state()
        start_pose1.pose.position.z = start_pose1.pose.position.z + 0.7
        abb.set_pose_target(start_pose1, end_effector_link)
        abb.go(wait=False)
        rospy.sleep(2)

        # KDL plugin - go to top position above the table
        abb.set_start_state_to_current_state()
        abb.set_pose_target(table1, end_effector_link)
        abb.go(wait=False)
        rospy.sleep(2)

        # go down in z direction to pick the box
        abb.set_start_state_to_current_state()
        table1.pose.position.z = table1.pose.position.z - 0.7
        abb.set_pose_target(table1, end_effector_link)
        abb.go(wait=False)
        rospy.sleep(2) 

        # go up in z direction
        abb.set_start_state_to_current_state()
        table1.pose.position.z = table1.pose.position.z + 0.7
        abb.set_pose_target(table1, end_effector_link)
        abb.go(wait=False)
        rospy.sleep(2)
       
        scene.remove_attached_object(end_effector_link, name=box_name)
        scene.remove_world_object(box_name)
        

        # Shut down MoveIt cleanly
        moveit_commander.roscpp_shutdown()

if __name__ == '__main__':
    try:
        move_group_python_interface_tutorial()
    except rospy.ROSInterruptException:
        pass

        