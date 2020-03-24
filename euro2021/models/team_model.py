from euro2021.db import Base
from euro2021.models.in_team_model import in_team_table

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class TeamModel(Base):
	__tablename__ = 'team'

	id = Column(Integer, primary_key=True)
	team_name = Column(String(255), nullable=False)

	players = relationship('PlayerModel', secondary=in_team_table, back_populates='teams')



