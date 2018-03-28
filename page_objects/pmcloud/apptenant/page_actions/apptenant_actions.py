# coding: utf-8
# 导入公共函数Selenium封装类
from libs.pagepubselenium import PagePubSelenium
# 导入企业帐号选择页元素定位
from page_objects.pmcloud.apptenant.page_elements.apptenant import Apptenant
# 导入页面等待装饰器
from libs.timedecorator import timeDecorator

__author__ = "sunxr"
__version__ = "V1.0"


class ApptenantActions(PagePubSelenium):
    """企业帐号选择页操作类"""

    def getApptenantTitle(self):
        """
        获取企业帐号选择页标题.
        :return: 企业账号选择页标题
        """

        return self.getTitle()

    def getSelectText(self):
        """
        获取选择框名称.
        :return: 选择框名称
        """

        return self.getElementText(locator=Apptenant.SELECTTEXT)

    def getSelectApptenantText(self):
        """
        获取选择的具体企业账号的名称.
        :return: 具体企业账号名称
        """

        return self.getElementText(locator=Apptenant.APPTENANT)

    @timeDecorator(1)
    def clickSelect(self):
        """
        点击下拉框.
        :return: 下拉框展开
        """

        self.click(locator=Apptenant.SELECT)

    @timeDecorator(1)
    def clickApptenant(self):
        """
        点击企业帐号.
        """

        self.click(locator=Apptenant.APPTENANT)

    @timeDecorator(1)
    def selectApptenant(self):
        """
        选取测试用企业帐号.
        :return: 选中企业账号
        """

        self.clickSelect()
        self.clickApptenant()

    @timeDecorator(1)
    def clickOKButton(self):
        """
        点击确定按钮.
        :return: 页面跳转到工作台页面
        """

        self.click(locator=Apptenant.OKBTN)

    def apptenantLogin(self):
        """
        选取测试用企业帐号后登陆.
        :return: 登录到工作台
        """

        self.selectApptenant()
        self.clickOKButton()
