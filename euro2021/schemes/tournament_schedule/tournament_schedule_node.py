from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from euro2021.models.tournament_schedule_model import TournamentScheduleModel


class TournamentScheduleNode(SQLAlchemyObjectType):
	class Meta:
		model = TournamentScheduleModel
		interface = (relay.Node, )
		exclude_fields = ('tournament_id', 'phase_id', 'team1_id', 'team2_id')
