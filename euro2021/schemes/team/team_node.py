from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from euro2021.models.team_model import TeamModel


class TeamNode(SQLAlchemyObjectType):
	class Meta:
		model = TeamModel
		interface = (relay.Node, )


class TeamConnection(relay.Connection):
	class Meta:
		node = TeamNode
