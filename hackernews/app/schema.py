from django.contrib.auth.models import User
import graphene
from graphql_jwt import refresh_token
import links.schema
import user.schema
import graphql_jwt

class Query(links.schema.Query, user.schema.Query, graphene.ObjectType):
    pass

# schema = graphene.Schema(query=Query)

class Mutation(links.schema.Mutation, user.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    veryfy_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query,mutation=Mutation)
