import graphene
from graphene_mongo import MongoengineObjectType
from .models import CarStatus
from .services import send_car_call


class CarCall(graphene.Mutation):
    ok = graphene.Boolean()

    def mutate(self, info):
        
        # 차량 호출 명령 시행
        print("----------------Got Car Call Request----------------")
        send_car_call()

        return CarCall(ok=True)

class Mutation(graphene.ObjectType):
    car_call = CarCall.Field()


## GraphQL Mutation
# AutoParking
'''
mutation {
  carCall {
    ok
  }
}
'''


class CarStatusType(MongoengineObjectType):
    class Meta:
        model = CarStatus

class Query(graphene.ObjectType):
    car_status = graphene.Field(CarStatusType)

    def resolve_car_status(self, info):
        return CarStatus.objects.order_by('-time').first()


## GraphQL Query
# CarStatus
'''
query {
  carStatus {
    time
    velocity
    battery
  }
}
'''


schema = graphene.Schema(query=Query, mutation=Mutation)
