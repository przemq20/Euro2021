from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from euro2021.models.phase_model import PhaseModel


class PhaseNode(SQLAlchemyObjectType):
	"""
	Node that represents phase
	"""
	class Meta:
		model = PhaseModel
		interface = (relay.Node, )
