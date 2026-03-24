from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_package',
            executable='my_node',
            name='my_node',
            output='screen',
            parameters=[{'param_name': 'param_value'}],
            remappings=[('/old_topic', '/new_topic')],
        ),
        Node(
            package='another_package',
            executable='another_node',
            name='another_node',
            output='screen',
        ),
    ])