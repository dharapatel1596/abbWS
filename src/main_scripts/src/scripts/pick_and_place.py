#!/usr/bin/env python
# coding: utf-8
import sys
import rospy
from moveit_commander import MoveGroupCommander, PlanningSceneInterface, RobotCommander, roscpp_initialize
from geometry_msgs.msg import PoseStamped
from robot_custom_msgs.srv import OrderData, OrderDataRequest
from collision_object import remove_box_from_table
from main_process_methods import update_database,pick_box, pick_position, place_box, place_position

class PickAndPlace(object):
    def __init__(self):

        self.db_file = r"/home/dhara/arm_ws/src/armDB"
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

        rospy.loginfo('-------Robot Node started-----Ready for operation-----')
    
    def main_process(self):
            
        ## Instantiate service to fetch order from DB
        call_service = rospy.ServiceProxy('get_order', OrderData) 
        request = OrderDataRequest()
        request.start = 'get-order'

        ## Call service
        data = call_service(request)

        if data.validation_text == 'valid':
            ## Define picking position 
            self.pick_pose = pick_position(pose_array=data, arm_move_group=self.abb)
            print('Picking position received: %s' %self.pick_pose)
            
            ## Define placing position
            self.place_pose = place_position(pose_array=data, arm_move_group=self.abb)
            print('Placing position received: %s' %self.place_pose)

            ## Define table order
            table_id_str = str(data.table_id)
            rospy.loginfo("-----Order received for table number: %s" %table_id_str)


            pick_box(pose=self.pick_pose, robot_group=self.robot, arm_move_group=self.abb,
                        gripper_move_group=self.gripper, eef_link=self.end_effector_link,
                        planning_scene=self.scene)

            place_box(pose=self.place_pose, robot_group=self.robot, arm_move_group=self.abb,
                        gripper_move_group=self.gripper, eef_link=self.end_effector_link,
                        planning_scene=self.scene, table_name=table_id_str)
            
            ## Update DB
            update_database(db_path=self.db_file,table_name_add='completed_orders',table_name_delete='order_data',
                                raw_id=data.raw_id,table_id=data.table_id,order_time=data.order_time)

            ## Clear all pose from MoveIT
            self.abb.clear_pose_targets()
            rospy.loginfo('cleared all targets')
            ## Go to Home
            self.abb.set_named_target("down")
            self.abb.go(wait=False)
            rospy.sleep(1)
            remove_box_from_table(box_name=table_id_str, scene=self.scene)
            rospy.sleep(1)
            
        else:
            rospy.loginfo('------Waiting for new order-----')
            rospy.sleep(5)

if __name__ == '__main__':
    try:
        rospy.init_node('main_order_receiver')
        rate = rospy.Rate(0.2)
        start = PickAndPlace()
        while not rospy.is_shutdown(): 
            start.main_process()
            rate.sleep()
    except rospy.ROSInterruptException:
        pass