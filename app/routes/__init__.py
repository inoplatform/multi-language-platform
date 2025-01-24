from flask import Blueprint

main_bp = Blueprint('main', __name__)
language_bp = Blueprint('language', __name__, url_prefix='/language')

from app.routes import main_routes, language_routes
