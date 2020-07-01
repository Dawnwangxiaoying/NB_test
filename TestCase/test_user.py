# -*- coding: utf-8 -*-

import allure
import pytest
from Common import Request
from Common import Assert
from Conf.Config import Config
from Common import Session
from Params.params import User


class TestUser:

    @pytest.allure.feature('创建用户')
    @allure.severity('blocker')

    @pytest.fixture()
    def test_user_01(self):
        """
        用例描述：正常创建用户-正常创建角色-角色关联权限-用户关联角色
        :return:usreid

        """
        data = User()
        urls = data.url
        params = data.data
        request = Request.Request()
        Asserts = Assert.Assertions()
        conf = Config()
        host = conf.host
        session = Session.Session()
        token = session.get_session()[0]
        print(token)
        req_url = 'http://' + host + urls[0]
        header = {'Authorization': token,'Content-Type': 'application/json','Cookie': 'sk=QPOOFGYHQBDGXGPA3P4E47U7IISSUXDXE7OVCCR5G6VCXJCX5TDI3OGJEX3CRT2L7VYERWCHZJ3U24ISZYDJT4242WVO3MJNCO6R73I'}

        # 创建用户
        response = request.post_request(req_url, params[0], header)
        assert Asserts.assert_in_text(response, 'user_id')
        print(response)
        # order_id = response['body']['order_id']

        # return user_id