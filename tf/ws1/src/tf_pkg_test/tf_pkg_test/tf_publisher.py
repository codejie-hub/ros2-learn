import tf2_ros
from geometry_msgs.msg import TransformStamped
import math
import rclpy
from tf_transformations import quaternion_from_euler

class TfPublisher(rclpy.node.Node):
    def __init__(self):
        super().__init__('tf_publisher')
        self.tf_broadcaster = tf2_ros.TransformBroadcaster(self)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.pitch = 0.0

    def timer_callback(self):
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'base_link'
        t.child_frame_id = 'tool0'
        # 变换内容：tool0 相对于 base_link，位置为 (1.0, 0.0, 0.0)，绕 Y 轴（pitch）旋转，角度每次增加 0.1 弧度。
        # 设置工具姿态
        t.transform.translation.x = 1.0
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.0
        # 每次调用增加 0.1 弧度的偏航角
        self.pitch += 0.1
        if self.pitch > 2 * math.pi:
            self.pitch -= 2 * math.pi
        # 设置工具的旋转
        q = quaternion_from_euler(0.0, self.pitch, 0.0)
        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]
        # 发布tf变换
        self.tf_broadcaster.sendTransform(t)
        self.get_logger().info('Publishing transform base_link -> tool0')
"""
变换关系:
发布的 TF 变换是从 base_link 到 tool0 的变换。
参考坐标系是 base_link，tool0 是子坐标系。
也就是说，tool0 的位置和姿态是相对于 base_link 定义和发布的
"""


def main(args=None):
    rclpy.init(args=args)
    tf_publisher = TfPublisher()
    rclpy.spin(tf_publisher)
    tf_publisher.destroy_node()
    rclpy.shutdown()

