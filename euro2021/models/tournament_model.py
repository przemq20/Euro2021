from sqlalchemy.orm import relationship

from db import Base
from models.in_group_model import in_group_table
from models.team_model import TeamModel

from sqlalchemy import Column, Integer, String, ForeignKey, Date, text
from sqlalchemy.ext.associationproxy import association_proxy


class GroupModel(Base):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True)
    tournament_name = Column(String(64), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    location = Column(text, ForeignKey('tournament.id'), nullable=False)

    group_info = relationship('GroupModel', back_populates='tournament_info')
    schedule = relationship('TournamentScheduleModel', back_populates='tournament_about')