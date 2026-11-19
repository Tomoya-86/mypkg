#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Tomoya Usuki
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from person_msgs.srv import Query


rclpy.init()
node = Node("talker")


def cb(request, response):
    if request.name == "鈴木太郎":
        response.age = 41
    else:
        response.age = 255
    return response


def main():
    srv = node.create_service(Query, "query", cb)
    rclpy.spin(node)
