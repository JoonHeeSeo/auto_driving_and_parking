import json
import logging
from datetime import datetime
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import CarStatus

logger = logging.getLogger(__name__)


class TurtlebotConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        logger.info('----------------Connect-------------------')
        logger.info(self)
        logger.info('----------------Connect-------------------')


        await self.channel_layer.group_add("car_connection", self.channel_name)
        await self.accept()


    async def disconnect(self, close_code):
        pass


    async def receive(self, text_data):
        logger.info('----------------Receive-------------------')
        logger.info(text_data)
        logger.info('----------------Receive-------------------')

        # 데이터를 받아서
        # 1:70.8682403878;2:25.8803996173  <<  형식
        parts = text_data.split(";")
        values = {}
        for part in parts:
            key, value = part.split(":")
            values[key] = float(value)
        velocity = values['1']
        battery = values['2']

        # 메시지를 MongoDB에 저장
        status = CarStatus(
            time = datetime.now(),
            velocity = velocity,
            battery = battery
        )
        status.save()
        
        # Test용 Echo
        await self.send(text_data)

        # Json으로 받기
        # data = json.loads(text_data)
        # status_content = data['message']


    async def car_call(self, event):
        logger.info('----------------Car Call-------------------')
        logger.info(event)
        logger.info('----------------Car Call-------------------')

        # 차량 호출 : 2
        await self.send(text_data=str(2))

        # Json으로 보내기
        # message = event['message']
        # await self.send(text_data=json.dumps({
        #     'message': message
        # }))


    async def auto_parking(self, event):
        logger.info('----------------Auto Parking-------------------')
        logger.info(event)
        logger.info('----------------Auto Parking-------------------')

        # 자동 주차 : 1
        await self.send(text_data=str(1))

        # Json으로 보내기
        # message = event['message']
        # await self.send(text_data=json.dumps({
        #     'message': message
        # }))
