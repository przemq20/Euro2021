from euro2021.db import db
from euro2021.models.in_team_model import in_team_table
from euro2021.models import team_model

from sqlalchemy.ext.associationproxy import association_proxy


class PlayerModel(db.Model):
	__tablename__ = 'player'

	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(64), nullable=False)
	last_name = db.Column(db.String(64), nullable=False)
	birth_date = db.Column(db.Date, nullable=False)

	matches_info = db.relationship('InMatchModel', back_populates='player')
	matches_info1 = db.relationship('InMatchStatisticsModel', back_populates='player1')
	teams = db.relationship('TeamModel', secondary=in_team_table, lazy='dynamic', uselist=True, back_populates='players')

	matches = association_proxy('matches_info', 'match')
