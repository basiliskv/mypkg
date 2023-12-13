import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16, String

def cb(msg):
    global node, time_msg

    # メッセージが正しく受信されている場合のみログを表示
    if hasattr(node, 'time_msg'):
        node.get_logger().info("Listen: %d, Time: %s" % (msg.data, node.time_msg.data))
    else:
        node.get_logger().warn("countupを受信しましたが、Timeがまだ設定されていません。")

rclpy.init()
node = Node("listener")
pub = node.create_subscription(Int16, "countup", cb, 10)
time_pub = node.create_subscription(String, "current_time", lambda msg: setattr(node, 'time_msg', msg), 10)

rclpy.spin(node)