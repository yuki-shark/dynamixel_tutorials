#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
# import std_msgs.msg
import math

def talker():
    pan = rospy.Publisher('/pan_controller/command', Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1000) # 60hz
    init_time = rospy.get_time()
    rospy.loginfo("init")
    pan.publish(0.0)
    while not rospy.is_shutdown():
        # hello_str = "hello world %s" % rospy.get_time()
        time = rospy.get_time()
        deg = math.pi / 2.0 * math.sin(time/4.0)
        rospy.loginfo(deg)
        pan.publish(deg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
