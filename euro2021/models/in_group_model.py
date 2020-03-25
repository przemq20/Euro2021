from sqlalchemy import Table, Column, Integer, ForeignKey

from euro2021.db import Base

in_group_table = Table(
    'in_group', Base.metadata,
    Column('group_id', Integer, ForeignKey('group.id')),
    Column('team_id', Integer, ForeignKey('team.id'))
)
