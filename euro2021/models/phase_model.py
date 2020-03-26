from sqlalchemy import Column, Integer, String

from euro2021.db import Base


class PhaseModel(Base):
    __tablename__ = 'phase'

    id = Column(Integer, primary_key=True)
    phase_name = Column(String(64), nullable=False)
