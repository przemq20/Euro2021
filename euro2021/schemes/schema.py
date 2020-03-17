import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField

from euro2021.schemes.player.player_node import PlayerConnection


class Query(graphene.ObjectType):
	node = graphene.relay.Node.Field()

	all_players = SQLAlchemyConnectionField(PlayerConnection)

schema = graphene.Schema(query=Query)
