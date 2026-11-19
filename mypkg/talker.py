#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Tomoya Usuki
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from person_msgs.msg import Person   #変更: 作ったPerson型を使う

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Person, "person", 10)   #変更: 型とトピック名
n = 0


def cb():
    global n
    msg = Person()          #変更: Person型のメッセージを作る
    msg.name = "鈴木太郎"    #変更: msgファイルに書いた「name」
    msg.age = n % 256       #変更: msgファイルに書いた「age」（0〜255まで）
    pub.publish(msg)
    n += 1

node.create_timer(0.5, cb)
rclpy.spin(node)
