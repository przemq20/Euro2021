from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from euro2021.models.match_model import MatchModel


class MatchNode(SQLAlchemyObjectType):
	class Meta:
		model = MatchModel
		interface = (relay.Node, )


class MatchConnection(relay.Connection):
	class Meta:
		node = MatchNode
