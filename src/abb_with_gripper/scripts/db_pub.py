#!/usr/bin/env python
# coding: utf-8
from turtle import shape
import rospy
from math import pi
from time import sleep
from geometry_msgs.msg import Pose, PoseStamped, Quaternion
from std_msgs.msg import String, Int32, Float64MultiArray, MultiArrayDimension
# from moveit_commander import MoveGroupCommander,PlanningSceneInterface
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

def get_user_input():
    
    rospy.init_node('sender', anonymous=True)
    
    pub = rospy.Publisher('/user_input', Float64MultiArray, queue_size=10)
    #target_pose = PoseStamped()
    rate = rospy.Rate(10) # 10hz
    database = r"/home/dhara/armDB"
    target_pose = [0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,0,0,0,0,0,0,0]
    target_pose_pick = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0]
    conn = create_connection(database)
    # Instantiate Pose
    
    while not rospy.is_shutdown():
        
        stacknum = input("Which Stack robot should place the box:")
        with conn:
            #print("connection received\n")
            cur = conn.cursor()
            cur.execute("select * from world")
            raw = cur.fetchall()
            #print(tuple(raw[0]))
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
            if stacknum == 1:
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
            elif stacknum == 2:
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
            data_to_send = Float64MultiArray()  # the data to be sent, initialise the array
            #data_to_send = target_pose
            data_to_send.data = target_pose   # assign the array with the value you want to send
            #data_to_send.data = target_pose_pick
            rospy.loginfo(data_to_send)
            pub.publish(data_to_send)
            



if __name__ == '__main__':
    try:
        get_user_input()
    except rospy.ROSInterruptException:
        pass