import os

from flask import Flask

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

engine = create_engine(os.environ['SQLALCHEMY_URI'])

Session = scoped_session(sessionmaker(
	autocommit=False,
	autoflush=False,
	bind=engine
))
Base.query = Session.query_property()

def close_db(e=None) -> None:
	Session.remove()


def init_app(app: Flask) -> None:
	app.teardown_appcontext(close_db)
