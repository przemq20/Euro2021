import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from euro2021.models.team_model import TeamModel
from euro2021.schemes.group.group_node import GroupNode
from euro2021.schemes.match.match_node import MatchNode
from euro2021.schemes.tournament_schedule.tournament_schedule_node import TournamentScheduleNode


class TeamNode(SQLAlchemyObjectType):
	class Meta:
		model = TeamModel
		interface = (relay.Node, )

	groups = graphene.List(GroupNode)
	scheduled_matches = graphene.List(TournamentScheduleNode)

	def resolve_scheduled_matches(self, info):
		return self.scheduled_matches_as_1 + self.scheduled_matches_as_2


class TeamConnection(relay.Connection):
	class Meta:
		node = TeamNode
