from sqlalchemy.orm import relationship

from euro2021.db import Base
import euro2021.models.tournament_schedule_model

from sqlalchemy import Column, Integer, String, ForeignKey, Date


class TournamentModel(Base):
    __tablename__ = 'tournament'

    id = Column(Integer, primary_key=True)
    tournament_name = Column(String(255), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    location = Column(String, ForeignKey('tournament.id'), nullable=False)

    groups = relationship('GroupModel', back_populates='tournament')
    schedules = relationship('TournamentScheduleModel', back_populates='tournament')
