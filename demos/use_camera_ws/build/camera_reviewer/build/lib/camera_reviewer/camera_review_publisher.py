import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class CameraPublisher(Node):
    def __init__(self):
        super().__init__('camera_publisher')
        # 创建图像发布者，发布到 'camera/image_raw' 话题
        self.publisher_ = self.create_publisher(Image, 'camera/image_raw', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.cap = cv2.VideoCapture(0)  # 打开默认摄像头
        self.bridge = CvBridge()

    def timer_callback(self):
        ret, frame = self.cap.read()
        if ret:
            # 将 OpenCV 图像转换为 ROS 2 图像消息
            img_msg = self.bridge.cv2_to_imgmsg(frame, "bgr8")
            self.publisher_.publish(img_msg)
            self.get_logger().info('发布图像帧')

    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()  # 释放摄像头资源

def main(args=None):
    rclpy.init(args=args)
    camera_publisher = CameraPublisher()
    rclpy.spin(camera_publisher)
    camera_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()