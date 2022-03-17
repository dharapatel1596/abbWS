#!/usr/bin/env python

import rospy
from robot_custom_msgs.srv._OrderData import OrderData, OrderDataResponse
from geometry_msgs.msg import Quaternion
from tf.transformations import quaternion_from_euler
import sqlite3
from sqlite3 import Error



def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    db_connection = None
    try:
        db_connection = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return db_connection

def callback(request):
    """ Sends Order data from DB When serviceProxy send request
        return: order_data
    """
    order_data = OrderDataResponse()
    
    database = r"/home/dhara/arm_ws/src/armDB"
    db_connection = create_connection(database)
    with db_connection:
        rospy.sleep(1)
        db_cursor = db_connection.cursor()
        ## Fetch the first row from order DB
        db_cursor.execute("select * from test")
        orders = db_cursor.fetchone()
        
        while orders != None:

            order_data.raw_id = orders[0]
            order_data.table_id = orders[1]
            order_data.order_time = orders[2]
            print("Sending Order for table number: %d" %order_data.table_id)
            print('---')

            ## Fetching world positions according to order
            db_cursor.execute("select * from world_position")
            world_position_raw = db_cursor.fetchall()

            ## Order Pick Position
            (id, x, y, z, roll, pitch, yaw) = tuple(world_position_raw[2])
            q = quaternion_from_euler(roll, pitch, yaw) #zyx, 
            stack = Quaternion(*q)
            order_data.target_pick_position_x = x
            order_data.target_pick_position_y = y
            order_data.target_pick_position_z = z
            order_data.target_pick_orientation_x = stack.x
            order_data.target_pick_orientation_y = stack.y
            order_data.target_pick_orientation_z = stack.z
            order_data.target_pick_orientation_w = stack.w

            ## Order Place Position
            (id, x, y, z, roll, pitch, yaw) = tuple(world_position_raw[order_data.table_id-1])
            q = quaternion_from_euler(roll, pitch, yaw) #zyx, 
            stack = Quaternion(*q)
            order_data.target_place_position_x = x
            order_data.target_place_position_y = y
            order_data.target_place_position_z = z
            order_data.target_place_orientation_x = stack.x
            order_data.target_place_orientation_y = stack.y
            order_data.target_place_orientation_z = stack.z
            order_data.target_place_orientation_w = stack.w

            order_data.validation_text = 'valid'
            
            return order_data  
        else:
            rospy.loginfo('---No order to send---')
            order_data.target_pick_position_x = 0.0
            order_data.target_pick_position_y = 0.0
            order_data.target_pick_position_z = 0.0
            order_data.target_pick_orientation_x = 0.0
            order_data.target_pick_orientation_y = 0.0
            order_data.target_pick_orientation_z = 0.0
            order_data.target_pick_orientation_w = 0.0
            order_data.target_place_position_x = 0.0
            order_data.target_place_position_y = 0.0
            order_data.target_place_position_z = 0.0
            order_data.target_place_orientation_x = 0.0
            order_data.target_place_orientation_y = 0.0
            order_data.target_place_orientation_z = 0.0
            order_data.target_place_orientation_w = 0.0
            order_data.validation_text = '---No new order---'
            return order_data


if __name__ == "__main__":
    rospy.init_node('databse_order_sender', anonymous=True)
    rospy.Service('get_order', OrderData, callback)

    rospy.loginfo("-----DB Service started----Waiting for service-request-----")
    rospy.spin()
