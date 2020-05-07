from euro2021.db import db
import euro2021.models.phase_model



class TournamentScheduleModel(db.Model):
    __tablename__ = 'tournament_schedule'

    id = db.Column(db.Integer, primary_key=True)
    tournament_id = db.Column(db.Integer, db.ForeignKey('tournament.id'), nullable=False)
    phase_id = db.Column(db.Integer, db.ForeignKey('phase.id'), nullable=False)
    match_time = db.Column(db.TIMESTAMP, nullable=False)
    match_location = db.Column(db.String, nullable=False)
    team1_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    team2_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

    phase = db.relationship('PhaseModel')
    tournament = db.relationship('TournamentModel', back_populates='schedules')
    match = db.relationship('MatchModel', back_populates='schedule')
    team_1 = db.relationship('TeamModel', foreign_keys=[team1_id], backref='scheduled_matches_as_1')
    team_2 = db.relationship('TeamModel', foreign_keys=[team2_id], backref='scheduled_matches_as_2')

