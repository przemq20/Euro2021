from flask import Flask
from flask_graphql import GraphQLView
import euro2021
from euro2021.schemes.schema import schema
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from euro2021.models.tournament_model import TournamentModel
from euro2021.models.tournament_schedule_model import TournamentScheduleModel
from euro2021.models.team_model import TeamModel
from euro2021.models.player_model import PlayerModel
from euro2021.models.phase_model import PhaseModel
from euro2021.models.match_model import MatchModel
from euro2021.models.in_match_model import InMatchModel
# from euro2021.models.in_match_statistics_model import InMatchStatisticsModel
from euro2021.models.group_model import GroupModel


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config')
    app.config.from_pyfile('config.py')

    from euro2021.db import db
    db.init_app(app)

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True,
        )
    )

    admin = Admin(app)
    admin.add_view(ModelView(euro2021.TournamentModel, db.session))
    admin.add_view(ModelView(euro2021.TournamentScheduleModel, db.session))
    admin.add_view(ModelView(euro2021.TeamModel, db.session))
    admin.add_view(ModelView(euro2021.PlayerModel, db.session))
    admin.add_view(ModelView(euro2021.PhaseModel, db.session))
    admin.add_view(ModelView(euro2021.MatchModel, db.session))
    admin.add_view(ModelView(euro2021.InMatchModel, db.session))
    # admin.add_view(ModelView(euro2021.InMatchStatisticsModel, db.session))
    admin.add_view(ModelView(euro2021.GroupModel, db.session))

    return app


# if __name__ == "__main__":
#     create_app().run()
