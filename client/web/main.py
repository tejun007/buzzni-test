from flask import Flask, render_template


def create_app(config_object=None):
    app = Flask(__name__,
                static_folder="./webapp/dist/static",
                template_folder="./webapp/dist")
    app.config.from_object(config_object)

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def index(path):
        return render_template("index.html")
    return app

