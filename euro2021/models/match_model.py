from sqlalchemy import Column, Integer, TIMESTAMP, Text

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
