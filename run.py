from flask import Flask
from app import api_bp
from model import db, redis_cache
from config import TestingConfig, BaseConfig

app = Flask(__name__)

t = 0


def create_app(config_filename):
    app.config.from_object(config_filename)
    global t
    if t == 0:
        app.register_blueprint(api_bp, url_prefix='/api')
        t = 1
    if config_filename != TestingConfig:
        db.init_app(app)
        redis_cache.init_app(app)
    return app


if __name__ == "__main__":
    PresentConfig = BaseConfig
    app = create_app(PresentConfig)
    app.run()
