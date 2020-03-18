import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField

from euro2021.schemes.in_match_model import in_match_model_node
from euro2021.schemes.match.match_node import MatchConnection
from euro2021.schemes.player.player_node import PlayerConnection


class Query(graphene.ObjectType):
	node = graphene.relay.Node.Field()

	all_players = SQLAlchemyConnectionField(PlayerConnection)
	all_matches = SQLAlchemyConnectionField(MatchConnection)


schema = graphene.Schema(query=Query)
