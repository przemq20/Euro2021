from sqlalchemy import Column, Integer, ForeignKey, Time, String
from sqlalchemy.orm import relationship

from euro2021.db import Base
import euro2021.models.player_model
import euro2021.models.match_model


class InMatchStatisticsModel(Base):
    __tablename__ = 'in_match_statistics'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('player.id'), primary_key=True)
    match_id = Column(Integer, ForeignKey('match.id'), primary_key=True)
    minute = Column(Integer, nullable=True)
    action = Column(String(64), nullable=True)

    match1 = relationship('MatchModel', back_populates='players_info1')
    player1 = relationship('PlayerModel', back_populates='matches_info1')
