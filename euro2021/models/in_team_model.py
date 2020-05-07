from euro2021.db import db

in_team_table = db.Table(
	'in_team', db.metadata,
	db.Column('player_id', db.Integer, db.ForeignKey('player.id')),
	db.Column('team_id', db.Integer, db.ForeignKey('team.id'))
)
