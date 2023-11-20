from mongoengine import Document, StringField, IntField, FloatField


class ParkingLot(Document):
    parking_lot_id = StringField(required=True)
    parking_lot_name = StringField(max_length=200)
    position_x = FloatField()
    position_y = FloatField()
    standard_rate = IntField()
    overtime_rate = IntField()
    vacancy = IntField()
