from sqlalchemy.ext.associationproxy import association_proxy

from euro2021.models import in_match_model
from euro2021.db import db


class MatchModel(db.Model):
	__tablename__ = 'match'

	id = db.Column(db.Integer, primary_key=True)
	start_time = db.Column(db.TIMESTAMP, nullable=False, doc="start time")
	end_time = db.Column(db.TIMESTAMP, nullable=True, doc="end time")
	location = db.Column(db.Text, nullable=False, doc="match location")
	tournament_schedule_id = db.Column(db.Integer, db.ForeignKey('tournament_schedule.id'), nullable=True)
	goals_team_1 = db.Column(db.Integer, nullable=False, doc="goals earned by first team")
	goals_team_2 = db.Column(db.Integer, nullable=False, doc="goals earned by second team")

	players_info = db.relationship('InMatchModel', back_populates='match')
	schedule = db.relationship('TournamentScheduleModel', back_populates='match')

	players = association_proxy('player_info', 'match')

	def __repr__(self):
		return "Match {}-{}".format(self.schedule.team_1.team_name, self.schedule.team_2.team_name)
