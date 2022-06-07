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

def abb_plan_path(pose):
    #print(pose)
    try:
        abb = MoveGroupCommander("arm")
        print('inside try')
        abb.plan(pose)
    except:
        print('Plan failed for pose %s' % pose)

def gen_pose(frame_id="/base_link", pos=[0,0,0], euler=[0,0,0]):
	pose = PoseStamped()
	pose.header.frame_id = frame_id
	pose.header.stamp = rospy.Time.now()
	pose.pose.position.x, pose.pose.position.y, pose.pose.position.z = pos
	pose.pose.orientation.x, pose.pose.orientation.y, pose.pose.orientation.z, pose.pose.orientation.w = quaternion_from_euler(*euler)
	return pose
        
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

        #rospy.Subscriber('/gazebo/set_model_state',ModelState)
        pub = rospy.Publisher('/gazebo/set_model_state',ModelState,queue_size=10)


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

        gazebo = ModelState()
        gazebo.model_name = 'unit_box'
        gazebo.pose.position = box_pose.pose.position
        gazebo.pose.orientation = box_pose.pose.orientation
        gazebo.reference_frame = 'world'
        gazebo.twist.linear.x = 0
        gazebo.twist.linear.y = 0
        gazebo.twist.linear.z = 0
        gazebo.twist.angular.x = 0
        gazebo.twist.angular.y = 0
        gazebo.twist.angular.z = 0
        #print('added box')
        pub.publish(gazebo)

        # Position for table 0
        start_pose1 = PoseStamped()
        start_pose1.header.frame_id = abb.get_planning_frame()
        start_pose1.pose.position.x = 2.0
        start_pose1.pose.position.y = 0.0 
        start_pose1.pose.position.z = 1.77 
        # start_pose.pose.orientation.x = 1.45743564202e-05
        # start_pose.pose.orientation.y = 0.6
        # #start_pose.pose.orientation.z = 0.5
        # start_pose.pose.orientation.w = 0.8 
        q = quaternion_from_euler(0, 1.5, 0) #zyx, 
        start_pose1.pose.orientation = Quaternion(*q)

        # abb.set_start_state(robot.get_current_state())
        # abb.set_pose_target(start_pose1, end_effector_link)
        # #abb_plan_path(pose=start_pose)
        # abb.go(wait=False)
        # rospy.sleep(2)

        # # go down in z direction to pick the box
        # abb.set_start_state(robot.get_current_state())
        # start_pose1.pose.position.z = start_pose1.pose.position.z - 0.6
        # abb.set_pose_target(start_pose1, end_effector_link)
        # abb.go(wait=False)
        # rospy.sleep(2)

        # ## attach box
        # grasping_group = 'gripper'
        # touch_links = robot.get_link_names(group=grasping_group)
        # scene.attach_box(end_effector_link, box_name, touch_links=touch_links)

        # table1 = PoseStamped()
        # table1.header.frame_id = abb.get_planning_frame()
        # ## Position for table 1
        # table1.pose.position.x = 0.0 
        # table1.pose.position.y = 2.0 
        # table1.pose.position.z = 1.78  
        # # start_pose.pose.orientation.x = -0.5
        # # start_pose.pose.orientation.y = 0.5
        # # start_pose.pose.orientation.z = 0.5
        # # start_pose.pose.orientation.w = 0.5
        # #q = quaternion_from_euler(0, 1.5707963, 0,axes='szyx')
        # q = quaternion_from_euler(0, 1.5707963, 1.5707963) #zyx
        # table1.pose.orientation = Quaternion(*q)
        # #print(start_pose)

        # # Position for table 2
        # # start_pose.pose.position.x = -1.25 
        # # start_pose.pose.position.y = 1.85 
        # # start_pose.pose.position.z = 1.78  
        # # start_pose.pose.orientation.x = -0.5
        # # start_pose.pose.orientation.y = 0.5
        # # start_pose.pose.orientation.z = 0.5
        # # start_pose.pose.orientation.w = 0.5
        # # q = quaternion_from_euler(0, 1.5707963, 1.5707963) #zyx
        # # start_pose.pose.orientation = Quaternion(*q)
        
        # # KDL plugin - go to top position above the table
        # abb.set_start_state(robot.get_current_state())
        # abb.set_pose_target(table1, end_effector_link)
        # #abb_plan_path(pose=start_pose)
        # abb.go(wait=False)
        # rospy.sleep(2)

        # gazebo.pose.position = table1.pose.position
        # gazebo.pose.orientation = table1.pose.orientation
        # pub.publish(gazebo)
        
        # # go down in z direction to pick the box
        # abb.set_start_state(robot.get_current_state())
        # table1.pose.position.z = table1.pose.position.z - 0.6
        # abb.set_pose_target(table1, end_effector_link)
        # abb.go(wait=False)
        # rospy.sleep(2)
        
        

        # # go up in z direction
        # abb.set_start_state(robot.get_current_state())
        # table1.pose.position.z = table1.pose.position.z + 0.6
        # abb.set_pose_target(table1, end_effector_link)
        # abb.go(wait=False)
        # rospy.sleep(2)
       
        scene.remove_attached_object(end_effector_link, name=box_name)
        scene.remove_world_object(box_name)
        

        # Shut down MoveIt cleanly
        moveit_commander.roscpp_shutdown()

if __name__ == '__main__':
    try:
        move_group_python_interface_tutorial()
    except rospy.ROSInterruptException:
        pass

        