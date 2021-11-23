#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "custom_msg_srv/msg/custommsg.hpp"
using std::placeholders::_1;

class Cpp_Subscriber : public rclcpp::Node
{
  public:
    Cpp_Subscriber()
    : Node("cpp_subscriber")
    {
      subscription_ = this->create_subscription<custom_msg_srv::msg::Custommsg>("py_str_msg", 10, std::bind(&Cpp_Subscriber::topic_callback, this, _1));
    }

  private:
    void topic_callback(const custom_msg_srv::msg::Custommsg::SharedPtr msg) const
    {
      RCLCPP_INFO(this->get_logger(), "I heard from python: '%s' and '%i", msg->msg.c_str(), msg->num);
    }
    rclcpp::Subscription<custom_msg_srv::msg::Custommsg>::SharedPtr subscription_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<Cpp_Subscriber>());
  rclcpp::shutdown();
  return 0;
}