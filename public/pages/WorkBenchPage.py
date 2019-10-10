#coding=utf-8
import time
from public.common import basepage
from public.pages import LoginPage, CustomerPage


class WorkBench(basepage.Page):
    """工作台模块"""
    def get_name(self):
        """获取右上角名称"""
        name = self.dr.get_text("class->user-name")
        return name

    def get_url(self):
        """获取url"""
        url = self.dr.get_url()
        return url

    def close(self):
        """关闭按钮"""
        self.dr.click("class->close")

    def click_out(self):
        """确定退出"""
        self.dr.click("css->.el-message-box__btns>button:nth-child(2)")

        return LoginPage.Login(self.dr)

    def click_menu(self, menu):
        """点击左侧菜单"""
        self.dr.click("xpath->//span[text()='{}' and @class='menu-title']/..".format(menu))
        # self.dr.click("css->ul[role=menubar]>div:nth-child({})".format(menus[menu]))
        time.sleep(1.5)

    def return_customer(self):
        return CustomerPage.Customer(self.dr)
