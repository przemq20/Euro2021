from sqlalchemy import Column, Integer, ForeignKey, Time
from sqlalchemy.orm import relationship

from euro2021.db import Base
import euro2021.models.player_model
import euro2021.models.match_model


class InMatchModel(Base):
	__tablename__ = 'in_match'

	player_id = Column(Integer, ForeignKey('player.id'), primary_key=True)
	match_id = Column(Integer, ForeignKey('match.id'), primary_key=True)
	started_at = Column(Time, nullable=True)
	ended_at = Column(Time, nullable=True)

	match = relationship('MatchModel', back_populates='players_info')
	player = relationship('PlayerModel', back_populates='matches_info')
