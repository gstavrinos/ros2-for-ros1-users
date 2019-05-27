import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class PythonSubscriber(Node):

    def __init__(self):
        super().__init__("ros2_example_subscriber")
        self.sub = self.create_subscription(String, "ros2_check_string", self.callback)

    def callback(self, msg):
        print(msg.data)


def main():
    rclpy.init()
    node = PythonSubscriber()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
