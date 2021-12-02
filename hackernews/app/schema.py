from django.contrib.auth.models import User
import graphene
from graphql_jwt import refresh_token
from links.models import Link
import links.schema
import user.schema
import graphql_jwt
import links.schema_relay
# from links import schema_relay


class Query(
    links.schema.Query,
    user.schema.Query,
    links.schema_relay.RelayQuery,
    graphene.ObjectType
):
    pass

# schema = graphene.Schema(query=Query)


class Mutation(links.schema.Mutation, user.schema.Mutation, links.schema_relay.RelayMutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    veryfy_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
