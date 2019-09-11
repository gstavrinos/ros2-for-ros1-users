import launch
import launch_ros.actions

def generate_launch_description():
    sub_node = launch_ros.actions.Node(
        package='ros2_example_package_py',
        node_executable='ros2_subscriber',
        output='screen',
        remappings=[('ros2_check_string', 'ros2_check_string_remapped')])
    pub_node = launch_ros.actions.Node(
        package='ros2_example_package_cpp',
        node_executable='ros2_publisher',
        output='screen',
        remappings=[('ros2_check_string', 'ros2_check_string_remapped')])
    ld = launch.LaunchDescription()
    ld.add_action(sub_node)
    ld.add_action(pub_node)
    return ld