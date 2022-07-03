# PEP8 OK
# -*- coding: utf-8 -*-
from flask import Blueprint
from project.config import Server
from project.services.user_service import UserService

user_route = Blueprint("user_route", __name__)

server = Server()
basePath = server.get_base_path()
USER_PREFIX = basePath + "/user"


@user_route.route(USER_PREFIX + "/", methods=["GET"])
def user():
    result = UserService().user()
    return result
