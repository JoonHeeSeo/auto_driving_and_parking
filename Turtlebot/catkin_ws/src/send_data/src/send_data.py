#!/usr/bin/env python
# -*- coding:utf-8 -*-

import rospy
import websocket
import ssl
from std_msgs.msg import UInt8, Float64
from geometry_msgs.msg import Twist
from sensor_msgs.msg import BatteryState
import threading

class DataSender:
    def __init__(self):
        self.speed_data = 0.0
        self.battery_data = 0.0

        # 웹 소켓 설정
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp("wss://k9a408.p.ssafy.io/ws/turtlebot/")

        # ROS 토픽 구독자 초기화
        self.sub_vel = rospy.Subscriber('/cmd_vel', Twist, self.speed_callback, queue_size=1)
        self.sub_battery = rospy.Subscriber('/battery_state', BatteryState, self.battery_callback, queue_size=1)

        # 웹 소켓 연결 유지를 위한 쓰레드 시작
        self.ws_thread = threading.Thread(target=self.ws.run_forever, kwargs={"sslopt": {"cert_reqs": ssl.CERT_NONE}})
        self.ws_thread.daemon = True  # 데몬 쓰레드로 설정하여 메인 쓰레드가 종료되면 함께 종료
        self.ws_thread.start()

        # ROS 메인 루프에서 데이터 송신을 위한 Timer 설정
        self.send_timer = rospy.Timer(rospy.Duration(1.0), self.send_data_to_server)

    def send_data_to_server(self, event):
        self.ws.send("{}:{};{}:{}".format(1, self.speed_data, 2, self.battery_data))

    def speed_callback(self, speed_msg):
        self.speed_data = speed_msg.linear.x * 1000

    def battery_callback(self, battery_msg):
        self.battery_data = (battery_msg.percentage - 0.98) / 0.22 * 100

if __name__ == '__main__':
    rospy.init_node('ros_to_websocket_node')
    node = DataSender()
    rospy.spin()

