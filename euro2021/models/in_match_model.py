from euro2021.db import db
import euro2021.models.player_model
import euro2021.models.match_model


class InMatchModel(db.Model):
	__tablename__ = 'in_match'

	player_id = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True)
	match_id = db.Column(db.Integer, db.ForeignKey('match.id'), primary_key=True)
	started_at = db.Column(db.Time, nullable=True, doc="time when player started playing")
	ended_at = db.Column(db.Time, nullable=True, doc="time when player ended playing")

	match = db.relationship('MatchModel', back_populates='players_info')
	player = db.relationship('PlayerModel', back_populates='matches_info')
