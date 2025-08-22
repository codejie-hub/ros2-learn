import rclpy
from rclpy.node import Node
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped
import math
from tf_transformations import quaternion_from_euler
from random import random

class DynamicTFPublish(Node):
    def __init__(self):
        super().__init__('dynamic_tf_publish')
        self.broadcaster = TransformBroadcaster(self)
        self.timer = self.create_timer(0.1, self.publish_dynamic_tf)

    def publish_dynamic_tf(self):
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'camera_link'
        t.child_frame_id = 'object_link'

        # 物体位置随机变化
        t.transform.translation.x = 1.0 + 0.1 * (random() - 0.5)
        t.transform.translation.y = 2.0 + 0.1 * (random() - 0.5)
        t.transform.translation.z = 0.0 + 0.1 * (random() - 0.5)
        # 
        q = quaternion_from_euler(0.0, 0.0, math.pi / 2)
        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]
        self.broadcaster.sendTransform(t)
        self.get_logger().info(f'publish dynamic TF:{t.transform}')

def main(args=None):
    rclpy.init(args=args)
    node = DynamicTFPublish()
    rclpy.spin(node)
    rclpy.shutdown()