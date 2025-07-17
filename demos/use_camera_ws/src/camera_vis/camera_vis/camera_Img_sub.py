import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class CameraSubscriber(Node):
    def __init__(self):
        super().__init__('camera_subscriber')
        self.subscription = self.create_subscription(
            Image,
            'camera/image_raw',
            self.listener_callback,
            10)
        self.bridge = CvBridge()
        

    def listener_callback(self, msg):
        # 将 ROS 2 图像消息转换为 OpenCV 图像
        cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        # 显示图像
        cv2.imshow("Camera Image", cv_image)
        cv2.waitKey(1)
        self.get_logger().info('接收到图像帧')

def main(args=None):
    rclpy.init(args=args)
    camera_subscriber = CameraSubscriber()
    rclpy.spin(camera_subscriber)
    camera_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
