import rclpy
from rclpy.node import Node
from myservice.srv import MyService


class SimpleClient(Node):
    def __init__(self):
        super.__init__("simpleClient")
        self.cli=self.create_client(MyService,"myservice")
        # 检查服务是否存在
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("waiting for service....")
        self.req = MyService.request()
        self.req.name="hello"
        self.req.repeat=1
        self.future=self.cli.call_async(self.req)

def main():
    rclpy.init()
    client_node=SimpleClient()
    rclpy.spin_until_future_complete(client_node,client_node.future)
    if client_node.future.result() is not None:
        client_node.get_logger().info(f"Result: success={client_node.future.result().success}, message='{client_node.future.result().message}'")
    else:
        client_node.get_logger().error("service call fail...")
    rclpy.shutdown()