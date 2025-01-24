from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_babel import Babel
from config import Config

db = SQLAlchemy()
migrate = Migrate()
babel = Babel()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    babel.init_app(app)

    from app.routes import main_bp, language_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(language_bp)

    return app
