from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='tf_test',
            executable='static_tf_publish',
            name='tf_static_publish',
            output='screen'
        ),
        Node(
            package='tf_test',
            executable='dynamic_tf_publish',
            name='tf_dynamic_publish',
            output='screen'
        ),
        Node(
            package='tf_test',
            executable='tf_subscribe',
            name='tf_subscriber',
            output='screen'
        ),
    ])