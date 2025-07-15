import rclpy
from rclpy.node import Node


def main():
    # 初始化ROS 2客户端库，这是使用ROS 2功能的必要步骤
    rclpy.init()
    # 创建一个名为'first_node'的ROS 2节点实例
    node = Node('first_node')
    # 使用节点的日志记录器输出一条信息日志，表明节点已启动
    node.get_logger().info('Hello, ROS 2!')
    # 进入节点的自循环，处理传入的ROS 2消息和服务请求
    rclpy.spin(node)
    # 销毁节点实例，释放节点占用的资源
    node.destroy_node()
    # 关闭ROS 2客户端库，结束ROS 2会话
    rclpy.shutdown()

if __name__=='__main__':
    main()