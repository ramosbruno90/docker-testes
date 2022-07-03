# PEP8 OK
# -*- coding: utf-8 -*-

from project.repositories.user.user_repository import UserRepository


class UserBusiness():

    def user(self):
        return list(UserRepository().select().where(UserRepository.is_active == True).dicts())
