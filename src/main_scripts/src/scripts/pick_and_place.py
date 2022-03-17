#!/usr/bin/env python
# coding: utf-8
import sys
import rospy
from moveit_commander import MoveGroupCommander,PlanningSceneInterface, RobotCommander, roscpp_initialize
from geometry_msgs.msg import PoseStamped
from collision_object import add_box_gripper, attach_box, detach_box, remove_box, add_box_on_table, remove_box_from_table
from db_service_server import create_connection
from robot_custom_msgs.srv import OrderData, OrderDataRequest

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
        self.target_pose = PoseStamped()
        self.target_pose.header.frame_id = self.abb.get_planning_frame()

        ## Instantiate Pose for picking position
        self.target_pose_pick = PoseStamped()
        self.target_pose_pick.header.frame_id = self.abb.get_planning_frame()

        rospy.loginfo('-------Robot Node started-----Ready for operation-----')
    
    def main_process(self):
            
            ## Instantiate service to fetch order from DB
            call_service = rospy.ServiceProxy('get_order', OrderData) 
            ## Instantiate service output  
            request = OrderDataRequest()
            request.start = 'get-order'
            ## Call service
            data = call_service(request)

            #print(data)
            if data.validation_text == 'valid':
                ## Define picking position -> target_pose_pick
                self.target_pose_pick.pose.position.x = data.target_pick_position_x
                self.target_pose_pick.pose.position.y = data.target_pick_position_y
                self.target_pose_pick.pose.position.z = data.target_pick_position_z
                self.target_pose_pick.pose.orientation.x = data.target_pick_orientation_x
                self.target_pose_pick.pose.orientation.y = data.target_pick_orientation_y
                self.target_pose_pick.pose.orientation.z = data.target_pick_orientation_z
                self.target_pose_pick.pose.orientation.w = data.target_pick_orientation_w
                #print('Placing position: %s' %self.target_pose_pick)

                ## Define placing position -> target_pose
                self.target_pose.pose.position.x = data.target_place_position_x
                self.target_pose.pose.position.y = data.target_place_position_y
                self.target_pose.pose.position.z = data.target_place_position_z
                self.target_pose.pose.orientation.x = data.target_place_orientation_x
                self.target_pose.pose.orientation.y = data.target_place_orientation_y
                self.target_pose.pose.orientation.z = data.target_place_orientation_z
                self.target_pose.pose.orientation.w = data.target_place_orientation_w
                #print('Picking position: %s' %self.target_pose)

                tableidstr = str(data.table_id)
                rospy.loginfo("-----Order received for table number: %s" %tableidstr)

                ## Put box on picking table
                add_box_on_table(tableid='0',scene=self.scene)

                ## Go to picking TOP position
                self.abb.set_start_state(self.robot.get_current_state())
                self.abb.set_pose_target(self.target_pose_pick, self.end_effector_link)
                self.abb.go(wait=False)
                rospy.loginfo('---after picking TOP pose---')
                rospy.sleep(2)

                ## Open gripper
                self.gripper.set_named_target("open")
                self.gripper.go( wait=False)
                rospy.sleep(1)
                
                ## Go down in z direction to pick the box
                self.abb.set_start_state(self.robot.get_current_state())
                self.target_pose_pick.pose.position.z = self.target_pose_pick.pose.position.z - 0.66
                self.abb.set_pose_target(self.target_pose_pick, self.end_effector_link)
                self.abb.go(wait=False)
                rospy.loginfo('---reched down to pick---')
                rospy.sleep(2)

                ## Close gripper
                self.gripper.set_named_target("close")
                self.gripper.go(wait=False)
                rospy.sleep(1)

                remove_box_from_table(box_name='0',scene=self.scene)

                ## box to gripper
                add_box_gripper(self.scene)
                attach_box(box_name='box',robot=self.robot,scene=self.scene,eef_link=self.end_effector_link)

                ## Go up in z direction after picking the box
                self.abb.set_start_state(self.robot.get_current_state())
                self.target_pose_pick.pose.position.z = self.target_pose_pick.pose.position.z + 0.64
                self.abb.set_pose_target(self.target_pose_pick, self.end_effector_link)
                self.abb.go(wait=False)
                rospy.loginfo('---gone up after pick---')
                rospy.sleep(2)
                
                self.abb.clear_pose_targets()
                rospy.loginfo('cleared all targets')

                ## Go to placing TOP position
                self.abb.set_start_state(self.robot.get_current_state())
                self.abb.set_pose_target(self.target_pose, self.end_effector_link)
                self.abb.go(wait=False)
                rospy.loginfo('---after placing TOP pose---')
                rospy.sleep(4)

                ## Go down in z direction to place the box
                self.abb.set_start_state(self.robot.get_current_state())
                self.target_pose.pose.position.z = self.target_pose.pose.position.z - 0.66
                self.abb.set_pose_target(self.target_pose, self.end_effector_link)
                self.abb.go(wait=False)
                rospy.loginfo('---gone down to place---')
                rospy.sleep(2)

                ## Open gripper
                self.gripper.set_named_target("open")
                self.gripper.go()
                rospy.sleep(1)
                
                ## Remove box from gripper
                detach_box(box_name='box',scene=self.scene,eef_link_name=self.end_effector_link)
                remove_box(box_name='box',scene=self.scene)

                ## Place box on placing table
                add_box_on_table(tableidstr,self.scene)
                rospy.sleep(1)

                ## Go up in z direction
                self.abb.set_start_state(self.robot.get_current_state())
                self.target_pose.pose.position.z = self.target_pose.pose.position.z + 0.64
                self.abb.set_pose_target(self.target_pose,self.end_effector_link)
                self.abb.go(wait=False)
                rospy.loginfo('---after placing pose---')
                rospy.sleep(2)
                
                ## Update DB
                self.add_entry_to_db('completed_orders',data.raw_id,data.table_id,data.order_time)
                self.delete_entry_from_db('test',data.raw_id)

                self.abb.clear_pose_targets()
                rospy.loginfo('cleared all targets')

                ## Go to Home
                self.abb.set_named_target("down")
                self.abb.go(wait=False)
                rospy.sleep(1)

                remove_box_from_table(tableidstr,self.scene)
                rospy.sleep(1)
                
            else:
                rospy.loginfo('------Waiting for new order-----')
                rospy.sleep(5)

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
        rate = rospy.Rate(0.2)
        
        while not rospy.is_shutdown():
            start = PickAndPlace()
            start.main_process()
            rate.sleep()
    except rospy.ROSInterruptException:
        pass