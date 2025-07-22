import rclpy
from rclpy.node import Node
from myservice.srv import MyService


class SimpleService(Node):
    def __init__(self):
        super().__init__('simple_service')
        self.srv = self.create_service(MyService, 'myservice', self.handle_service)
        self.get_logger().info("Service myservice is ready..")

    def handle_service(self, request, response):
        self.get_logger().info(f'Received request: {request.name}, repeat: {request.repeat}')
        response.success = True
        response.message = f'Hello {request.name}, repeated {request.repeat} times!'
        return response
    
def main():
    rclpy.init()
    node=SimpleService()
    rclpy.spin(node)
    rclpy.shutdown()