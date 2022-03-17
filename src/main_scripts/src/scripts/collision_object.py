#!/usr/bin/env python
# coding: utf-8
import rospy
from geometry_msgs.msg import PoseStamped


def wait_for_state_update(box_name,scene,
        box_is_known=False, box_is_attached=False, timeout=4
    ):
        """ Ensuring Collision Updates Are Received
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        ## If the Python node dies before publishing a collision object update message, the message
        ## could get lost and the box will not appear. To ensure that the updates are
        ## made, we wait until we see the changes reflected in the
        ## ``get_attached_objects()`` and ``get_known_object_names()`` lists.
        ## we call this function after adding, removing, attaching or detaching an object in the planning scene. 
        ## We then wait until the updates have been made or ``timeout`` seconds have passed
        """
        start = rospy.get_time()
        seconds = rospy.get_time()
        while (seconds - start < timeout) and not rospy.is_shutdown():
            # Test if the box is in attached objects
            attached_objects = scene.get_attached_objects([box_name])
            is_attached = len(attached_objects.keys()) > 0

            # Test if the box is in the scene.
            # Note that attaching the box will remove it from known_objects
            is_known = box_name in scene.get_known_object_names()

            # Test if we are in the expected state
            if (box_is_attached == is_attached) and (box_is_known == is_known):
                return True

            # Sleep so that we give other threads time on the processor
            rospy.sleep(0.1)
            seconds = rospy.get_time()

        # If we exited the while loop without returning then we timed out
        return False
def add_box_on_table(tableid,scene):

        """ Adding Objects to the Planning Scene
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        """
        ## First, we will create a box in the planning scene between the fingers:
        box_pose = PoseStamped()
        box_pose.header.frame_id = "world"
        if tableid == "1":
            box_pose.pose.orientation.w = 1.0
            box_pose.pose.position.y = 2.0
            box_pose.pose.position.z = 0.95
            box_name = "1"
            return scene.add_box(box_name, box_pose, size=(0.05, 0.05, 0.05))
        elif tableid == "2":
            box_pose.pose.orientation.w = 1.0
            box_pose.pose.position.x = -1.25
            box_pose.pose.position.y = 1.85
            box_pose.pose.position.z = 0.95
            box_name = "2"
            return scene.add_box(box_name, box_pose, size=(0.05, 0.05, 0.05))
        elif tableid == "0":
            box_pose.pose.orientation.w = 1.0
            box_pose.pose.position.x = 2.0
            box_pose.pose.position.z = 0.95
            box_name = "0"
            return scene.add_box(box_name, box_pose, size=(0.05, 0.05, 0.05))
        else:
            return False

def remove_box_from_table(box_name,scene):
        """ Removing Objects from the Planning Scene
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        """
        ## We can remove the box from the world.
        return scene.remove_world_object(box_name)

def add_box_gripper(scene, timeout=4):

        """ Adding Objects to the Planning Scene
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        """
        ## First, we will create a box in the planning scene between the fingers:
        box_pose = PoseStamped()
        box_pose.header.frame_id = "link_6"
        box_pose.pose.orientation.w = 1.0
        box_pose.pose.position.x = 0.18
        box_name = "box"
        scene.add_box(box_name, box_pose, size=(0.062, 0.062, 0.062))

        return wait_for_state_update(box_name,scene,box_is_known=True, timeout=timeout)

def attach_box(box_name,robot,scene,eef_link, timeout=4):

        """Attaching Objects to the Robot
        ## ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        ## Next, we will attach the box to the abb robot wrist. Manipulating objects requires the
        ## robot be able to touch them without the planning scene reporting the contact as a
        ## collision. By adding link names to the ``touch_links`` array, we are telling the
        ## planning scene to ignore collisions between those links and the box. 
        ## For the robot, we set ``grasping_group = 'name of your end effector group name'``. 
        """
        grasping_group = "gripper"
        touch_links = robot.get_link_names(group=grasping_group)
        scene.attach_box(eef_link, box_name, touch_links=touch_links)

        # We wait for the planning scene to update.
        return wait_for_state_update(box_name,scene,
            box_is_attached=True, box_is_known=False, timeout=timeout
        )

def detach_box(box_name,scene,eef_link_name, timeout=4):

        """Detaching Objects from the Robot
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        """
        scene.remove_attached_object(eef_link_name, name=box_name)
        
        # We wait for the planning scene to update.
        return wait_for_state_update(box_name,scene,
            box_is_known=True, box_is_attached=False, timeout=timeout
        )

def remove_box(box_name,scene, timeout=4):
        
        """Removing Objects from the Planning Scene
        ## ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        """
        ## We can remove the box from the world.
        scene.remove_world_object(box_name)

        ## **Note:** The object must be detached before we can remove it from the world

        # We wait for the planning scene to update.
        return wait_for_state_update(box_name,scene,
            box_is_attached=False, box_is_known=False, timeout=timeout
        )