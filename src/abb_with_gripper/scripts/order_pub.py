#!/usr/bin/env python
# coding: utf-8
import rospy
from geometry_msgs.msg import Quaternion
from std_msgs.msg import Float64MultiArray
from tf.transformations import quaternion_from_euler
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
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

def send_order_to_robot():
    
    rospy.init_node('order_sender', anonymous=True)
    pub = rospy.Publisher('/robot_line', Float64MultiArray, queue_size=10)
    
    rate = rospy.Rate(10) # 10hz

    database = r"/home/dhara/arm_ws/src/armDB"
    conn = create_connection(database)
    target_pose = [0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,0,0,0,0,0,0,0,0]
    new_raw = 0
    while not rospy.is_shutdown():
        with conn:
            rospy.sleep(1)
            cur = conn.cursor()
            cur.execute("select * from placingdata")
            placingraw = cur.fetchall()
            
            if new_raw < len(placingraw):

                tableid = (placingraw[new_raw][0])
                target_pose[14] = tableid
                print("Order for table number: %d" %tableid)
                print('.--.')
                cur.execute("select * from world")
                raw = cur.fetchall()
                (id, x, y, z, roll, pitch, yaw) = tuple(raw[2])
                q = quaternion_from_euler(roll, pitch, yaw) #zyx, 
                stack = Quaternion(*q)
                target_pose[7] = x
                target_pose[8] = y
                target_pose[9] = z
                target_pose[10] = stack.x
                target_pose[11] = stack.y
                target_pose[12] = stack.z
                target_pose[13] = stack.w
 
                if tableid == 1:
                    (id, x, y, z, roll, pitch, yaw) = tuple(raw[0])
                    q = quaternion_from_euler(roll, pitch, yaw) #zyx, 
                    stack = Quaternion(*q)
                    target_pose[0] = x
                    target_pose[1] = y
                    target_pose[2] = z
                    target_pose[3] = stack.x
                    target_pose[4] = stack.y
                    target_pose[5] = stack.z
                    target_pose[6] = stack.w
                elif tableid == 2:
                    (id, x, y, z, roll, pitch, yaw) = tuple(raw[1])
                    q = quaternion_from_euler(roll, pitch, yaw) #zyx, 
                    stack = Quaternion(*q)
                    target_pose[0] = x
                    target_pose[1] = y
                    target_pose[2] = z
                    target_pose[3] = stack.x
                    target_pose[4] = stack.y
                    target_pose[5] = stack.z
                    target_pose[6] = stack.w
                else:
                    (id, x, y, z, roll, pitch, yaw) = tuple(raw[2])
                    q = quaternion_from_euler(roll, pitch, yaw) #zyx, 
                    stack = Quaternion(*q)
                    target_pose[0] = x
                    target_pose[1] = y
                    target_pose[2] = z
                    target_pose[3] = stack.x
                    target_pose[4] = stack.y
                    target_pose[5] = stack.z
                    target_pose[6] = stack.w
                new_raw = new_raw + 1
                data_to_send = Float64MultiArray()  # the data to be sent, initialise the array
                data_to_send.data = target_pose   # assign the array with the value you want to send
                rospy.loginfo(data_to_send)
                pub.publish(data_to_send)
                print('-------')
                rospy.sleep(5)
            else:
                print('------Waiting for new order------')
                rospy.sleep(5)
            
            
if __name__ == '__main__':
    try:
        send_order_to_robot()
    except rospy.ROSInterruptException:
        pass
    except rospy.ROSInternalException:
        print('ROS internal error')