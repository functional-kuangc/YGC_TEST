# coding: utf-8
# 导入公共函数Selenium封装类
from libs.pagepubselenium import PagePubSelenium
# 导入友工程登录页元素定位
from page_objects.pmcloud.login.page_elements.login import PMCloudLogin
# 导入页面等待装饰器
from libs.timedecorator import timeDecorator

__author__ = "sunxr"
__version__ = "V1.0"


class PMCloudLoginActions(PagePubSelenium):
    """友工程登录页操作类"""

    @timeDecorator(1)
    def typeUsername(self):
        """
        输入用户名.
        """

        self.sendText(locator=PMCloudLogin.USERNAME, text=PMCloudLogin.USER)

    @timeDecorator(1)
    def typePassword(self):
        """
        输入密码
        """

        self.sendText(locator=PMCloudLogin.PASSWORD, text=PMCloudLogin.PSW)

    @timeDecorator(1)
    def isRememberPassword(self, remember_selected=False):
        """
        是否勾选记住密码.
        :param remember_selected: 勾选为True，不勾选为False
        """

        if remember_selected:
            """勾选记住密码"""
            if not self.isElementSelected(locator=PMCloudLogin.REMEMBER):
                self.click(locator=PMCloudLogin.REMEMBER)
        else:
            """不勾选记住密码"""
            if self.isElementSelected(locator=PMCloudLogin.REMEMBER):
                self.click(locator=PMCloudLogin.REMEMBER)

    @timeDecorator(5)
    def clickLoginButton(self):
        """
        点击登录按钮.
        :return: 跳转到登录后页面
        """

        self.click(locator=PMCloudLogin.LOGINBTN)

    def pmcloudLogin(self, remember_selected=False):
        """
        登录账号全流程操作.
        :param remember_selected: 是否记住密码，勾选为True，不勾选为False
        :return: 跳转到登录后页面
        """

        self.typeUsername()
        self.typePassword()
        self.isRememberPassword(remember_selected)
        self.clickLoginButton()
