#!/usr/bin/env python
# coding: utf-8
import rospy
# from math import pi
from time import sleep
# import moveit_commander
# from geometry_msgs.msg import Pose, PoseStamped
from std_msgs.msg import String, Int32, Float64MultiArray
# from moveit_commander import MoveGroupCommander,PlanningSceneInterface
# from tf.transformations import quaternion_from_euler
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
    pub = rospy.Publisher('/user_input', Float64MultiArray, queue_size=10)
    rospy.init_node("dbfilepub")
    rate = rospy.Rate(10) # 10hz
    database = r"/home/dhara/armDB"
    target_joints = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    target_jointsdown = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    conn = create_connection(database)

    while not rospy.is_shutdown():
        stacknum = input("Which Stack should robot go:")
        #print(stacknum)
        
        with conn:
            #print("connection received\n")
            cur = conn.cursor()
            cur.execute("select * from joints")
            raw = cur.fetchall()
            
            if (raw[1][0]) == stacknum:
                (id, joint1, joint2, joint3, joint4, joint5, joint6)= tuple(raw[1])
                target_joints[0] = joint1
                target_joints[1] = joint2
                target_joints[2] = joint3
                target_joints[3] = joint4
                target_joints[4] = joint5
                target_joints[5] = joint6
            elif (raw[2][0]) == stacknum:
                (id, joint1, joint2, joint3, joint4, joint5, joint6)= tuple(raw[2])
                target_joints[0] = joint1
                target_joints[1] = joint2
                target_joints[2] = joint3
                target_joints[3] = joint4
                target_joints[4] = joint5
                target_joints[5] = joint6
            else:
                (id, joint1, joint2, joint3, joint4, joint5, joint6)= tuple(raw[0])
                target_joints[0] = joint1
                target_joints[1] = joint2
                target_joints[2] = joint3
                target_joints[3] = joint4
                target_joints[4] = joint5
                target_joints[5] = joint6
            data_to_send = Float64MultiArray()  # the data to be sent, initialise the array
            data_to_send.data = target_joints # assign the array with the value you want to send
            rospy.loginfo(data_to_send)
            pub.publish(data_to_send)
            rate.sleep()


if __name__ == '__main__':
    try:
        get_user_input()
    except rospy.ROSInterruptException:
        pass