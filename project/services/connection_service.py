# PEP8 OK
# -*- coding: utf-8 -*-
from project.business.connection_business import ConnectionBusiness

from .base_service import BaseService


class ConnectionService(BaseService):
    def test_connection(self):
        try:
            result = ConnectionBusiness().test_connection()
            return self.return_success("Sucesso", result)
        except Exception as ex:
            return self.return_exception(ex)
