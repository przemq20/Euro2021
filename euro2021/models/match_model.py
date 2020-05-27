from sqlalchemy.ext.associationproxy import association_proxy

from euro2021.models import in_match_model
from euro2021.db import db


class MatchModel(db.Model):
	__tablename__ = 'match'

	id = db.Column(db.Integer, primary_key=True)
	start_time = db.Column(db.TIMESTAMP, nullable=False)
	end_time = db.Column(db.TIMESTAMP, nullable=True)
	location = db.Column(db.Text, nullable=False)
	tournament_schedule_id = db.Column(db.Integer, db.ForeignKey('tournament_schedule.id'), nullable=True)
	goals_team_1 = db.Column(db.Integer, nullable=False)
	goals_team_2 = db.Column(db.Integer, nullable=False)

	players_info = db.relationship('InMatchModel', back_populates='match')
	schedule = db.relationship('TournamentScheduleModel', back_populates='match')

	players = association_proxy('player_info', 'match')
