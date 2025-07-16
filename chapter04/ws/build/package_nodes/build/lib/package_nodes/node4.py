import rclpy
from rclpy.node import Node

class Node4(Node):
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info(f'{name} node has been started')

def main():
    rclpy.init()
    node = Node4('node4')
    rclpy.spin(node)
    rclpy.shutdown()