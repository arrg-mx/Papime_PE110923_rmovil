#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/int64.hpp"

class NumberCounterNode : public rclcpp::Node // MODIFY NAME
{
public:
    NumberCounterNode() : Node("number_counter_node"), counter_(0) // MODIFY NAME
    {
        counter_publisher_ = this->create_publisher<std_msgs::msg::Int64>("number_counter_topic", 10);
        number_subscriber_ = this->create_subscription<std_msgs::msg::Int64>("number_topic_pub",
                             10,std::bind(&NumberCounterNode::callback_number, this, std::placeholders::_1));
        RCLCPP_INFO(this->get_logger(), "Nodo contador del numero activo");
    }

private:

    void callback_number(const std_msgs::msg::Int64::SharedPtr msg)
    {
        counter_ += msg->data;
        auto new_msg = std_msgs::msg::Int64();
        new_msg.data = counter_;
        counter_publisher_->publish(new_msg);
    }
    int counter_;
    rclcpp::Publisher<std_msgs::msg::Int64>::SharedPtr counter_publisher_;
    rclcpp::Subscription<std_msgs::msg::Int64>::SharedPtr number_subscriber_;

};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<NumberCounterNode>(); // MODIFY NAME
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}