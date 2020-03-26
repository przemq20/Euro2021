from sqlalchemy.orm import relationship

from euro2021.db import Base
import euro2021.models.phase_model

from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP


class TournamentScheduleModel(Base):
    __tablename__ = 'tournament_schedule'

    id = Column(Integer, primary_key=True)
    tournament_id = Column(Integer, ForeignKey('tournament.id'), nullable=False)
    phase_id = Column(Integer, ForeignKey('phase.id'), nullable=False)
    match_time = Column(TIMESTAMP, nullable=False)
    match_location = Column(String, nullable=False)
    team1_id = Column(Integer, ForeignKey('team.id'), nullable=False)
    team2_id = Column(Integer, ForeignKey('team.id'), nullable=False)

    phase = relationship('PhaseModel')
    tournament = relationship('TournamentModel', back_populates='schedules')
    match = relationship('MatchModel', back_populates='schedule')
    team_1 = relationship('TeamModel', foreign_keys=[team1_id], backref='scheduled_matches_as_1')
    team_2 = relationship('TeamModel', foreign_keys=[team2_id], backref='scheduled_matches_as_2')

