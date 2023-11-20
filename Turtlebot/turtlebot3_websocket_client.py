import asyncio
import websockets
import json
async def connect_to_server():
    uri = "ws://k9a408.p.ssafy.io/ws/turtlebot/"  # 원하는 웹소켓 서버 주소로 변경하세요.

    async with websockets.connect(uri) as websocket:
        while True:
            msg = input()
            if msg == 'exit':
                break
            json_data = {"message": msg}
            # print(json_data)
            await websocket.send(json.dumps(json_data))  # 서버로 메시지 보내기

            response = await websocket.recv()  # 서버에서 메시지 기다리고 받기
            print(f"서버로부터 받은 메시지: {response}")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(connect_to_server())
