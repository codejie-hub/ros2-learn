import rclpy
import tf2_ros
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener

class TFSubscriber(rclpy.node.Node):
    def __init__(self):
        super().__init__('tf_subscriber')
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        self.timer = self.create_timer(0.1, self.lookup_transform)

    def lookup_transform(self):
        trans = self.tf_buffer.lookup_transform('base_link', 'tool0', rclpy.time.Time())
        if trans:
            self.get_logger().info(f"Transform : {trans.transform.translation}")
            self.get_logger().info(f"Rotation : {trans.transform.rotation}")
        else:
            self.get_logger().warn("Transform not available")

def main(args=None):
    rclpy.init(args=args)
    tf_subscriber = TFSubscriber()
    rclpy.spin(tf_subscriber)
    tf_subscriber.destroy_node()
    rclpy.shutdown()