from sqlalchemy import Column, Integer, TIMESTAMP, Text, ForeignKey, Table
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship

from euro2021.db import Base


class MatchModel(Base):
	__tablename__ = 'match'

	id = Column(Integer, primary_key=True)
	start_time = Column(TIMESTAMP, nullable=False)
	end_time = Column(TIMESTAMP, nullable=True)
	location = Column(Text, nullable=False)
	tournament_schedule_id = Column(Integer, nullable=True)
	goals_team_1 = Column(Integer, nullable=False)
	goals_team_2 = Column(Integer, nullable=False)

	players_info = relationship("InMatchModel", back_populates='match')

	players = association_proxy('player_info', 'match')
