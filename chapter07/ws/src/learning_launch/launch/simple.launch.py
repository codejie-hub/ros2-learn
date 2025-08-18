from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='talk_listen',
            executable='talker',
            output='screen'
        ),
        Node(
            package='talk_listen',
            executable='listener',
            output='screen'
        ),
    ])