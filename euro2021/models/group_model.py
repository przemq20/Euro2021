from euro2021.db import db
from euro2021.models.in_group_model import in_group_table
import euro2021.models.tournament_model


class GroupModel(db.Model):
    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(64), nullable=False)
    tournament_id = db.Column(db.Integer, db.ForeignKey('tournament.id'), nullable=False)

    tournament = db.relationship('TournamentModel', back_populates='groups')
    teams = db.relationship('TeamModel', secondary=in_group_table, back_populates='groups')
