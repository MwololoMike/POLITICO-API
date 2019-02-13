from flask import Flask
from app.api.v1.views.views_party import politico
from app.api.v1.views.views_office import politico_office


def create_app():
    app = Flask(__name__)
    app.register_blueprint(politico)
    app.register_blueprint(politico_office)
    return app


app = create_app()

if __name__ == "__main__":
    app.run()
