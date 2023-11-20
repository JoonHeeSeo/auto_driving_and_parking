import graphene

import parking.schema as parking_schema 
import testapp.schema as testapp_schema 
import turtlebot.schema as turtlebot_schema

class Query(parking_schema.Query, turtlebot_schema.Query, testapp_schema.Query, graphene.ObjectType): 
   pass 

class Mutation(parking_schema.Mutation, turtlebot_schema.Mutation, graphene.ObjectType):
   pass

schema = graphene.Schema(query=Query, mutation=Mutation)


