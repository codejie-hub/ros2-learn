from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from launch.substitutions import Command
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    urdf_file = os.path.join(
        get_package_share_directory('ur5e_demo'),
        'urdf',
        'ur5_robotiq_140.urdf'
    )
    
    # 直接读取URDF文件内容
    with open(urdf_file, 'r') as infp:
        robot_description_content = infp.read()

    # 使用 xacro 生成 urdf
    # robot_description_content = Command([
    #     'xacro ', urdf_file
    # ])


    rviz_config = os.path.join(
        get_package_share_directory('ur5e_demo'),
        'rviz',
        'ur5e.rviz'
    )

    return LaunchDescription([
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui'
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{'robot_description': robot_description_content}]
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config],
            output='screen'
        )
    ])