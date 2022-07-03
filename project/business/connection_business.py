# PEP8 OK
# -*- coding: utf-8 -*-
import speedtest
from project.framework.exception.exceptions import BusinessException


class ConnectionBusiness():

    def test_connection(self):

        try:

            test = speedtest.Speedtest()

            # download
            down = test.download()
            rsDown = round(down)
            fDown = int(rsDown / 1e+6)

            # upload
            upload = test.upload()
            rsUp = round(upload)
            fUp = int(rsUp / 1e+6)

            return {
                "Download": f'{fDown} mb/s',
                "Upload": f'{fUp} mb/s'
            }
        except:
            raise BusinessException('Teste não pode ser realizado"')
