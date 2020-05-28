from euro2021.db import db
from euro2021.models.in_team_model import in_team_table
from euro2021.models import team_model

from sqlalchemy.ext.associationproxy import association_proxy


class PlayerModel(db.Model):
	__tablename__ = 'player'

	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(64), nullable=False, doc="player's first name")
	last_name = db.Column(db.String(64), nullable=False, doc="player's last name")
	birth_date = db.Column(db.Date, nullable=False, doc="player's birthday")

	matches_info = db.relationship('InMatchModel', back_populates='player')
	teams = db.relationship('TeamModel', secondary=in_team_table, lazy='dynamic', uselist=True, back_populates='players')
	current_team = db.relationship(
		'TeamModel',
		secondary=in_team_table,
		uselist=False,
		primaryjoin='and_(PlayerModel.id==in_team.c.player_id, in_team.c.last_game == None)',
		secondaryjoin='TeamModel.id==in_team.c.team_id',
		viewonly=True
	)

	matches = association_proxy('matches_info', 'match')

	def __repr__(self):
		return self.first_name + " " + self.last_name
