import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField

import euro2021.schemes.match.in_match_model_node
import euro2021.schemes.group.group_node
import euro2021.schemes.tournament_schedule.phase_node
import euro2021.schemes.tournament_schedule.tournament_schedule_node
from euro2021.schemes.match.match_node import MatchConnection
from euro2021.schemes.player.player_node import PlayerConnection
from euro2021.schemes.team.team_node import TeamConnection
from euro2021.schemes.tournament.tournament_node import TournamentConnection


class Query(graphene.ObjectType):
	node = graphene.relay.Node.Field()

	all_players = SQLAlchemyConnectionField(PlayerConnection)
	all_matches = SQLAlchemyConnectionField(MatchConnection)
	all_teams = SQLAlchemyConnectionField(TeamConnection)
	all_tournaments = SQLAlchemyConnectionField(TournamentConnection)


schema = graphene.Schema(query=Query)
