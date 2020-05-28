from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from euro2021.models.tournament_model import TournamentModel


class TournamentNode(SQLAlchemyObjectType):
	"""
	Node that represents tournament
	"""
	class Meta:
		model = TournamentModel
		interface = (relay.Node, )


class TournamentConnection(relay.Connection):
	class Meta:
		node = TournamentNode
