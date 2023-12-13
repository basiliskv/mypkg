import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16, String  # String型を追加

import time  # 追加

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Int16, "countup", 10)
n = 0

def cb():
    global n
    msg = Int16()
    msg.data = n

    # 現在時刻を取得してString型のメッセージとしてpublish
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    time_msg = String()
    time_msg.data = now
    time_pub.publish(time_msg)

    pub.publish(msg)
    n += 1

time_pub = node.create_publisher(String, "current_time", 10)  # 追加

node.create_timer(0.5, cb)
rclpy.spin(node)