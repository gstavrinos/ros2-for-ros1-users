#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

class CppPublisherExample : public rclcpp::Node{
public:
  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr pub;
  

  CppPublisherExample(): Node("ros2_example_publisher"){
      pub = create_publisher<std_msgs::msg::String>("ros2_check_string", 10);
  };
};

int main(int argc, char * argv[]){

  rclcpp::init(argc, argv);

  auto node = std::make_shared<CppPublisherExample>();

  while(rclcpp::ok()){
    std_msgs::msg::String msg = std_msgs::msg::String();
    msg.data = "Hello World!";
    node->pub->publish(msg);
  }

  rclcpp::shutdown();
  return 0;
}