from euro2021.db import db


class PhaseModel(db.Model):
    __tablename__ = 'phase'

    id = db.Column(db.Integer, primary_key=True)
    phase_name = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return self.phase_name
