#!/usr/bin/env python
# coding: utf-8
import rospy
from geometry_msgs.msg import Quaternion
from std_msgs.msg import Float64MultiArray
from tf.transformations import quaternion_from_euler
import sqlite3
from sqlite3 import Error
import global_variables


class order_publisher(object):
    def create_connection(self,db_file):

        """ create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn

    def read_order_from_db(self,current_order):

        """ read order from database one by one
            :param current_order: counter from main file
            :return: order array
        """
        
        database = r"/home/dhara/arm_ws/src/armDB"
        conn = self.create_connection(database)
        target_pose = [0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0]
        #current_order = 0
    
        with conn:
            rospy.sleep(1)
            cur = conn.cursor()
            cur.execute("select * from order_data")
            orders = cur.fetchall()
            
            if current_order < len(orders):

                order_for_table = (orders[current_order][0])
                target_pose[14] = order_for_table
                rospy.loginfo('.----------.')
                rospy.loginfo("Sending Order for table number: %d" %order_for_table)
                rospy.loginfo('.----------.')
                cur.execute("select * from world_position")
                world_position_raw = cur.fetchall()
                (id, x, y, z, roll, pitch, yaw) = tuple(world_position_raw[2])
                q = quaternion_from_euler(roll, pitch, yaw) #zyx, 
                stack = Quaternion(*q)
                target_pose[7] = x
                target_pose[8] = y
                target_pose[9] = z
                target_pose[10] = stack.x
                target_pose[11] = stack.y
                target_pose[12] = stack.z
                target_pose[13] = stack.w

                (id, x, y, z, roll, pitch, yaw) = tuple(world_position_raw[order_for_table-1])
                q = quaternion_from_euler(roll, pitch, yaw) #zyx, 
                stack = Quaternion(*q)
                target_pose[0] = x
                target_pose[1] = y
                target_pose[2] = z
                target_pose[3] = stack.x
                target_pose[4] = stack.y
                target_pose[5] = stack.z
                target_pose[6] = stack.w

                current_order = current_order + 1

                data_to_send = Float64MultiArray()  # the data to be sent, initialise the array
                data_to_send.data = target_pose   # assign the array with the value you want to send 
                return data_to_send   
            else:
                text = ['------Waiting for new order------']
                return text

    def send_order_to_robot(self,topic_name):
        
        """ send order to chanel 'topic_name'
            :param topic_name: chanel in which data should be published
            :return: pub.publish(order)
        """
        # Define publisher
        pub = rospy.Publisher(topic_name, Float64MultiArray, queue_size=10)
        #rate = rospy.Rate(10) # 10hz
        counter = 0
        while not rospy.is_shutdown():
            order = self.read_order_from_db(counter)
            #print(order)
            if order == ['------Waiting for new order------']:
                rospy.loginfo(order)
            else:
                rospy.loginfo(order)
                pub.publish(order)
                print('-------')
                counter = counter + 1
            rospy.sleep(5)
        

            
if __name__ == '__main__':
    try:
        rospy.init_node('order_sender', anonymous=True)
        order_from_db = order_publisher()
        order_from_db.send_order_to_robot(global_variables.robot_topic_name)
    except rospy.ROSInterruptException:
        pass