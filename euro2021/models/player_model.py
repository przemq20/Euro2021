from sqlalchemy.orm import relationship

from euro2021.db import Base

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.associationproxy import association_proxy


class PlayerModel(Base):
	__tablename__ = 'player'

	id = Column(Integer, primary_key=True)
	first_name = Column(String(64), nullable=False)
	last_name = Column(String(64), nullable=False)
	birth_date = Column(Date, nullable=False)

	matches_info = relationship('InMatchModel', back_populates='player')

	matches = association_proxy('matches_info', 'match')

