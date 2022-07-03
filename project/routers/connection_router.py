# PEP8 OK
# -*- coding: utf-8 -*-
from flask import Blueprint
from project.config import Server
from project.services.connection_service import ConnectionService

connection_route = Blueprint("connection_route", __name__)

server = Server()
basePath = server.get_base_path()
CONN_PREFIX = basePath + "/test_connection"


@connection_route.route(CONN_PREFIX + "/", methods=["GET"])
def test_connection():
    result = ConnectionService().test_connection()
    return result
