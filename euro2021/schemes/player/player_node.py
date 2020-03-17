import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from euro2021.models.player_model import PlayerModel


class PlayerNode(SQLAlchemyObjectType):
	class Meta:
		model = PlayerModel
		interface = (graphene.relay.Node, )
		# exclude_fields = ('id',)


class PlayerConnection(graphene.relay.Connection):
	class Meta:
		node = PlayerNode
