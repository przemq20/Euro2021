from euro2021.db import Base

from sqlalchemy import Column, Integer, String


class TeamModel(Base):
	__tablename__ = 'team'

	id = Column(Integer, primary_key=True)
	team_name = Column(String(255), nullable=False)
