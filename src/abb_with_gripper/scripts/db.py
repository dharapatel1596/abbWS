#!/usr/bin/env python
# coding: utf-8
import rospy
# from math import pi
from time import sleep
# import moveit_commander
# from geometry_msgs.msg import Pose, PoseStamped
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

database = r"/home/dhara/arm_ws/src/armDB"
conn = create_connection(database)
target_joints = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
target_jointsdown = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#while 1:
#stacknum = input("Which Stack should robot go:")
with conn:
    #print("connection received\n")
    cur = conn.cursor()
    cur.execute("select * from test")
    raw = cur.fetchone()
    old = raw[2]
    #print(raw)
    raw_id = raw[0]
    table_id = raw[1]
    table_name = 'completed_orders'
    query = "INSERT INTO %s (id_from_order_db,order_for_table,oldtime,newtime) VALUES (?, ?,?,DateTime('now'))" % table_name
    cur.execute(query,(raw_id,table_id,old))
    conn.commit()


    # (id, joint1, joint2, joint3, joint4, joint5, joint6)= tuple(raw[0])
    # target_jointsdown[0] = joint1
    # target_jointsdown[1] = joint2
    # target_jointsdown[2] = joint3
    # target_jointsdown[3] = joint4
    # target_jointsdown[4] = joint5
    # target_jointsdown[5] = joint6
    
    # if (raw[1][0]) == stacknum:
    #     (id, joint1, joint2, joint3, joint4, joint5, joint6)= tuple(raw[1])
    #     target_joints[0] = joint1
    #     target_joints[1] = joint2
    #     target_joints[2] = joint3
    #     target_joints[3] = joint4
    #     target_joints[4] = joint5
    #     target_joints[5] = joint6
    # elif (raw[2][0]) == stacknum:
    #     (id, joint1, joint2, joint3, joint4, joint5, joint6)= tuple(raw[2])
    #     target_joints[0] = joint1
    #     target_joints[1] = joint2
    #     target_joints[2] = joint3
    #     target_joints[3] = joint4
    #     target_joints[4] = joint5
    #     target_joints[5] = joint6
    # else:
    #     (id, joint1, joint2, joint3, joint4, joint5, joint6)= tuple(raw[0])
    # target_jointsdown[0] = joint1
    # target_jointsdown[1] = joint2
    # target_jointsdown[2] = joint3
    # target_jointsdown[3] = joint4
    # target_jointsdown[4] = joint5
    # target_jointsdown[5] = joint6