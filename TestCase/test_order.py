# -*- coding: utf-8 -*-

import allure
import pytest
from Params.params import Order
from Common import Request
from Common import Assert
from Conf.Config import Config
from Common import Mysql


class TestOrder:

    @pytest.allure.feature('购买产品支付订单场景1')
    @allure.severity('blocker')
    def test_order_01(self):
        """
        用例描述：购买单个产品-匹配单个计费项下多个策略-支付订单
        """
        data = Order()
        urls = data.url
        params = data.data
        header = data.header
        request = Request.Request()
        Asserts = Assert.Assertions()
        conf = Config()
        host = conf.host
        req_url = 'http://' + host
        api_url = req_url + urls[0]
        sqlinfo = Mysql.Mysqlconnect()

        #创建订单

        response = request.post_request(api_url, params[0], header[0])
        assert Asserts.assert_in_text(response, 'order_id')
        order_id = response['body']['order_id']

        #支付订单
        url = req_url+urls[1].replace('{order_id}', order_id)
        request.post_request(url, params[1], header[0])

        # 断言支付成功，数据库状态变为paid
        info = sqlinfo.info('subscription','select order_status from prd_order where order_id = "%s"'%order_id)
        assert Asserts.assert_exist(info[0], 'paid')

    @allure.severity('critical')
    @allure.story('购买产品支付订单场景2')
    def test_order_02(self):
        """
        用例描述：购买单个产品-匹配同一方案下多个计费项（计费项下的策略都是按包计费）-购买两个产品实例-支付订单
        """
        data = Order()
        urls = data.url
        params = data.data
        header = data.header
        request = Request.Request()
        Asserts = Assert.Assertions()
        conf = Config()
        host = conf.host
        req_url = 'http://' + host
        api_url = req_url + urls[0]
        sqlinfo = Mysql.Mysqlconnect()

        # 创建订单
        response = request.post_request(api_url, params[2], header[0])
        assert Asserts.assert_in_text(response, 'order_id')
        order_id = response['body']['order_id']

        # 支付订单
        url = req_url+urls[1].replace('{order_id}', order_id)
        request.post_request(url, params[1], header[0])

        #断言支付成功，数据库状态变为paid
        info = sqlinfo.info('subscription','select order_status from prd_order where order_id = "%s"'%order_id)
        assert Asserts.assert_exist(info[0], 'paid')

    @allure.severity('critical')
    @allure.story('购买产品支付订单场景3')
    def test_order_03(self):
        """
        用例描述：购买单个产品-匹配同一方案下多个计费项（计费项下的策略有按包计费也有按量计费）-支付订单
        """
        data = Order()
        urls = data.url
        params = data.data
        header = data.header
        request = Request.Request()
        Asserts = Assert.Assertions()
        conf = Config()
        host = conf.host
        req_url = 'http://' + host
        api_url = req_url + urls[0]
        sqlinfo = Mysql.Mysqlconnect()

        # 创建订单
        response = request.post_request(api_url, params[3], header[0])
        assert Asserts.assert_in_text(response, 'order_id')
        order_id = response['body']['order_id']

        # 支付订单
        url = req_url+urls[1].replace('{order_id}', order_id)
        request.post_request(url, params[1], header[0])

        #断言支付成功，数据库状态变为paid
        info = sqlinfo.info('subscription','select order_status from prd_order where order_id = "%s"'%order_id)
        assert Asserts.assert_exist(info[0], 'paid')

    @allure.severity('critical')
    @allure.story('购买产品支付订单场景4')
    def test_order_04(self):
        """
        用例描述：购买单个产品-匹配多个方案（其中包括按量和按包）-支付订单
        """
        data = Order()
        urls = data.url
        params = data.data
        header = data.header
        request = Request.Request()
        Asserts = Assert.Assertions()
        conf = Config()
        host = conf.host
        req_url = 'http://' + host
        api_url = req_url + urls[0]
        sqlinfo = Mysql.Mysqlconnect()

        # 创建订单
        response = request.post_request(api_url, params[4], header[0])
        assert Asserts.assert_in_text(response, 'order_id')
        order_id = response['body']['order_id']

        # 支付订单
        url = req_url+urls[1].replace('{order_id}', order_id)
        request.post_request(url, params[1], header[0])

        #断言支付成功，数据库状态变为paid
        info = sqlinfo.info('subscription','select order_status from prd_order where order_id = "%s"'%order_id)
        assert Asserts.assert_exist(info[0], 'paid')

    @allure.severity('critical')
    @allure.story('购买产品支付订单场景5')
    def test_order_05(self):
        """
        用例描述：购买多个产品-一个按时间使用量一个按资源使用量付费-支付订单
        """
        data = Order()
        urls = data.url
        params = data.data
        header = data.header
        request = Request.Request()
        Asserts = Assert.Assertions()
        conf = Config()
        host = conf.host
        req_url = 'http://' + host
        api_url = req_url + urls[0]
        sqlinfo = Mysql.Mysqlconnect()

        # 创建订单
        response = request.post_request(api_url, params[5], header[0])
        assert Asserts.assert_in_text(response, 'order_id')
        order_id = response['body']['order_id']

        # 支付订单
        url = req_url+urls[1].replace('{order_id}', order_id)
        request.post_request(url, params[1], header[0])

        #断言支付成功，数据库状态变为paid
        info = sqlinfo.info('subscription','select order_status from prd_order where order_id = "%s"'%order_id)
        assert Asserts.assert_exist(info[0], 'paid')