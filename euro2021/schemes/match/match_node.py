from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from euro2021.models.match_model import MatchModel


class MatchNode(SQLAlchemyObjectType):
	"""
	Node that represents match
	"""
	class Meta:
		model = MatchModel
		interface = (relay.Node, )
		exclude_fields = ("tournament_schedule_id",)


class MatchConnection(relay.Connection):
	class Meta:
		node = MatchNode
