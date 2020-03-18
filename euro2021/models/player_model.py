from euro2021.db import Base

from sqlalchemy import Column, Integer, String, Date


class PlayerModel(Base):
	__tablename__ = 'player'

	id = Column(Integer, primary_key=True)
	first_name = Column(String(64), nullable=False)
	last_name = Column(String(64), nullable=False)
	birth_date = Column(Date, nullable=False)


