import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/wp/learn_ros/demos/use_camera_ws/install/camera_vis'
