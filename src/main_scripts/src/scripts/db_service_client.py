#!/usr/bin/env python
import rospy, random
from robot_custom_msgs.srv import *

if __name__ == "__main__":
    rospy.init_node('caller')

    call_service = rospy.ServiceProxy('get_order', OrderData)

    #r = rospy.Rate(1)
    #while not rospy.is_shutdown():
        
    req = OrderDataRequest()
    req.start = 'get-order'

    resp = call_service(req)
    print(resp)

        #r.sleep()
