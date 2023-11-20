from mongoengine import Document, FloatField, DateTimeField


class CarStatus(Document):

    # 시간
    time = DateTimeField()

    # 속도 : 1
    velocity = FloatField()
 
    # 배터리 잔량 : 2
    battery = FloatField()

            