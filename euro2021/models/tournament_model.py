from euro2021.db import db
import euro2021.models.tournament_schedule_model


class TournamentModel(db.Model):
    __tablename__ = 'tournament'

    id = db.Column(db.Integer, primary_key=True)
    tournament_name = db.Column(db.String(255), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    location = db.Column(db.String, db.ForeignKey('tournament.id'), nullable=False)

    groups = db.relationship('GroupModel', back_populates='tournament')
    schedules = db.relationship('TournamentScheduleModel', back_populates='tournament')

    def __repr__(self):
        return self.tournament_name
