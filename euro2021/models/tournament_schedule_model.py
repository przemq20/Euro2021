from sqlalchemy.orm import relationship

from euro2021.db import Base
from euro2021.models.in_group_model import in_group_table
from euro2021.models.team_model import TeamModel
from euro2021.models.phase_model import PhaseModel
from euro2021.models.tournament_model import TournamentModel

from sqlalchemy import Column, Integer, String, ForeignKey, Date, text, TIMESTAMP, Text
from sqlalchemy.ext.associationproxy import association_proxy


class TournamentScheduleModel(Base):
    __tablename__ = 'tournament_schedule'

    id = Column(Integer, primary_key=True)
    tournament_id = Column(Integer, ForeignKey('tournament.id'), nullable=False)
    phase_id = Column(Integer, ForeignKey('phase.id'), nullable=False)
    match_time = Column(TIMESTAMP,ForeignKey('match.id'), nullable=False)
    match_location = Column(Text, nullable=False)
    team1_id = Column(Integer, ForeignKey('team.id'), nullable=False)
    team2_id = Column(Integer, ForeignKey('team.id'), nullable=False)

    phase = relationship('PhaseModel', back_populates='in_tournament')
    tournament_about = relationship('TournamentModel', back_populates='schedule')
