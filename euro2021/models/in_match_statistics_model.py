# from euro2021.db import db
# import euro2021.models.player_model
# import euro2021.models.match_model
#
#
# class InMatchStatisticsModel(db.Model):
#     __tablename__ = 'in_match_statistics'
#
#     id = db.Column(db.Integer, primary_key=True)
#     player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
#     match_id = db.Column(db.Integer, db.ForeignKey('match.id'))
#     minute = db.Column(db.Integer, nullable=True)
#     action = db.Column(db.String(64), nullable=True)
#
#     match = db.relationship('MatchModel', back_populates='players_info')
#     player = db.relationship('PlayerModel', back_populates='matches_info')
#
#     match1 = db.relationship('MatchModel', back_populates='players_info1')
#     player1 = db.relationship('PlayerModel', back_populates='matches_info1')
