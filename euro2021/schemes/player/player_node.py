from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from euro2021.models.player_model import PlayerModel


class PlayerNode(SQLAlchemyObjectType):
	"""
	Node that represents player
	"""
	class Meta:
		model = PlayerModel
		interface = (relay.Node, )


class PlayerConnection(relay.Connection):
	class Meta:
		node = PlayerNode
