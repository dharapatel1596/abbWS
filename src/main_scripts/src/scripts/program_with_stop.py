#!/usr/bin/env python
# coding: utf-8
import sys
import rospy
from moveit_commander import MoveGroupCommander,PlanningSceneInterface, RobotCommander, roscpp_initialize
from geometry_msgs.msg import PoseStamped
from collision_object import add_box_gripper, attach_box, detach_box, remove_box, add_box_on_table, remove_box_from_table
from db_service_server import create_connection
from robot_custom_msgs.srv import OrderData, OrderDataRequest
from std_msgs.msg import Bool
from main_process_methods import pick_position, place_position, place_box, pick_box, go_to_safe_pose

class PickAndPlace(object):

    def __init__(self):

        ## Execution Flag
        self.execution_flag = True
        
        self.db_file = r"/home/dhara/arm_ws/src/armDB"
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

        ## Instantiate Planning scene for RVIZ
        self.scene = PlanningSceneInterface()

        ## Instantiate Pose for placing position
        self.place_pose = PoseStamped()
        self.place_pose.header.frame_id = self.abb.get_planning_frame()

        ## Instantiate Pose for picking position
        self.pick_pose = PoseStamped()
        self.pick_pose.header.frame_id = self.abb.get_planning_frame()


        rospy.loginfo('-----Robot Node started-----Ready for operation-----')

    def error_handling(self):
        objects = self.scene.get_known_object_names()
        print(objects)

        if self.scene.get_attached_objects(['box']):
            print('going to side position')
            go_to_safe_pose(robot=self.robot,arm_move_group=self.abb,eef_link=self.end_effector_link)
            detach_box(box_name='box',scene=self.scene,eef_link_name=self.end_effector_link)
            remove_box(box_name='box',scene=self.scene)
            rospy.sleep(5)
            self.execution_flag = True
        else:
            self.execution_flag = True

    def sensor_callback(self,data):
        if data.data == True:
            self.execution_flag = not(data.data)
            rospy.loginfo('stop robot')
            self.abb.stop()
        else:
            #self.main_process()
            self.execution_flag = False
            self.error_handling()
            
    def check_for_sensor(self):
        rospy.Subscriber("/stop_motion", Bool, self.sensor_callback)

    def main_process(self):
        if  self.execution_flag == True:
            ## Instantiate service to fetch order from DB
            call_service = rospy.ServiceProxy('get_order', OrderData) 
            ## Instantiate service output  
            request = OrderDataRequest()
            request.start = 'get-order'
            ## Call service
            data = call_service(request)

            #print(data)
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

                if self.execution_flag == True:
                    rospy.loginfo("-----sending execute in pick function: %s" %self.execution_flag)
                    pick_box(pose=self.pick_pose, robot_group=self.robot, arm_move_group=self.abb,
                                    gripper_move_group=self.gripper, eef_link=self.end_effector_link,
                                    planning_scene=self.scene, execution_flag = self.execution_flag)
                if  self.execution_flag == True:
                    rospy.loginfo("-----sending execute in place function: %s" %self.execution_flag)
                    place_box(pose=self.place_pose, robot_group=self.robot, arm_move_group=self.abb,
                                    gripper_move_group=self.gripper, eef_link=self.end_effector_link,
                                    planning_scene=self.scene, table_name=table_id_str, execution_flag = self.execution_flag)

                
                if self.execution_flag == True:
                    ## Update DB
                    self.add_entry_to_db('completed_orders',data.raw_id,data.table_id,data.order_time)
                    self.delete_entry_from_db('test',data.raw_id)

                    self.abb.clear_pose_targets()
                    rospy.loginfo('cleared all targets')

                    ## Go to Home
                    self.abb.set_named_target("down")
                    self.abb.go(wait=False)
                    rospy.sleep(1)

                    remove_box_from_table(table_id_str,self.scene)
                    rospy.sleep(1)
                
            else:
                rospy.loginfo('------Waiting for new order-----')
                rospy.sleep(5)
        else:
            rospy.loginfo('execution halt---waiting')

    def delete_entry_from_db(self,table_name,raw_id):
        """ Deletes entry according to raw_id from
            param: table_name
            return: successful operation
        """
        db_connect = create_connection(self.db_file)
        with db_connect:
            db_cursor = db_connect.cursor()
            query = "DELETE FROM %s WHERE id=?" % table_name
            db_cursor.execute(query, (raw_id,))
            db_connect.commit()
            return rospy.loginfo('-----Entry deleted successfully from %s-----'%table_name)

    def add_entry_to_db(self,table_name,raw_id,table_id,order_time):
        """ Adds entry according to table_name
            return: successful operation
        """
        db_connect = create_connection(self.db_file)
        with db_connect:
            db_cursor = db_connect.cursor()
            query = "INSERT INTO %s (id_from_order_db,order_for_table,oldtime,newtime) VALUES (? ,?, ?,DateTime('now'))" % table_name
            db_cursor.execute(query,(raw_id, table_id,order_time))
            db_connect.commit()
            return rospy.loginfo('-----Entry added successfully in %s-----'%table_name)


if __name__ == '__main__':
    try:
        rospy.init_node('main_order_receiver')
        rate = rospy.Rate(1)
        start = PickAndPlace()
        start.check_for_sensor()
        while not rospy.is_shutdown():
            start.main_process()
            rate.sleep()
    except rospy.ROSInterruptException:
        pass