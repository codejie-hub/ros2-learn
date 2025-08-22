import rclpy
from rclpy.node import Node
from tf2_ros import StaticTransformBroadcaster
import math
from geometry_msgs.msg import TransformStamped
from tf_transformations import quaternion_from_euler

class StaticTFPublish(Node):
    def __init__(self):
        super().__init__('static_tf_publish')
        self.broadcaster = StaticTransformBroadcaster(self)
        self.publish_static_tf()

    def publish_static_tf(self):
        self.get_logger().info('Static TF publish node started.')
        t=TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'base_link'
        t.child_frame_id = 'camera_link'
        # 
        t.transform.translation.x = 1.0
        t.transform.translation.y = 2.0
        t.transform.translation.z = 0.0
        # 欧uler转四元数
        q = quaternion_from_euler(0.0, 0.0, math.pi/2)
        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]
        # 发送静态TF
        self.broadcaster.sendTransform(t)
        self.get_logger().info(f'publish static TF:{t.transform}')


def main(args=None):
    rclpy.init(args=args)
    node = StaticTFPublish()
    rclpy.spin(node)
    rclpy.shutdown()