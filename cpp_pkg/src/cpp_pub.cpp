#include <chrono>
#include <cinttypes>
#include <memory>

#include "example_interfaces/srv/add_two_ints.hpp"
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

using namespace std::chrono_literals;

using AddTwoInts = example_interfaces::srv::AddTwoInts;
using std::placeholders::_1;
using std::placeholders::_2;

class Cpp_Publisher : public rclcpp::Node
{
    public:
        Cpp_Publisher()
        : Node("cpp_publisher"), count_(0)
        {
            publisher_=this->create_publisher<std_msgs::msg::String>("cpp_str_msg", 10);
            timer_=this->create_wall_timer(500ms,std::bind(&Cpp_Publisher::timer_callback,this));
            server_ = this->create_service<AddTwoInts>("add_two_ints", std::bind(&Cpp_Publisher::handle_service,this, _1, _2));
        }
    private:
        void timer_callback()
        {
            auto message = std_msgs::msg::String();
            message.data = "Hello python! " + std::to_string(count_++);
            RCLCPP_INFO(this->get_logger(), "Publishing to python: '%s'",message.data.c_str());
            publisher_->publish(message);
        }
    private:
         void handle_service(const AddTwoInts::Request::SharedPtr request_message,const AddTwoInts::Response::SharedPtr response_message)
         {
            RCLCPP_INFO(this->get_logger(),"request: %" PRId64 " + %" PRId64, request_message->a, request_message->b);
            response_message->sum = request_message->a + request_message->b;
         }
    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
    rclcpp::Service<example_interfaces::srv::AddTwoInts>::SharedPtr server_;
    size_t count_;
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<Cpp_Publisher>());
    rclcpp::shutdown();
    return 0;
}
