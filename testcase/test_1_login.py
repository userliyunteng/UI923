#coding=utf-8
import time
import unittest

from public.common import mytest
from public.pages import LoginPage
from ddt import ddt,data,unpack
from loguru import logger
from public.common.datainfo import get_test_case_data, data_info
from public.common.get_img import screenshot_about_case
from BeautifulReport import BeautifulReport


@ddt
class TestLogin(mytest.MyTest):
    """登录模块"""

    @screenshot_about_case
    @data(*get_test_case_data(data_info, 'test_01_login'))
    def test_01_login(self, data):
        """正常登录"""
        test_data = data['data']
        test_assert = data['assertion']
        login = LoginPage.Login(self.dr)
        ele = login.login(test_data['username'],test_data['pw'])
        login.exist_loading()
        username = ele.get_name()
        url = ele.get_url()
        self.assertIn(url,test_assert['title'])
        self.assertIn(username, test_assert['username'])



    # @screenshot_about_case
    # def test_baidu(self):
    #     """百度搜索"""
    #     m = LoginPage.Login(self.dr)
    #     m.input_v()
    #     m.click_btn()
    #     m.click_one()
    #     m.into_newwin()
    #     url = m.get_url()
    #     self.assertIn('http://sz.test.zelinedu.net', url)

