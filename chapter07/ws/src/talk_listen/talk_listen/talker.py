import rclpy
from rclpy.node import Node
from interface.msg import Mymsg

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.publisher_ = self.create_publisher(Mymsg, 'greetings', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = Mymsg()
        msg.hello = 'hello'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: {msg.hello}')

def main(args=None):
    rclpy.init(args=args)
    node = Talker()
    rclpy.spin(node)
    rclpy.shutdown()