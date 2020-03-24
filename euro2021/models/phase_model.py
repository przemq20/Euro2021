from sqlalchemy import Column, Integer, TIMESTAMP, Text, ForeignKey, Table
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship

from euro2021.db import Base


class PhaseModel(Base):
    __tablename__ = 'phase'

    id = Column(Integer, primary_key=True)
    phase_name = Column(Integer, nullable=False)

    in_tournament = relationship('PhaseModel',back_populates='phase')