# import unittest
# from graphene.test import Client
# from graphene import Schema
# from .schema import Query
# from .models import ParkingLot

# class GrapheneTestCase(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.client = Client(Schema(query=Query))
#         # 테스트 객체 생성
#         ParkingLot(parking_lot_id="50", parking_lot_name="TestLot1").save()
#         ParkingLot(parking_lot_id="51", parking_lot_name="TestLot2").save()

#     def test_parking_lots(self):
#         # parking_lots 쿼리 실행
#         executed = self.client.execute('''{ parkingLots { parkingLotName } }''')
#         self.assertEqual(executed, {
#             'data': {
#                 'parkingLots': [
#                     {'parkingLotName': 'TestLot1'},
#                     {'parkingLotName': 'TestLot2'}
#                 ]
#             }
#         })

# if __name__ == '__main__':
#     unittest.main()
