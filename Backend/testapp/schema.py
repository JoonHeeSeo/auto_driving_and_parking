import graphene
from .models import Test
from graphene_mongo import MongoengineObjectType


class TestType(MongoengineObjectType):
    class Meta:
        model = Test

class Query(graphene.ObjectType):
    tests = graphene.List(TestType)

    def resolve_tests(self, info):
        return Test.objects.all()


# GraphQL 쿼리 
'''
query {
  tests {
    title
    publicationDate
  }
}
'''
