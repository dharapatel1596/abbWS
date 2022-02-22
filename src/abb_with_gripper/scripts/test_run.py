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

def add_box(self, timeout=4):
        # Copy class variables to local variables to make the web tutorials more clear.
        # In practice, you should use the class variables directly unless you have a good
        # reason not to.
        box_name = self.box_name
        scene = self.scene

        ## BEGIN_SUB_TUTORIAL add_box
        ##
        ## Adding Objects to the Planning Scene
        ## ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        ## First, we will create a box in the planning scene between the fingers:
        box_pose = PoseStamped()
        box_pose.header.frame_id = "tool_0"
        box_pose.pose.orientation.w = 1.0
        box_pose.pose.position.z = 0.11  # above the panda_hand frame
        box_name = "box"
        scene.add_box(box_name, box_pose, size=(0.075, 0.075, 0.075))

        ## END_SUB_TUTORIAL
        # Copy local variables back to class variables. In practice, you should use the class
        # variables directly unless you have a good reason not to.
        self.box_name = box_name
        return self.wait_for_state_update(box_is_known=True, timeout=timeout)

def attach_box(self, timeout=4):
        # Copy class variables to local variables to make the web tutorials more clear.
        # In practice, you should use the class variables directly unless you have a good
        # reason not to.
        box_name = self.box_name
        robot = self.robot
        scene = self.scene
        eef_link = self.eef_link
        group_names = self.group_names

        ## BEGIN_SUB_TUTORIAL attach_object
        ##
        ## Attaching Objects to the Robot
        ## ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        ## Next, we will attach the box to the Panda wrist. Manipulating objects requires the
        ## robot be able to touch them without the planning scene reporting the contact as a
        ## collision. By adding link names to the ``touch_links`` array, we are telling the
        ## planning scene to ignore collisions between those links and the box. For the Panda
        ## robot, we set ``grasping_group = 'hand'``. If you are using a different robot,
        ## you should change this value to the name of your end effector group name.
        grasping_group = "gripper"
        touch_links = robot.get_link_names(group=grasping_group)
        scene.attach_box(eef_link, box_name, touch_links=touch_links)
        ## END_SUB_TUTORIAL

        # We wait for the planning scene to update.
        return self.wait_for_state_update(
            box_is_attached=True, box_is_known=False, timeout=timeout
        )

def detach_box(self, timeout=4):
        # Copy class variables to local variables to make the web tutorials more clear.
        # In practice, you should use the class variables directly unless you have a good
        # reason not to.
        box_name = self.box_name
        scene = self.scene
        eef_link = self.eef_link

        ## BEGIN_SUB_TUTORIAL detach_object
        ##
        ## Detaching Objects from the Robot
        ## ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        ## We can also detach and remove the object from the planning scene:
        scene.remove_attached_object(eef_link, name=box_name)
        ## END_SUB_TUTORIAL

        # We wait for the planning scene to update.
        return self.wait_for_state_update(
            box_is_known=True, box_is_attached=False, timeout=timeout
        )

def remove_box(self, timeout=4):
        # Copy class variables to local variables to make the web tutorials more clear.
        # In practice, you should use the class variables directly unless you have a good
        # reason not to.
        box_name = self.box_name
        scene = self.scene

        ## BEGIN_SUB_TUTORIAL remove_object
        ##
        ## Removing Objects from the Planning Scene
        ## ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        ## We can remove the box from the world.
        scene.remove_world_object(box_name)

        ## **Note:** The object must be detached before we can remove it from the world
        ## END_SUB_TUTORIAL

        # We wait for the planning scene to update.
        return self.wait_for_state_update(
            box_is_attached=False, box_is_known=False, timeout=timeout
        )

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
        abb.set_named_target("down")
         
        # # Plan and execute a trajectory to the goal configuration
        abb.go()
        rospy.sleep(1)
        
        # Open the gripper
        gripper.set_named_target("open")
        #gripper.set_random_target()
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
         #                      abb.get_end_effector_link())
        
        # KDL
        abb.set_start_state(robot.get_current_state())
        abb.set_pose_target(start_pose, end_effector_link)
        abb.go()
        rospy.sleep(2)

        #input("============ Press `Enter` to add a box to the planning scene ...")
        # Copy class variables to local variables to make the web tutorials more clear.
        # In practice, you should use the class variables directly unless you have a good
        # reason not to.

        ## BEGIN_SUB_TUTORIAL add_box
        ##
        ## Adding Objects to the Planning Scene
        ## ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        ## First, we will create a box in the planning scene between the fingers:
        box_pose = PoseStamped()
        box_pose.header.frame_id = "link_6"
        box_pose.pose.orientation.w = 1.0
        box_pose.pose.position.x = 0.15
        box_pose.pose.position.z = 0.0  # above the panda_hand frame
        box_name = "box"
        scene.add_box(box_name, box_pose, size=(0.065, 0.065, 0.065))
        #attach box
        grasping_group = "gripper"
        touch_links = robot.get_link_names(group=grasping_group)
        scene.attach_box(end_effector_link, box_name, touch_links=touch_links)
        
        #scene.remove_attached_object(end_effector_link, name=box_name)

        #scene.remove_world_object(box_name)
        

        # Shut down MoveIt cleanly
        moveit_commander.roscpp_shutdown()

if __name__ == '__main__':
    try:
        move_group_python_interface_tutorial()
    except rospy.ROSInterruptException:
        pass

        