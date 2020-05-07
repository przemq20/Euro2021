from sqlalchemy.ext.hybrid import hybrid_property

from euro2021.db import db
from euro2021.models.in_group_model import in_group_table
from euro2021.models.in_team_model import in_team_table
import euro2021.models.group_model


class TeamModel(db.Model):
	__tablename__ = 'team'

	id = db.Column(db.Integer, primary_key=True)
	team_name = db.Column(db.String(255), nullable=False)

	players = db.relationship('PlayerModel', secondary=in_team_table, back_populates='teams')
	groups = db.relationship('GroupModel', secondary=in_group_table, back_populates='teams')

	@hybrid_property
	def scheduled_matches(self):
		return self.scheduled_matches_as_1 + self.scheduled_matches_as_2
