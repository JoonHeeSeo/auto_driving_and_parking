#!/usr/bin/env python
# -*- coding:utf-8 -*-

import rospy
import websocket
import ssl
import sys, select, os
import signal
from geometry_msgs.msg import Twist
from std_msgs.msg import String, UInt8  # 문자열 메시지를 사용하기 위해 추가


#####
def on_message(ws, message):
    global flag
    # 서버로부터 메시지를 수신했을 때 호출되는 콜백 함수
    print(message)
    received_message = int(message)
    if received_message ==1:
        pub = rospy.Publisher('/core/decided_mode', UInt8, queue_size=1)
        pub.publish(2)
    elif received_message ==2:
	pub = rospy.Publisher('/stop_flag', UInt8, queue_size=1)
        pub.publish(2)
    #stop_flag = message
    # 텍스트가 0이다 : 변수 명 변경 - 특정 변수를 publish,
    #pub = rospy.Publisher('stop_flag', String, queue_size=1)
    #pub.publish(stop_flag)
    flag = True

def on_open(ws):
    
    flag = False

def signal_handler(sig, frame):
    # 사용자가 Ctrl + C를 눌러서 종료하면 노드를 종료
    rospy.signal_shutdown("User interrupted")


if __name__ == '__main__':
    rospy.init_node('get_ws')  # ROS 노드 초기화
    # Ctrl + C를 사용한 종료 핸들러 등록
    signal.signal(signal.SIGINT, signal_handler)

    while not rospy.is_shutdown():
    # 웹 소켓 설정
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp("wss://k9a408.p.ssafy.io/ws/turtlebot/")
        ws.on_open = on_open
        ws.on_message = on_message

        ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})  # 웹 소켓 연결 유지

    # 웹 소켓 루프가 종료되면 노드 종료
    rospy.signal_shutdown("WebSocket loop terminated")
