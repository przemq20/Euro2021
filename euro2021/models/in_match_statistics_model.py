from euro2021.db import db
import euro2021.models.player_model
import euro2021.models.match_model


class InMatchStatisticsModel(db.Model):
    __tablename__ = 'in_match_statistics'

    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('in_match.player_id'))
    match_id = db.Column(db.Integer, db.ForeignKey('in_match.match_id'))
    minute = db.Column(db.Integer, nullable=True)
    action = db.Column(db.String(64), nullable=True)


