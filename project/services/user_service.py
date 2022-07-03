# PEP8 OK
# -*- coding: utf-8 -*-
from project.business.user_business import UserBusiness

from .base_service import BaseService


class UserService(BaseService):
    def user(self):
        try:
            result = UserBusiness().user()
            return self.return_success("Sucesso", result)
        except Exception as ex:
            return self.return_exception(ex)
