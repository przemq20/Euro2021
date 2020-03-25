from sqlalchemy.orm import relationship

from euro2021.db import Base
from euro2021.models.in_team_model import in_team_table
from euro2021.models.team_model import TeamModel

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.associationproxy import association_proxy


class PlayerModel(Base):
	__tablename__ = 'player'

	id = Column(Integer, primary_key=True)
	first_name = Column(String(64), nullable=False)
	last_name = Column(String(64), nullable=False)
	birth_date = Column(Date, nullable=False)

	matches_info = relationship('InMatchModel', back_populates='player')
	teams = relationship('TeamModel', secondary=in_team_table, back_populates='players')

	matches = association_proxy('matches_info', 'match')
