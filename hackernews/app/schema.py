from django.contrib.auth.models import User
import graphene
import links.schema
import user.schema

class Query(links.schema.Query, user.schema.Query, graphene.ObjectType):
    pass

# schema = graphene.Schema(query=Query)

class Mutation(links.schema.Mutation, user.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query,mutation=Mutation)
