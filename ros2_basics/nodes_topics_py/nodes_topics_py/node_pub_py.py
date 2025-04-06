#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from std_msgs.msg import Int64


class NumberPub(Node):

    def __init__(self):
        super().__init__("number_pub_node")

        self.number_ = 2
        self.number_publisher_ = self.create_publisher(Int64, "number_topic_pub", 10)
        self.timer_ = self.create_timer(1.0, self.publis_number)
        self.get_logger().info("Nodo number_pub_node esta activo")
        

    def publis_number(self):
        msg = Int64()
        msg.data = self.number_
        self.number_publisher_.publish(msg)
        


def main(args=None):
    rclpy.init(args=args)
    node = NumberPub()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()