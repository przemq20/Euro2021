from flask import Flask
from flask_graphql import GraphQLView
from euro2021.schemes.schema import schema


def create_app(config=None):
	app = Flask(__name__, instance_relative_config=True)

	app.config.from_object('config')
	app.config.from_pyfile('config.py')

	from euro2021 import db
	db.init_app(app)

	app.add_url_rule(
		'/graphql',
		view_func=GraphQLView.as_view(
			'graphql',
			schema=schema,
			graphiql=True,
		)
	)

	return app
