#!/usr/bin/env python
# coding: utf-8
import rospy
from geometry_msgs.msg import PoseStamped
from collision_object import remove_box_from_table
from robot_custom_msgs.srv import OrderData, OrderDataRequest
from main_process_methods import pick_position, place_position, update_database
from pick_place_class import PickPlaceClass

class PickAndPlace(object):
    def __init__(self):
    
        self.db_file = r"/opt/Robotik/ROS_Example_Program/src/armDB"
        
        self.robot = PickPlaceClass()
        ## Instantiate Pose for placing position
        self.place_pose = PoseStamped()
        self.place_pose.header.frame_id = self.robot.abb.get_planning_frame()

        ## Instantiate Pose for picking position
        self.pick_pose = PoseStamped()
        self.pick_pose.header.frame_id = self.robot.abb.get_planning_frame()

        rospy.loginfo('-------Robot Node started-----Ready for operation-----')
    
    def main_process(self):
            
            ## Instantiate service to fetch order from DB
            call_service = rospy.ServiceProxy('get_order', OrderData) 
            ## Instantiate service output  
            request_data = OrderDataRequest()
            request_data.start = 'get_data'

            ## Call service
            data = call_service(request_data)

            if data.validation_text == 'valid':
                ## Define picking position 
                self.pick_pose = pick_position(pose_array=data,arm_move_group=self.robot.abb)
                rospy.loginfo('Picking position received: %s' %self.pick_pose)
                
                ## Define placing position
                self.place_pose = place_position(pose_array=data,arm_move_group=self.robot.abb)
                rospy.loginfo('Placing position received: %s' %self.place_pose)

                ## Define table order
                table_id_str = str(data.table_id)
                rospy.loginfo("-----Order received for table number: %s" %table_id_str)

                ## Calling pick Method
                self.robot.pick_box(pose=self.pick_pose)

                ## Calling place Method
                self.robot.place_box(pose=self.place_pose, table_name=table_id_str)

                ## Update DB
                update_database(db_path=self.db_file,table_name_add='completed_orders',table_name_delete='order_data',
                                    raw_id=data.raw_id,table_id=data.table_id,order_time=data.time_of_order_entry)

                ## Go to Home
                self.robot.home_position()

                remove_box_from_table(table_id_str,self.robot.scene)
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