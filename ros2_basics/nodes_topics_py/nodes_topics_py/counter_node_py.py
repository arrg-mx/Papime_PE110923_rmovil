#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from std_msgs.msg import Int64

class CounterNode(Node): # Definicion del nodo
    def __init__(self):
        super().__init__("counter_node") # Nombre del nodo

        self.counter_ = 0
        self.number_counter_publisher_ = self.create_publisher(Int64, "number_count_topic", 10)
        self.number_subcriber_ = self.create_subscription(Int64, "number_topic_pub", self.callback_number, 10)
        self.get_logger().info("Nodo de contador activo")

    def callback_number(self, msg):
        self.counter_ += msg.data 
        new_msg = Int64()
        new_msg.data = self.counter_
        self.number_counter_publisher_.publish(new_msg)


def main(args=None):
    rclpy.init(args=args)
    node = CounterNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()