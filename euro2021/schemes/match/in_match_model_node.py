from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from euro2021.models.in_match_model import InMatchModel


class InMatchNode(SQLAlchemyObjectType):
	class Meta:
		model = InMatchModel
		interface = (relay.Node, )
