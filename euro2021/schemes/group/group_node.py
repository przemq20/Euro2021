from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from euro2021.models.group_model import GroupModel


class GroupNode(SQLAlchemyObjectType):
	"""
	Node that represents group
	"""
	class Meta:
		model = GroupModel
		interface = (relay.Node, )
		exclude_fields = ('tournament_id',)
