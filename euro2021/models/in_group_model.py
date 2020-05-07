
from euro2021.db import db

in_group_table = db.Table(
    'in_group', db.metadata,
    db.Column('group_id', db.Integer, db.ForeignKey('group.id')),
    db.Column('team_id', db.Integer, db.ForeignKey('team.id'))
)
