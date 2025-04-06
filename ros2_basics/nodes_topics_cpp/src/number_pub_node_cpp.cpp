#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/int64.hpp"

class NumberPublisherNode : public rclcpp::Node // MODIFY NAME
{
public:
    NumberPublisherNode() : Node("number_publisher"), number_(2) // MODIFY NAME
    {
        number_publisher_ = this->create_publisher<
        std_msgs::msg::Int64>("number_topic_pub", 10);
        number_timer_ = this->create_wall_timer(
            std::chrono::seconds(1),std::bind(
                &NumberPublisherNode::publish_number, this));
        RCLCPP_INFO(this->get_logger(), "Nodo publicador del numero activo");
    }

private:

    void publish_number()
    {
        auto msg = std_msgs::msg::Int64();
        msg.data = number_;
        number_publisher_->publish(msg);
    }

    int number_;
    rclcpp::Publisher<std_msgs::msg::Int64>::SharedPtr number_publisher_;
    rclcpp::TimerBase::SharedPtr number_timer_;

};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<NumberPublisherNode>(); // MODIFY NAME
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}