# -*- coding: utf-8 -*-

"""
封装获取cookie方法

"""

import requests
from Common import Log
from Conf import Config


class Session:
    def __init__(self):
        self.config = Config.Config()
        self.log = Log.MyLog()

    def get_session(self):
        """
        获取session
        :return:
        """
        headers = {"Content-Type": "application/json;charset=UTF-8"}

        login_url = 'http://' + self.config.host + '/v1/login'
        parm = self.config.loginInfo
        response = requests.post(login_url, parm, headers=headers)

        seafiletoken = response.json()['token']
        userid = response.json()['user_id']
        sysid = response.json()['access_sys_id']
        return seafiletoken, userid, sysid



# if __name__ == '__main__':
#     ss = Session()
#     ss.get_session()
#     s1 = ss.get_session()[0]
#     print(s1)