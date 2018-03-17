# coding: utf-8
# 导入公共函数Selenium封装类
from libs.pagepubselenium import PagePubSelenium
# 导入添加参与企业元素定位
from page_objects.pmcloud.project.page_elements.project_team_enterprise_add import ProjectTeamEnterpriseAdd
# 导入页面等待装饰器
from libs.timedecorator import timeDecorator

__author__ = "sunxr"
__version__ = "V1.0"


class ProjectTeamEnterpriseAddActions(PagePubSelenium):
    """添加参与企业操作类"""

    @timeDecorator(1)
    def clearSearchKeyword(self):
        """
        清空搜索框中关键字.
        """

        if self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN4) == "取消":
            self.clear(locator=ProjectTeamEnterpriseAdd.SEARCHINPUT4)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN6) == "取消":
            self.clear(locator=ProjectTeamEnterpriseAdd.SEARCHINPUT6)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN3) == "取消":
            self.clear(locator=ProjectTeamEnterpriseAdd.SEARCHINPUT3)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN3) == "取消":
            self.clear(locator=ProjectTeamEnterpriseAdd.SEARCHINPUT5)

    @timeDecorator(1)
    def typeSearchKeyword(self, keyword="sxr"):
        """
        在搜索框中输入搜索关键字.
        :param keyword: 搜索关键字
        """

        if self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN4) == "取消":
            self.sendText(locator=ProjectTeamEnterpriseAdd.SEARCHINPUT4, text=keyword)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN6) == "取消":
            self.sendText(locator=ProjectTeamEnterpriseAdd.SEARCHINPUT6, text=keyword)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN3) == "取消":
            self.sendText(locator=ProjectTeamEnterpriseAdd.SEARCHINPUT3, text=keyword)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN5) == "取消":
            self.sendText(locator=ProjectTeamEnterpriseAdd.SEARCHINPUT5, text=keyword)

    @timeDecorator(3)
    def clickSearchButton(self):
        """
        点击搜索按钮.
        :return: 搜索结果
        """

        if self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN4) == "取消":
            self.click(locator=ProjectTeamEnterpriseAdd.SEARCHBUTTON4)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN6) == "取消":
            self.click(locator=ProjectTeamEnterpriseAdd.SEARCHBUTTON6)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN3) == "取消":
            self.click(locator=ProjectTeamEnterpriseAdd.SEARCHBUTTON3)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN5) == "取消":
            self.click(locator=ProjectTeamEnterpriseAdd.SEARCHBUTTON5)

    @timeDecorator(1)
    def selectFirstEnterprise(self):
        """
        从搜索结果中选择第一个企业.
        """

        if self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN4) == "取消":
            self.click(locator=ProjectTeamEnterpriseAdd.SELECTSEARCHLIST41)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN6) == "取消":
            self.click(locator=ProjectTeamEnterpriseAdd.SELECTSEARCHLIST61)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN3) == "取消":
            self.click(locator=ProjectTeamEnterpriseAdd.SELECTSEARCHLIST31)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN5) == "取消":
            self.click(locator=ProjectTeamEnterpriseAdd.SELECTSEARCHLIST51)

    @timeDecorator(1)
    def selectSecondEnterprise(self):
        """
        从搜索结果中选择第二个企业.
        """

        if self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN4) == "取消":
            self.click(locator=ProjectTeamEnterpriseAdd.SELECTSEARCHLIST42)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN6) == "取消":
            self.click(locator=ProjectTeamEnterpriseAdd.SELECTSEARCHLIST62)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN4) == "取消":
            self.click(locator=ProjectTeamEnterpriseAdd.SELECTSEARCHLIST32)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN5) == "取消":
            self.click(locator=ProjectTeamEnterpriseAdd.SELECTSEARCHLIST52)

    @timeDecorator(1)
    def clickOKButton(self):
        """
        点击确定按钮.
        """

        if self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN4) == "取消":
            self.click(locator=ProjectTeamEnterpriseAdd.OKBTN4)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN6) == "取消":
            self.click(locator=ProjectTeamEnterpriseAdd.OKBTN6)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN3) == "取消":
            self.click(locator=ProjectTeamEnterpriseAdd.OKBTN3)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN5) == "取消":
            self.click(locator=ProjectTeamEnterpriseAdd.OKBTN5)

    @timeDecorator(1)
    def clickCancelButton(self):
        """
        点击取消按钮.
        """

        if self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN4) == "取消":
            self.click(locator=ProjectTeamEnterpriseAdd.CANCELBTN4)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN6) == "取消":
            self.click(locator=ProjectTeamEnterpriseAdd.CANCELBTN6)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN3) == "取消":
            self.click(locator=ProjectTeamEnterpriseAdd.CANCELBTN3)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN5) == "取消":
            self.click(locator=ProjectTeamEnterpriseAdd.CANCELBTN5)

    @timeDecorator(1)
    def clickCloseButton(self):
        """
        点击右上角关闭按钮.
        """

        if self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN4) == "取消":
            self.click(locator=ProjectTeamEnterpriseAdd.CLOSEBTN4)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN6) == "取消":
            self.click(locator=ProjectTeamEnterpriseAdd.CLOSEBTN6)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN3) == "取消":
            self.click(locator=ProjectTeamEnterpriseAdd.CLOSEBTN3)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN5) == "取消":
            self.click(locator=ProjectTeamEnterpriseAdd.CLOSEBTN5)

    @timeDecorator(1)
    def getToastMsg(self):
        """
        获取toast提示信息.
        :return: toast提示信息
        """

        if self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN4) == "取消":
            return self.getElementText(locator=ProjectTeamEnterpriseAdd.ENTERPRISEADDTOAST5)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN6) == "取消":
            return self.getElementText(locator=ProjectTeamEnterpriseAdd.ENTERPRISEADDTOAST7)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN3) == "取消":
            return self.getElementText(locator=ProjectTeamEnterpriseAdd.ENTERPRISEADDTOAST4)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN5) == "取消":
            return self.getElementText(locator=ProjectTeamEnterpriseAdd.ENTERPRISEADDTOAST6)

    @timeDecorator(1)
    def closeToast(self):
        """
        关闭toast提示.
        """

        if self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN4) == "取消":
            return self.click(locator=ProjectTeamEnterpriseAdd.ENTERPRISEADDTOASTCLOSE5)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN6) == "取消":
            return self.click(locator=ProjectTeamEnterpriseAdd.ENTERPRISEADDTOASTCLOSE7)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN3) == "取消":
            return self.click(locator=ProjectTeamEnterpriseAdd.ENTERPRISEADDTOASTCLOSE4)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN5) == "取消":
            return self.click(locator=ProjectTeamEnterpriseAdd.ENTERPRISEADDTOASTCLOSE6)

    # 企业列表操作
    @timeDecorator(1)
    def getEnterpriseListMsg(self):
        """
        添加参与企业列表为空时的提示信息.
        :return: 提示信息
        """

        if self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN4) == "取消":
            return self.getElementText(locator=ProjectTeamEnterpriseAdd.ENTERPRISELISTMSG4)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN6) == "取消":
            return self.getElementText(locator=ProjectTeamEnterpriseAdd.ENTERPRISELISTMSG6)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN3) == "取消":
            return self.getElementText(locator=ProjectTeamEnterpriseAdd.ENTERPRISELISTMSG3)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN5) == "取消":
            return self.getElementText(locator=ProjectTeamEnterpriseAdd.ENTERPRISELISTMSG5)

    @timeDecorator(1)
    def clickFirstEnterpriseType(self):
        """
        点击第一个参与方的参与方类型控件.
        """

        if self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN4) == "取消":
            return self.click(locator=ProjectTeamEnterpriseAdd.FIRSTENTERPRISETYPE4)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN6) == "取消":
            return self.click(locator=ProjectTeamEnterpriseAdd.FIRSTENTERPRISETYPE6)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN3) == "取消":
            return self.click(locator=ProjectTeamEnterpriseAdd.FIRSTENTERPRISETYPE3)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN5) == "取消":
            return self.click(locator=ProjectTeamEnterpriseAdd.FIRSTENTERPRISETYPE5)

    @timeDecorator(1)
    def clickSecondEnterpriseType(self):
        """
        点击第二个参与方的参与方类型控件.
        """

        if self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN4) == "取消":
            return self.click(locator=ProjectTeamEnterpriseAdd.SECONDENTERPRISETYPE4)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN6) == "取消":
            return self.click(locator=ProjectTeamEnterpriseAdd.SECONDENTERPRISETYPE6)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN3) == "取消":
            return self.click(locator=ProjectTeamEnterpriseAdd.SECONDENTERPRISETYPE3)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN5) == "取消":
            return self.click(locator=ProjectTeamEnterpriseAdd.SECONDENTERPRISETYPE5)

    @timeDecorator(1)
    def selectFirstEnterpriseTypeSG(self):
        """
        选择第一个企业为施工方.
        """

        if self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN4) == "取消":
            return self.click(locator=ProjectTeamEnterpriseAdd.FIRSTENTERPRISETYPESELECTSG5)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN6) == "取消":
            return self.click(locator=ProjectTeamEnterpriseAdd.FIRSTENTERPRISETYPESELECTSG7)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN3) == "取消":
            return self.click(locator=ProjectTeamEnterpriseAdd.FIRSTENTERPRISETYPESELECTSG4)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN5) == "取消":
            return self.click(locator=ProjectTeamEnterpriseAdd.FIRSTENTERPRISETYPESELECTSG6)

    @timeDecorator(1)
    def selectSecondEnterpriseTypeJL(self):
        """
        选择第二个企业为监理方.
        """

        if self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN4) == "取消":
            return self.click(locator=ProjectTeamEnterpriseAdd.SECONDENTERPRISETYPESELECTJL6)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN6) == "取消":
            return self.click(locator=ProjectTeamEnterpriseAdd.SECONDENTERPRISETYPESELECTJL8)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN3) == "取消":
            return self.click(locator=ProjectTeamEnterpriseAdd.SECONDENTERPRISETYPESELECTJL5)
        elif self.getElementText(locator=ProjectTeamEnterpriseAdd.CANCELBTN5) == "取消":
            return self.click(locator=ProjectTeamEnterpriseAdd.SECONDENTERPRISETYPESELECTJL7)

    # 流程类操作
    def searchEnterprise(self):
        """
        搜索并选择两个参与方全流程.
        """

        self.clearSearchKeyword()
        self.typeSearchKeyword()
        self.clickSearchButton()
        self.selectFirstEnterprise()
        self.clearSearchKeyword()
        self.typeSearchKeyword()
        self.clickSearchButton()
        self.selectSecondEnterprise()

    def selectEnterpriseType(self):
        """
        设置两个参与方分别为施工方和监理方全流程.
        :return:
        """

        self.clickFirstEnterpriseType()
        self.selectFirstEnterpriseTypeSG()
        self.clickSecondEnterpriseType()
        self.selectSecondEnterpriseTypeJL()

    def saveEnterpriseAdd(self):
        """
        添加参与方并保存.
        """

        self.searchEnterprise()
        self.selectEnterpriseType()
        self.clickOKButton()

    def cancelEnterpriseAddByCancelButton(self):
        """
        通过取消按钮取消添加参与方.
        """

        self.searchEnterprise()
        self.selectEnterpriseType()
        self.clickCancelButton()

    def cancelEnterpriseAddByCloseButton(self):
        """
        通过右上角关闭按钮取消添加参与方.
        """

        self.searchEnterprise()
        self.selectEnterpriseType()
        self.clickCloseButton()
