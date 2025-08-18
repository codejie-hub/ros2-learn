import sys
if sys.prefix == '/home/wp/envs/demo_env':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/wp/learn_ros/demos/face_recognition_ws/install/demo_python_service'
