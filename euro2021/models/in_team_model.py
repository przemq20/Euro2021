from sqlalchemy import Table, Column, Integer, ForeignKey

from db import Base

in_team_table = Table(
	'in_team', Base.metadata,
	Column('player_id', Integer, ForeignKey('player.id')),
	Column('team_id', Integer, ForeignKey('team.id'))
)
