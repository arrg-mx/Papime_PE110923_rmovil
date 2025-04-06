#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class MyCustmNode(Node): # Definicion del nodo
    def __init__(self):
        super().__init__("node_name") # Nombre del nodo


def main(args=None):
    rclpy.init(args=args)
    node = MyCustmNode()
    rclpy.spin()
    rclpy.shutdown()

if __name__ == "__main__":
    main()