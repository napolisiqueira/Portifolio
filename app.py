import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)


    #imports routes
    from controllers import routes
    # Register routes Bluprints
    app.register_blueprint(routes.index)

    return app