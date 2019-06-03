from flask import Flask, jsonify
from flask_cors import CORS

from server.apis import (create_v1_api, v1)


def create_app(config_object=None):
    app = Flask(__name__,
                static_folder="./webapp/dist/static",
                template_folder="./webapp/dist")

    app.config.from_object(config_object)
    CORS(app, resources={r"/apis/*": {"origins": "*"}})

    app.register_blueprint(v1, url_prefix='/apis/v1')

    @app.route('/ping')
    def ping():
        return jsonify(dict(pong='pong'))

    create_v1_api()
    return app
