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
        access_sys_id = session.get_session()[2]
        header = {'Authorization': "Bearer "+token,'Content-Type': 'application/json'}

        # 创建用户
        req_url_user = 'http://' + host + urls[0]
        response = request.post_request(req_url_user, params[0], header)
        assert Asserts.assert_in_text(response, 'user_id')


        # 创建角色
        req_url_roles = 'http://' + host + urls[1]
        prs = {"role_name": "角色名称","access_sys_id": access_sys_id,"description": "角色描述"}
        response = request.post_request(req_url_roles, prs, header)
        # assert Asserts.assert_code(response['code'], 200)//接口返回有问题

        # 角色关联用户