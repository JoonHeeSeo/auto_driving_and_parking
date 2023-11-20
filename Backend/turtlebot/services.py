from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def send_car_call():
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "car_connection", 
        {
            'type': 'car.call',
            'message': 'Car call message',
        }
    )
