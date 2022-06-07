#!/usr/bin/env python
'''
PROS:
--vel, acc scaling easily controlled
--ptp,lin motion easily controlled
--pause, resume action

CONS:
--Grippers which don't have mimic joint can not be used
--scene couldn't be added
--plan and execute functionality not exist
--not flexible - less functionality
'''

from geometry_msgs.msg import Point, PoseStamped
from pilz_robot_programming import *
import math
import rospy
from moveit_commander import MoveGroupCommander,RobotCommander,PlanningSceneInterface

__REQUIRED_API_VERSION__ = "1"


def start_program():

    r = Robot(__REQUIRED_API_VERSION__)
    robot = RobotCommander()
    
    # Connect to the abb move group
    abb = MoveGroupCommander("arm")
        
    # Initialize the move group for the right gripper
    gripper = MoveGroupCommander("gripper")
    scene = PlanningSceneInterface()
    #pose_after_relative = r.get_current_pose()
    print(r.get_current_joint_states())
    #print(cur)
    # abb.set_named_target("side") 
    # abb.go()
    # rospy.sleep(1)
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
    print('add box')
    #r.move(Ptp(goal=cur, relative=True, vel_scale=0.2))

    #r.move(Ptp(goal=Pose(position=Point(0, 2.0, 1.86)), vel_scale=0.1, acc_scale=0.1))
    r.move(Lin(goal=Pose(position=Point(0.0, 2.0, 1.86))))

    r.move(Gripper([0.02,0.02],0.2))


    # Simple ptp movement
    #r.move(Ptp(goal=[0, 0.5, 0.5, 0, 0, 0], vel_scale=0.4))

    #start_joint_values = r.get_current_joint_states()
    #print(start_joint_values)


    # # Relative ptp movement
    # r.move(Ptp(goal=[0.1, 0, 0, 0, 0, 0], relative=True, vel_scale=0.2))
    # r.move(Ptp(goal=Pose(position=Point(0, 0, -0.1)), relative=True))
    # r.move(Ptp(goal=[-0.2, 0, 0, 0, 0, 0], relative=True, acc_scale=0.2))

    # pose_after_relative = r.get_current_pose()

    # # Simple Lin movement
    # r.move(Lin(goal=Pose(position=Point(0.2, 0, 0.8)), vel_scale=0.1, acc_scale=0.1))

    # # Relative Lin movement
    r.move(Lin(goal=Pose(position=Point(0, -0.2, 0), orientation=from_euler(0, 0, math.radians(15))), relative=True,
           vel_scale=0.1, acc_scale=0.1))
    # r.move(Lin(goal=Pose(position=Point(0, 0.2, 0)), relative=True,
    #        vel_scale=0.1, acc_scale=0.1))

    # # Circ movement
    # r.move(Circ(goal=Pose(position=Point(0.2, -0.2, 0.8)), center=Point(0.1, -0.1, 0.8), acc_scale=0.1))

    # # Move robot with stored pose
    # r.move(Ptp(goal=pose_after_relative, vel_scale=0.2))

    # # Repeat the previous steps with a sequence command
    # sequence = Sequence()
    # sequence.append(Lin(goal=Pose(position=Point(0.2, 0, 0.8)), vel_scale=0.1, acc_scale=0.1))
    # sequence.append(Circ(goal=Pose(position=Point(0.2, -0.2, 0.8)), center=Point(0.1, -0.1, 0.8), acc_scale=0.1))
    # sequence.append(Ptp(goal=pose_after_relative, vel_scale=0.2))

    # r.move(sequence)

    # # Move to start goal for sequence demonstration
    # r.move(Ptp(goal=start_joint_values))

    # # Blend sequence
    # blend_sequence = Sequence()
    # blend_sequence.append(Lin(goal=Pose(position=Point(0.2, 0, 0.7)), acc_scale=0.05), blend_radius=0.01)
    # blend_sequence.append(Lin(goal=Pose(position=Point(0.2, 0.1, 0.7)), acc_scale=0.05))

    # r.move(blend_sequence)

    # # Move with custom reference frame
    # r.move(Ptp(goal=PoseStamped(header=Header(frame_id="prbt_tcp"),
    #                             pose=Pose(position=Point(0, 0, 0.1)))))
    # r.move(Ptp(goal=Pose(position=Point(0, -0.1, 0)), reference_frame="prbt_link_3", relative=True))

    # # Create and execute an invalid ptp command with out of bound joint values
    # try:
    #     r.move(Ptp(goal=[0, 10.0, 0, 0, 0, 0]))
    # except RobotMoveFailed:
    #     rospy.loginfo("Ptp command did fail as expected.")


if __name__ == "__main__":
    # Init a ros node
    rospy.init_node('robot_program_node')

    start_program()
