from flask import Blueprint

bp = Blueprint("main", __name__, url_prefix="", static_folder="static", static_url_path="dashboard/static", template_folder="templates")

from app.main import routes