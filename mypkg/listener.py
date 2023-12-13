import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16, String  # String型を追加

def cb(msg):
    global node
    node.get_logger().info("Listen: %d, Time: %s" % (msg.data, time_msg.data))

rclpy.init()
node = Node("listener")
pub = node.create_subscription(Int16, "countup", cb, 10)
time_pub = node.create_subscription(String, "current_time", lambda msg: setattr(node, 'time_msg', msg), 10)  # 追加

rclpy.spin(node)