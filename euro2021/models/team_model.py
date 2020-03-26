from sqlalchemy.ext.hybrid import hybrid_property

from euro2021.db import Base
from euro2021.models.in_group_model import in_group_table
from euro2021.models.in_team_model import in_team_table
import euro2021.models.group_model

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class TeamModel(Base):
	__tablename__ = 'team'

	id = Column(Integer, primary_key=True)
	team_name = Column(String(255), nullable=False)

	players = relationship('PlayerModel', secondary=in_team_table, back_populates='teams')
	groups = relationship('GroupModel', secondary=in_group_table, back_populates='teams')

	@hybrid_property
	def scheduled_matches(self):
		return self.scheduled_matches_as_1 + self.scheduled_matches_as_2
