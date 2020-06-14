# -*- coding: utf-8 -*-

from configparser import ConfigParser
from Common import Log
import os


class Config:
    os.environ['Environ'] = 'test'
    # titles:
    TITLE_DEBUG = "private_test"
    TITLE_RELEASE = "online_release"

    # values:
    VALUE_TESTER = "tester"
    VALUE_ENVIRONMENT = "environment"
    VALUE_VERSION_CODE = "versionCode"
    VALUE_HOST = "host"
    VALUE_LOGIN_INFO = "loginInfo"
    VALUE_MYSQL_HOST = "Mysqlhost"
    VALUE_MYSQL_PORT = "Mysqlport"
    VALUE_MYSQL_USER = "Mysqluser"
    VALUE_MYSQL_PASSWD = "Mysqlpasswd"

    # path
    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

    def __init__(self):
        """
        初始化
        """
        self.config = ConfigParser()
        self.log = Log.MyLog()
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
        self.xml_report_path = Config.path_dir+'/Report/xml'
        self.html_report_path = Config.path_dir+'/Report/html'

        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保配置文件存在！")

        self.config.read(self.conf_path, encoding='utf-8')

        if os.environ['Environ'] == 'test':
            self.tester = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_TESTER)
            self.environment = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_ENVIRONMENT)
            self.versionCode = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_VERSION_CODE)
            self.host = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_HOST)
            self.loginInfo = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_LOGIN_INFO)
            self.Mysqlhost = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_MYSQL_HOST)
            self.Mysqlport = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_MYSQL_PORT)
            self.Mysqluser= self.get_conf(Config.TITLE_DEBUG, Config.VALUE_MYSQL_USER)
            self.Mysqlpasswd = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_MYSQL_PASSWD)
        if os.environ['Environ'] == 'release':
            self.tester = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_TESTER)
            self.environment = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_ENVIRONMENT)
            self.versionCode = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_VERSION_CODE)
            self.host = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_HOST)
            self.loginInfo = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_LOGIN_INFO)
            self.Mysqlhost = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_MYSQL_HOST)
            self.Mysqlport = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_MYSQL_PORT)
            self.Mysqluser = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_MYSQL_USER)
            self.Mysqlpasswd = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_MYSQL_PASSWD)

    def get_conf(self, title, value):
        """
        配置文件读取
        :param title:
        :param value:
        :return:
        """
        return self.config.get(title, value)
