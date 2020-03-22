from sqlalchemy.orm import relationship

from db import Base
from models.in_group_model import in_group_table
from models.team_model import TeamModel

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.associationproxy import association_proxy


class GroupModel(Base):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True)
    group_name = Column(String(64), nullable=False)
    tournament_id = Column(Integer, ForeignKey('tournament.id'), nullable=False)

    tournament_info = relationship('TournamentModel', back_populates='group_info')
    groups = relationship('InGroupModel', secondary=in_group_table, back_populates='?')