from flask import Blueprint
from flask_restx import Api

blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(
    blueprint,
    title="Mazpeople Escucha",
    version="1.0",
    description="Microservice to manage and create surveys",
    doc="/swagger/"
)

if api is not None:
    # Users
    from project.app.users.entrypoints.api.userView import api as ns_user
    api.add_namespace(ns_user)

    # Schedules
    from project.app.schedules.entrypoints.api.schedulesView import api as ns_schedules
    api.add_namespace(ns_schedules)
