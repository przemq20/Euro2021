from sqlalchemy.orm import relationship

from euro2021.db import Base
from euro2021.models.in_group_model import in_group_table
import euro2021.models.tournament_model

from sqlalchemy import Column, Integer, String, ForeignKey


class GroupModel(Base):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True)
    group_name = Column(String(64), nullable=False)
    tournament_id = Column(Integer, ForeignKey('tournament.id'), nullable=False)

    tournament = relationship('TournamentModel', back_populates='groups')
    teams = relationship('TeamModel', secondary=in_group_table, back_populates='groups')
