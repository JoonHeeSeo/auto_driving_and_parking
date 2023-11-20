import graphene
from graphene_mongo import MongoengineObjectType
from .models import ParkingLot
from .services import send_auto_parking, send_custom_parking


class ParkingLotType(MongoengineObjectType):
    class Meta:
        model = ParkingLot

class Query(graphene.ObjectType):
    parking_lots = graphene.List(ParkingLotType)

    def resolve_parking_lots(self, info):
        return ParkingLot.objects.all()


## GraphQL Query
# ParkingLot
'''
query {
  parkingLots {
    parkingLotId
    parkingLotName
    positionX
    positionY
    standardRate
    overtimeRate
    vacancy
  }
}
'''


class AutoParking(graphene.Mutation):
    ok = graphene.Boolean()

    def mutate(self, info):
        
        # 자동 주차 명령 시행
        print("----------------Got Auto Parking Request----------------")
        send_auto_parking()

        return AutoParking(ok=True)

class CustomParking(graphene.Mutation):
    class Arguments:
        parking_lot_id = graphene.String(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, parking_lot_id):
        
        # 임의 주차 명령 시행
        print(f"----------------Got Custom Parking Request to {parking_lot_id}----------------")
        send_custom_parking(parking_lot_id)

        return CustomParking(ok=True)

class Mutation(graphene.ObjectType):
    auto_parking = AutoParking.Field()
    custom_parking = CustomParking.Field()


## GraphQL Mutation
# AutoParking
'''
mutation {
  autoParking {
    ok
  }
}
'''

# CustomParking
'''
mutation($parkingLotId: String!) {
  customParking(parkingLotId: $parkingLotId) {
    ok
  }
}

{
  "parkingLotId": "1"
}
'''


schema = graphene.Schema(query=Query, mutation=Mutation)
