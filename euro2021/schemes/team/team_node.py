import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from euro2021.models.team_model import TeamModel
from euro2021.schemes.group.group_node import GroupNode


class TeamNode(SQLAlchemyObjectType):
	class Meta:
		model = TeamModel
		interface = (relay.Node, )

	groups = graphene.List(GroupNode)


class TeamConnection(relay.Connection):
	class Meta:
		node = TeamNode
