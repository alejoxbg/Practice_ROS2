#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
using std::placeholders::_1;

class Cpp_Subscriber : public rclcpp::Node
{
  public:
    Cpp_Subscriber()
    : Node("cpp_subscriber")
    {
      subscription_ = this->create_subscription<std_msgs::msg::String>("py_str_msg", 10, std::bind(&Cpp_Subscriber::topic_callback, this, _1));
    }

  private:
    void topic_callback(const std_msgs::msg::String::SharedPtr msg) const
    {
      RCLCPP_INFO(this->get_logger(), "I heard from python: '%s'", msg->data.c_str());
    }
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<Cpp_Subscriber>());
  rclcpp::shutdown();
  return 0;
}