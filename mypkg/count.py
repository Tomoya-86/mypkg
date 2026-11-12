#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Tomoya Usuki
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node

class CountNode(Node):
    def __init__(self):
        super().__init__("count")
        self.get_logger().info("CountNode has been started.")

def main():
    rclpy.init()
    node = CountNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
