import launch
from launch import LaunchDescription
from launch import LaunchService

def main(argv=sys.argv[1:]):
    ld = LaunchDescription([
        launch_ros.actions.Node(
            package="ros2_example_py", node_executable="ros2_subscriber", output="screen",
            parameters=["config/config.yaml"]),
        launch_ros.actions.Node(
            package="ros2_example_cpp", node_executable="ros2_publisher", output="screen")

    ])
    ls = LaunchService(argv=argv)
    ls.include_launch_description(ld)
    return ls.run()

if __name__ == "__main__":
    sys.exit(main())