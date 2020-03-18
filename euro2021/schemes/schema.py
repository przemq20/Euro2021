import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField

import euro2021.schemes.match.in_match_model_node
from euro2021.schemes.match.match_node import MatchConnection
from euro2021.schemes.player.player_node import PlayerConnection
from euro2021.schemes.team.team_node import TeamConnection


class Query(graphene.ObjectType):
	node = graphene.relay.Node.Field()

	all_players = SQLAlchemyConnectionField(PlayerConnection)
	all_matches = SQLAlchemyConnectionField(MatchConnection)
	all_teams = SQLAlchemyConnectionField(TeamConnection)


schema = graphene.Schema(query=Query)
